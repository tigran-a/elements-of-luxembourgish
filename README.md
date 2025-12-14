# Open Book: Elements of Luxembourgish

An open-source, community-driven project for learning the Luxembourgish language. This project aims to provide a helpful and modern resource for learners, compiled from a series of LaTeX-based lessons.

## About The Project

This repository contains the source code for "Elements of Luxembourgish," a growing collection of materials designed to help people learn the Luxembourgish language. The project is structured into lessons, each focusing on specific grammar points, vocabulary, and practical use cases, such as the "Sproochentest" (the official Luxembourgish language test).

The course is written in LaTeX and includes features such as:
*   Trilingual explanations (Luxembourgish, English, and French)
*   Vocabulary lists with images
*   Grammar explanations
*   Structured exercises for image description
*   Detailed examples with auto-generated images

## Getting Started

To compile this project and generate the final PDF textbook, you will need a working LaTeX distribution on your system (e.g., TeX Live, MiKTeX, or MacTeX).

### Prerequisites

*   A full LaTeX distribution that includes `lualatex`.
*   The `Noto` font family should be installed on your system.

### Compilation

The project is designed to be compiled with `lualatex` to support a wide range of Unicode characters and fonts. To generate the PDF, run the following command from the root of the project directory:

```sh
lualatex letz.tex
```

You may need to run the command twice to ensure the table of contents and cross-references are correctly generated. After successful compilation, a `letz.pdf` file will be created.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**. See the `LICENSE.txt` file for more information.

This license allows you to share and adapt the material for non-commercial purposes, as long as you give appropriate credit and distribute your contributions under the same license.


