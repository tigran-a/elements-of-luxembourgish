#!/usr/bin/env python3
"""
saz_spellcheck.py: Check Luxembourgish spelling and Eifeler Regel grammar using the saz.lu API.
Usage:
    python3 saz_spellcheck.py <file_path_or_directory>
"""

import sys
import os
import re
import requests

def clean_latex_line(line):
    line = line.strip()
    if not line:
        return None
        
    # Skip comments
    if line.startswith("%"):
        return None
        
    # Skip LaTeX metadata / layout commands
    skip_cmds = (
        "\\documentclass", "\\usepackage", "\\begin", "\\end", "\\chapter",
        "\\section", "\\subsection", "\\subsubsection", "\\vspace", "\\hspace",
        "\\newpage", "\\maketitle", "\\tableofcontents", "\\setcounter",
        "\\include", "\\includegraphics", "\\caption", "\\label", "\\ref",
        "\\rule", "\\setlength", "\\definecolor", "\\renewcommand", "\\babelfont"
    )
    if any(line.startswith(cmd) for cmd in skip_cmds):
        return None
    
    # Skip French and English translation lines
    if re.search(r"(Français|English)\s*:", line, re.IGNORECASE):
        return None
    if line.startswith(r"\textit{Cette leçon") or line.startswith(r"\textit{This lesson"):
        return None
    if line.startswith(r"\textit{(L'") or line.startswith(r"\textit{(Le ") or line.startswith(r"\textit{(La "):
        return None

    # Remove \item
    line = re.sub(r"\\item\b", "", line)

    # If the line has an explicit translation part (e.g. " : French / English" or " (French / English)"),
    # try to keep the Luxembourgish portion
    # Remove French / English glosses like (Le voisin / Male neighbor)
    line = re.sub(r"\([^)]*(?:voisin|neighbor|people|friend|weather|éventail|fan|vin|wine)[^)]*\)", "", line, flags=re.IGNORECASE)
    # Remove IPA brackets [ ... ]
    line = re.sub(r"\[[^\]]*\]", "", line)
    # Remove \rule{...}{...}
    line = re.sub(r"\\rule\{[^}]*\}\{[^}]*\}", "", line)
    
    # Strip LaTeX commands like \textit{...}, \textbf{...}
    line = re.sub(r"\\[a-zA-Z]+\*?\{([^\}]+)\}", r"\1", line)
    line = re.sub(r"\\[a-zA-Z]+", " ", line)
    line = re.sub(r"\$+", "", line)
    line = re.sub(r"[{}\\]", "", line)
    line = re.sub(r"\s+", " ", line).strip()
    
    return line if len(line) > 3 else None

def spellcheck_text(text):
    if not text.strip():
        return []
    
    url = "https://www.saz.lu/api/validateText"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Content-Type": "application/json",
        "Origin": "https://saz.lu",
        "Referer": "https://saz.lu/"
    }
    payload = {"text": text}
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get("sentences", [])
        else:
            print(f"[Warning] saz.lu API error: HTTP {response.status_code} for text: '{text[:50]}...'", file=sys.stderr)
            return []
    except requests.exceptions.RequestException as e:
        print(f"[Network Error] Could not reach saz.lu API: {e}", file=sys.stderr)
        return []

def check_file(file_path):
    print(f"Checking file: {file_path}")
    print("=" * 60)
    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    errors_found = 0
    for idx, line in enumerate(lines, start=1):
        cleaned = clean_latex_line(line)
        if not cleaned:
            continue
            
        sentences = spellcheck_text(cleaned)
        for sentence in sentences:
            for word in sentence.get("words", []):
                suggestions = word.get("suggestions")
                if suggestions:
                    # Focus primarily on GRAMMAR (EIFEL_RULE) and SPELLING
                    grammar_errs = suggestions.get("GRAMMAR", [])
                    spelling_errs = suggestions.get("SPELLING", [])
                    
                    if not grammar_errs and not spelling_errs:
                        continue
                        
                    word_val = word.get("value", "").strip()
                    if not word_val:
                        continue
                        
                    print(f"Line {idx}: '{cleaned}'")
                    print(f"  --> Word: '{word_val}'")
                    if grammar_errs:
                        for err in grammar_errs:
                            repls = err.get("replacements") or []
                            print(f"      [GRAMMAR / {err.get('key')}]: Suggestions -> {', '.join([str(r) for r in repls if r is not None])}")
                    if spelling_errs:
                        for err in spelling_errs:
                            repls = err.get("replacements") or []
                            print(f"      [SPELLING]: Suggestions -> {', '.join([str(r) for r in repls if r is not None])}")
                    print("-" * 60)
                    errors_found += 1
                    
    print(f"Done. Found {errors_found} issue(s) in {os.path.basename(file_path)}.")
    print("=" * 60)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 saz_spellcheck.py <file_path_or_directory>")
        sys.exit(1)
        
    path = sys.argv[1]
    if os.path.isdir(path):
        for f in sorted(os.listdir(path)):
            if f.endswith(".tex"):
                check_file(os.path.join(path, f))
    elif os.path.isfile(path):
        check_file(path)
    else:
        print(f"Path not found: {path}")

if __name__ == "__main__":
    main()
