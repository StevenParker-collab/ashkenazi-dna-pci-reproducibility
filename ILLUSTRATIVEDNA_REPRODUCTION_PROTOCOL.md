# IllustrativeDNA Admix Lab reproduction protocol

This file records the exact web-platform procedure used for the qpAdm and FST analyses reported in the manuscript. The reported qpAdm and FST analyses were not run from local shell scripts. They were run in the IllustrativeDNA Admix Lab web interface, described by IllustrativeDNA as a do-it-yourself tool powered by qpAdm and available at https://illustrativedna.com/admix-lab/.

The purpose of this repository is therefore to preserve the exact web-interface inputs, settings, population labels, raw outputs, screenshots, and derived tables required to audit and reproduce the submitted runs inside the same Admix Lab environment.

## Platform

Platform: IllustrativeDNA Admix Lab
URL: https://illustrativedna.com/admix-lab/
Dataset selected in Admix Lab: Human Origins v62.0
Analyses performed: qpAdm and FST
Original execution mode: web browser interface
Local command-line scripts used for qpAdm/FST: none

## qpAdm reproduction steps

1. Open IllustrativeDNA Admix Lab.
2. Select the Human Origins v62.0 dataset.
3. Select qpAdm analysis.
4. Use target population: Jew_Ashkenazi.HO.
5. Use allsnps = TRUE.
6. Enter one of the following left/source configurations.
7. Enter the right-set populations listed below.
8. Run the model.
9. Compare the p-value, feasibility status, coefficients, standard errors, SNP-count log, and model output against the raw files in outputs/raw/illustrativedna/.

### qpAdm model 1: Southern Italian model

Target:
Jew_Ashkenazi.HO

Sources:
Italian_South.HO
Lebanese.HO
Russian.DG

Expected reported result:
p value: 0.1445
Feasibility: TRUE
Italian_South.HO: 69.97%, SE 4.93%
Lebanese.HO: 22.06%, SE 3.45%
Russian.DG: 7.97%, SE 2.74%

Raw output file:
outputs/raw/illustrativedna/illustrativedna_qpadm_south_italian_model_raw_output.txt

### qpAdm model 2: Northern Italian model

Target:
Jew_Ashkenazi.HO

Sources:
Italian_North.HO
Lebanese.HO
Russian.DG

Expected reported result:
p value: 0.0256
Feasibility: FALSE
Italian_North.HO: 54.53%, SE 3.88%
Lebanese.HO: 42.57%, SE 2.38%
Russian.DG: 2.90%, SE 3.10%

Raw output file:
outputs/raw/illustrativedna/illustrativedna_qpadm_north_italian_model_raw_output.txt

### qpAdm model 3: Central Italian model

Target:
Jew_Ashkenazi.HO

Sources:
Italian_Central.HO
Lebanese.HO
Russian.DG

Expected reported result:
p value: 0.0514
Feasibility: TRUE
Italian_Central.HO: 61.33%, SE 4.72%
Lebanese.HO: 33.83%, SE 3.01%
Russian.DG: 4.84%, SE 3.17%

Raw output file:
outputs/raw/illustrativedna/illustrativedna_qpadm_central_italian_model_raw_output.txt

### qpAdm right set used for all three models

Mbuti.DG
Han.DG
Chukchi.DG
Karitiana.DG
Papuan.DG
Switzerland_Bichon_Epipaleolithic.SG
Basque.DG
Ju_hoan_North.DG
Iranian.DG
Yoruba.DG

Right-set file:
data/qpadm_right_set.txt

Model specification table:
models/qpadm_model_specifications.tsv

## FST reproduction steps

1. Open IllustrativeDNA Admix Lab.
2. Select the Human Origins v62.0 dataset.
3. Select FST analysis.
4. Use left/target population: Jew_Ashkenazi.HO.
5. Use the comparator populations listed below.
6. Set Adjust Pseudohaploids to NO.
7. Run the FST calculation.
8. Compare the output against outputs/raw/illustrativedna/illustrativedna_fst_jew_ashkenazi_raw_output.txt and tables/table10_fst_results.csv.

### FST target

Jew_Ashkenazi.HO

### FST comparator populations

Sicilian.HO
Italian_South.HO
Maltese.HO
Cretan.DG
Jew_Iranian.HO
Jew_Iraqi.DG
Jew_Tunisian.HO
Jew_Yemenite.HO
Jew_Georgian.HO
Jew_Moroccan.HO
Jew_Libyan.HO
Greek.HO

### FST settings and dataset information reported by platform output

Dataset: Human Origins v62.0
Packed ancestrymap file reported in output: HO.geno
Samples reported in output: 21,945
SNPs reported in output: 584,131
Allele frequencies calculated from: 118 samples in 13 populations
Adjust Pseudohaploids: NO

Raw output file:
outputs/raw/illustrativedna/illustrativedna_fst_jew_ashkenazi_raw_output.txt

Comparator file:
data/fst_comparator_populations.txt

Model specification table:
models/fst_comparisons.tsv

## Why no qpAdm/FST shell scripts are provided as original commands

No local qpAdm or ADMIXTOOLS shell scripts were used to generate the submitted qpAdm and FST results. The analytic software was accessed through the IllustrativeDNA Admix Lab web interface, which exposes qpAdm-powered tools in a browser. Therefore, the reproducibility record for the original analyses consists of:

1. the web platform and URL;
2. the selected dataset, Human Origins v62.0;
3. the exact target/source/right-set/comparator population labels;
4. the exact settings, including allsnps = TRUE and Adjust Pseudohaploids = NO;
5. the platform-reported SNP and sample counts where available;
6. raw copied output logs;
7. screenshots of the web-interface outputs;
8. derived CSV tables.

Files formerly described as command templates should not be interpreted as original analysis scripts. This corrected repository labels qpAdm and FST reproduction as a web-platform reproduction protocol, not a local command-line workflow.
