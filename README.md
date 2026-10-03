# Open Book: Elements of Luxembourgish

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Engine: LuaLaTeX](https://img.shields.io/badge/Engine-LuaLaTeX-blue.svg)](https://www.luatex.org/)
[![Volumes](https://img.shields.io/badge/Volumes-3%20Volumes%20(35%20Lessons)-brightgreen.svg)](#course-architecture)
[![Build Status](https://img.shields.io/github/actions/workflow/status/tigran-a/elements-of-luxembourgish/compile.yml?branch=main&label=PDF%20Build)](https://github.com/tigran-a/elements-of-luxembourgish/actions)

An open-source, community-driven textbook and reference series for learning the Luxembourgish language (*Lëtzebuergesch*), compiled from pedagogical LaTeX lessons with rich illustrations, audio-based dialogues, and trilingual translations (Luxembourgish, French, English).

---

## Download Pre-compiled PDFs

If you just want to read the book, you do not need to install LaTeX:
* Download the latest compiled PDFs directly from the **[GitHub Releases](https://github.com/tigran-a/elements-of-luxembourgish/releases)** page.

---

## Course Architecture

The textbook is organized into three progressive volumes:

| Volume | Source File | Compiled PDF | Lessons | Focus & Topics |
| :--- | :--- | :--- | :--- | :--- |
| **Volume 1** | `letz.tex` | `letz.pdf` | **1 – 20** | **Foundations & Everyday Life**: Pronunciation basics, family, house, work, orientation, shopping, basic tenses, and the illustrated picture dictionary. |
| **Volume 2** | `letz2.tex` | `letz2.pdf` | **21 – 31** | **Intermediate Topics**: Reflexive verbs, public services, health & doctor visits, leisure, expanded vocabulary, and complex sentence structures. |
| **Volume 3** | `letz3.tex` | `letz3.pdf` | **32 – 35+** | **Advanced & Conversational**: Civic & cultural events, fine-grained pronunciation (phonetic IPA for diphthongs), modal vs. prepositional infinitives, and conversational practice. |

---

## Key Features

* **Trilingual Structure**: All explanations, vocabulary glosses, and grammar notes are provided in Luxembourgish, French, and English.
* **Rigorous Eifeler Regel (n-Rule)**: Strict grammatical compliance with official Luxembourgish spelling regulations.
* **Illustrated Picture Dictionary**: Custom 300 DPI illustrations for concrete vocabulary items (`vokab_300dpi/`).
* **LOD Alignment**: Pronunciations and word entries cross-checked against the official *Lëtzebuerger Online Dictionnaire* ([lod.lu](https://lod.lu)).
* **Interactive Exercises**: Fill-in-the-blank vocabulary, translations, and oral practice questions with full answer keys.

---

## Repository Structure

```text
├── lessons/               # Individual lesson LaTeX files (lesson1.tex - lesson35.tex)
├── vokab_300dpi/          # High-resolution (300 DPI) vocabulary dictionary images
├── exercises/             # Supplementary topical worksheets (e.g., dative/accusative)
├── letz.tex               # Master document for Volume 1 (Lessons 1-20)
├── letz2.tex              # Master document for Volume 2 (Lessons 21-31)
├── letz3.tex              # Master document for Volume 3 (Lessons 32+)
├── saz_spellcheck.py      # Automated spellchecker & Eifeler rule validator (saz.lu API)
├── saz_concordancer.py    # Concordancer tool for authentic example sentences
├── verify_lessons.py      # LOD database integrity checker
├── Makefile               # Convenient build automation commands
├── .github/workflows/     # GitHub Actions CI for automatic PDF compilation
└── README.md              # Project documentation
```

---

## Linguistic & Quality Assurance Tools

The repository includes command-line tools to ensure orthographic accuracy:

### 1. Spellchecker & Eifeler Rule Validator
Validates Luxembourgish text and grammar rules using the official [saz.lu](https://saz.lu) API:
```bash
# Check a single lesson
python3 saz_spellcheck.py lessons/lesson35.tex

# Check an entire directory
python3 saz_spellcheck.py lessons/
```

### 2. Concordancer Corpus Search
Finds authentic Luxembourgish sentences with French/English translations from national corpora (LOD, RTL, government texts):
```bash
python3 saz_concordancer.py "Noperen" --limit 5
```

---

## Building from Source

### Prerequisites
* A full TeX Live or MacTeX installation with `lualatex`.
* The `Noto Sans` font family installed on your system.
* Python 3.10+ (for validation scripts).

### Quick Build with Make
```bash
# Compile individual volumes
make vol1    # Generates letz.pdf
make vol2    # Generates letz2.pdf
make vol3    # Generates letz3.pdf

# Compile all three volumes
make all

# Validate spelling on a lesson
make check LESSON=lessons/lesson35.tex

# Clean temporary build artifacts
make clean
```

### Manual Compilation
```bash
lualatex -interaction=nonstopmode letz3.tex
lualatex -interaction=nonstopmode letz3.tex   # Run twice to resolve TOC and cross-references
```

---

## Contributing

Contributions are welcome! Whether fixing a typo, improving a translation, or suggesting a new exercise:

1. **Fork** the repository.
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/lesson-improvements
   ```
3. **Verify spelling & grammar**:
   Run `python3 saz_spellcheck.py lessons/<modified_lesson>.tex` to ensure zero Eifeler Regel or spelling errors.
4. **Compile the PDF** to make sure LaTeX builds cleanly.
5. **Commit & Push**:
   ```bash
   git commit -m "Improve lesson 35 exercises and grammar explanations"
   git push origin feature/lesson-improvements
   ```
6. **Open a Pull Request**.

---

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**. See [LICENSE.txt](LICENSE.txt) for full terms.
