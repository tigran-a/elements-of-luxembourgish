# Makefile for Elements of Luxembourgish

TEXMFVAR ?= $(PWD)/tmp/texmfvar

.PHONY: all vol1 vol2 vol3 vol4 check help clean

help:
	@echo "Elements of Luxembourgish - Build Targets:"
	@echo "  make vol1    - Compile Volume 1 (Lessons 1-20 -> letz.pdf)"
	@echo "  make vol2    - Compile Volume 2 (Lessons 21-31 -> letz2.pdf)"
	@echo "  make vol3    - Compile Volume 3 (Lessons 32-39 -> letz3.pdf)"
	@echo "  make vol4    - Compile Volume 4 (Lessons 40+ -> letz4.pdf)"
	@echo "  make all     - Compile all four volumes"
	@echo "  make check   - Run spellcheck and Eifeler rule validation on a lesson"
	@echo "                 (e.g., make check LESSON=lessons/lesson40.tex)"
	@echo "  make clean   - Clean temporary LaTeX build artifacts"

all: vol1 vol2 vol3 vol4

vol1:
	mkdir -p $(TEXMFVAR)
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz.tex
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz.tex

vol2:
	mkdir -p $(TEXMFVAR)
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz2.tex
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz2.tex

vol3:
	mkdir -p $(TEXMFVAR)
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz3.tex
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz3.tex

vol4:
	mkdir -p $(TEXMFVAR)
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz4.tex
	TEXMFVAR=$(TEXMFVAR) lualatex -interaction=nonstopmode letz4.tex

check:
	python3 saz_spellcheck.py $(or $(LESSON),lessons/lesson40.tex)

clean:
	rm -f *.aux *.log *.toc *.out *.fls *.fdb_latexmk lessons/*.aux
