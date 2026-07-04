# Genotype retrieval and analysis access notes

This file addresses PCI's request that genotypic information and retrieval instructions be publicly accessible.

## Analyses actually performed for the submitted manuscript

The qpAdm and FST analyses reported in the manuscript were performed in the IllustrativeDNA Admix Lab web interface using the Human Origins v62.0 dataset.

URL:
https://illustrativedna.com/admix-lab/

The analyses were performed by selecting the exact `.HO`, `.DG`, and `.SG` population labels recorded in this repository. No local qpAdm, ADMIXTOOLS, or FST shell scripts were used to generate the submitted qpAdm and FST results.

## Reproduction pathway for submitted qpAdm/FST runs

To reproduce the submitted qpAdm and FST analyses, another user should open the IllustrativeDNA Admix Lab interface, select Human Origins v62.0, and enter the exact target, source, right-set, comparator labels, and settings listed in:

- ILLUSTRATIVEDNA_REPRODUCTION_PROTOCOL.md
- data/qpadm_target_and_sources.txt
- data/qpadm_right_set.txt
- data/fst_comparator_populations.txt
- models/qpadm_model_specifications.tsv
- models/fst_comparisons.tsv

The raw copied outputs are preserved in:

- outputs/raw/illustrativedna/

Screenshots are preserved in:

- figures/

## Genotypic information

The genotype panel used by the web platform is identified as Human Origins v62.0. The FST run output reported HO.geno with 21,945 samples and 584,131 SNPs, and allele frequencies calculated from 118 samples across 13 populations.

The underlying genotype files are not redistributed in this repository. Reproduction of the submitted runs therefore depends on access to the same IllustrativeDNA Admix Lab Human Origins v62.0 web environment.

## Independent command-line replication

A separate command-line ADMIXTOOLS replication could be performed using a publicly downloadable Human Origins or AADR-compatible genotype dataset and the same population definitions. Such a run would be an independent replication pathway, not the original analysis workflow used for the submitted qpAdm and FST outputs.
