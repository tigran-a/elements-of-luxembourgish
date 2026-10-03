# Open Book: Elements of Luxembourgish

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Engine: LuaLaTeX](https://img.shields.io/badge/Engine-LuaLaTeX-blue.svg)](https://www.luatex.org/)
[![Volumes](https://img.shields.io/badge/Volumes-3%20Volumes%20(35%20Lessons)-brightgreen.svg)](#course-architecture)
[![Build Status](https://img.shields.io/github/actions/workflow/status/tigran-a/elements-of-luxembourgish/compile.yml?branch=main&label=PDF%20Build)](https://github.com/tigran-a/elements-of-luxembourgish/actions)

An open-source, community-driven textbook and reference series for learning the Luxembourgish language (*Lëtzebuergesch*), compiled from pedagogical LaTeX lessons with rich illustrations, audio-based dialogues, and trilingual translations (Luxembourgish, French, English).

---

## Download Pre-compiled PDFs

If you just want to read the book, you do not need to install LaTeX. You can download the pre-compiled PDFs directly:

| Volume | Scope | Direct Download Link | Status |
| :--- | :--- | :--- | :--- |
| **Volume 1** | Lessons 1 – 20 | [**Download `letz.pdf`**](https://github.com/tigran-a/elements-of-luxembourgish/releases/download/v0.1.35/letz.pdf) | Finalized Release |
| **Volume 2** | Lessons 21 – 31 | [**Download `letz2.pdf`**](https://github.com/tigran-a/elements-of-luxembourgish/releases/download/v0.1.35/letz2.pdf) | Finalized Release |
| **Volume 3** | Lessons 32 – 35+ | [**Download `letz3.pdf`**](https://github.com/tigran-a/elements-of-luxembourgish/releases/download/v0.1.35/letz3.pdf) | Active / Growing |

> **Note on Volumes:** The division into Volumes 1, 2, and 3 is **chronological, not level-specific**. Volume 1 is not "lower level" or strictly A1 compared to Volume 3. Rather, each volume contains a rich, accessible cross-section of everyday themes, grammar points, illustrated vocabulary, and conversational dialogues compiled as the course progresses. Volumes 1 and 2 are finalized and stable; new lessons are continuously added to Volume 3.

---

## Linguistic Methodology & Data Sources

To ensure highest orthographic and lexical standard, the materials in this course are systematically developed and cross-referenced with official Luxembourgish linguistic resources:

* **[Lëtzebuerger Online Dictionnaire (LOD)](https://lod.lu/)**:
  Used as the primary lexical authority for official spellings, word genders, plural forms, complete verb conjugation paradigms, and International Phonetic Alphabet (IPA) pronunciations.
* **[Saz.lu Schreifassistent](https://saz.lu/)**:
  Used to validate sentences for standard orthography and strict compliance with the **Eifeler Regel** (*n-Rule*), ensuring grammatical accuracy across all dialogues and exercises.
* **[Saz.lu Concordancer](https://saz.lu/concordancer)**:
  Used to source authentic, real-world Luxembourgish sentences from national media and institutional corpora (LOD, RTL, government publications) with French, English, and German translations.
* **[Spellchecker.lu](https://spellchecker.lu/)**:
  Used as an additional validation layer for Luxembourgish vocabulary and morphology.

---

## Key Features

* **Trilingual Structure**: All explanations, vocabulary glosses, and grammar notes are provided in Luxembourgish, French, and English.
* **Strict Eifeler Regel (n-Rule)**: Consistent application of official Luxembourgish sandhi rules (*n* retention and elision).
* **Illustrated Picture Dictionary**: Custom 300 DPI vector-style illustrations for concrete vocabulary items (`vokab_300dpi/`).
* **Practical Everyday Scenarios**: Realistic dialogues and Q&As reflecting everyday life in Luxembourg (work, neighborhood, administration, health, culture, hobbies).
* **Interactive Exercises**: Fill-in-the-blank vocabulary tasks, translation exercises, and oral practice questions with complete solutions.

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
├── saz_concordancer.py    # Concordancer tool for authentic sentence corpus search
├── verify_lessons.py      # LOD database integrity checker
├── Makefile               # Convenient build automation commands
├── .github/workflows/     # GitHub Actions CI for automatic PDF compilation
└── README.md              # Project documentation
```

---

## Linguistic & Quality Assurance Tools

The repository includes command-line tools to assist contributors and learners:

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
