# Ashkenazi DNA PCI reproducibility repository

Repository for reproducibility materials supporting the manuscript:

Ashkenazi DNA Under the Microscope: Debunking the Europe-Levant Intermediate Myth

Repository URL:
https://github.com/StevenParker-collab/ashkenazi-dna-pci-reproducibility

## Purpose

This repository is organized to address the PCI Evol Biol reproducibility request. It records the exact data sources, software platform, population labels, model specifications, raw outputs, derived tables, and manuscript methods text used for the submitted analyses.

## Important clarification

The qpAdm and FST analyses reported in the manuscript were not run from local scripts. They were run in the IllustrativeDNA Admix Lab web interface using the Human Origins v62.0 dataset.

IllustrativeDNA Admix Lab URL:
https://illustrativedna.com/admix-lab/

The repository therefore preserves the exact web-platform inputs and outputs:

- target population labels;
- source population labels;
- right-set populations;
- FST comparator populations;
- selected settings, including allsnps = TRUE and Adjust Pseudohaploids = NO;
- raw copied output logs;
- screenshots of output pages;
- derived CSV tables used in the manuscript.

The file ILLUSTRATIVEDNA_REPRODUCTION_PROTOCOL.md is the main reproduction guide for the qpAdm and FST results.

## Repository contents

- ILLUSTRATIVEDNA_REPRODUCTION_PROTOCOL.md: exact web-interface reproduction protocol for the qpAdm and FST analyses.
- METHODS.md: formal methods text for the revised manuscript.
- MANUSCRIPT_MATERIALS_AND_METHODS_REPLACEMENT.md: copy-ready manuscript replacement section.
- DATA_AVAILABILITY.md: data and software availability statement.
- PCI_RESPONSE_LETTER.md: draft response to PCI.
- data/: exact population labels, target coordinates, and genotype access notes.
- models/: qpAdm and FST model specification tables.
- outputs/raw/illustrativedna/: raw copied IllustrativeDNA Admix Lab outputs.
- outputs/derived/ and tables/: derived CSV tables used in the manuscript and supplement.
- figures/: screenshots and exported figures from the reported analyses.
- scripts/: table-rebuild scripts and web-platform reproduction notes. The qpAdm and FST reported results were not generated from these scripts.
- supplementary/: supplementary PDF.
- docs/: manuscript and PCI-related documentation.

## Reviewer checklist

1. Open ILLUSTRATIVEDNA_REPRODUCTION_PROTOCOL.md.
2. Confirm the platform: IllustrativeDNA Admix Lab, Human Origins v62.0.
3. Check data/qpadm_target_and_sources.txt and data/qpadm_right_set.txt.
4. Check models/qpadm_model_specifications.tsv.
5. Compare the qpAdm raw output files in outputs/raw/illustrativedna/ with Table 9.
6. Check data/fst_comparator_populations.txt and models/fst_comparisons.tsv.
7. Compare the FST raw output in outputs/raw/illustrativedna/ with Table 10.
8. Check data/global25_targets.csv for the exact Ashkenazi_Germany and Italian_Jew coordinates.
9. Use scripts/02_rebuild_tables.py to rebuild CSV tables from the stored derived tables.

## Reproducibility note

Because the submitted qpAdm and FST analyses were run in a web platform, this repository does not present shell scripts as the original analytic commands. Reproduction of the original results should be performed by entering the exact recorded population labels and settings into the same IllustrativeDNA Admix Lab Human Origins v62.0 interface. The raw outputs and screenshots provide the audit trail for those submitted runs.
