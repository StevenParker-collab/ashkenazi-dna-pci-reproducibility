# Submission package index

This repository is the reproducibility archive for:

Ashkenazi DNA Under the Microscope: Debunking the Europe-Levant Intermediate Myth

Start here:

1. `MANUSCRIPT.pdf` - the full revised preprint/manuscript with the expanded PCI-style Materials and Methods section.
2. `SUPPLEMENTARY_MATERIALS.pdf` - the supplementary materials PDF containing the supplementary tables and supporting material.
3. `README.md` - repository overview and navigation.
4. `ILLUSTRATIVEDNA_REPRODUCTION_PROTOCOL.md` - step-by-step reproduction protocol for the qpAdm and FST analyses performed in IllustrativeDNA Admix Lab.
5. `DATA_AVAILABILITY.md` - data sources, genotype access notes, and platform-accessibility notes.
6. `METHODS.md` - extended repository-level Methods documentation.
7. `models/` - model specification files for qpAdm and FST analyses.
8. `data/` - population labels, coordinate inputs, run index, and genotype source notes.
9. `outputs/raw/` - raw or transcribed platform outputs for qpAdm, FST, and Global25 analyses.
10. `tables/` and `outputs/derived/` - machine-readable result tables corresponding to the manuscript and supplementary tables.
11. `figures/` - screenshots and exported figures supporting the reported analyses.

Important note on analysis execution:

The reported qpAdm and FST analyses were performed through the public IllustrativeDNA Admix Lab web interface using the Human Origins v62.0 dataset. They were not executed with local shell scripts or direct command-line ADMIXTOOLS calls. The repository therefore provides exact web-platform reproduction instructions, exact `.HO`, `.DG`, and `.SG` population labels, model specifications, settings, raw exported outputs, and derived tables.

The Global25 analyses used Davidski Global25 coordinates and ExploreYourDNA tools. Repository-side scripts are supplied only for table rebuilding and coordinate-distance checking from supplied text inputs; they are not the original execution mechanism for the IllustrativeDNA qpAdm/FST runs.
