# Materials and Methods

## Study design

This study evaluates whether inferred Ashkenazi Jewish population placement changes when Southern European and central Mediterranean references are included explicitly instead of representing Europe through Northern Italian, Tuscan, Sardinian, or other northern-shifted proxies. The analyses are organized as a sensitivity test of reference population design. The primary target populations analyzed in the author-generated sections were Jew_Ashkenazi.HO in Human Origins-based qpAdm and FST analyses and Ashkenazi_Germany in modern Global25 coordinate analyses. Italian_Jew was analyzed as a falsification and comparison target in the Global25 framework.

The analyses do not report newly sequenced genotypes. They use published or web-hosted genotype resources and previously published coordinate data to generate new model comparisons, distance rankings, and derived tables.

## Genotype dataset used for qpAdm and FST analyses

The qpAdm and autosomal FST analyses reported in the submitted manuscript were run through the IllustrativeDNA Admix Lab using the Human Origins v62.0 dataset. The qpAdm target population was Jew_Ashkenazi.HO. The same target was used for the FST comparison table. The FST run log reported that the HO.geno packed ancestrymap dataset contained 21,945 samples and 584,131 SNPs and that allele frequencies were calculated from 118 samples across 13 populations for the reported FST comparison.

For qpAdm, the platform setting allsnps = TRUE was used. Under this setting, each f4-statistic is computed using the SNPs available for that statistic rather than forcing a single SNP intersection across all f4-statistics. The raw platform output logs record the number of SNPs used for each f4-statistic. Across the reported qpAdm runs, these values were generally between approximately 528,000 and 579,000 SNPs, depending on the population combination.

For autosomal FST, the option Adjust Pseudohaploids was set to NO. The raw FST output and final distance table are provided in outputs/raw/fst/ and tables/.

## qpAdm model specifications

The target population in all author-generated qpAdm runs was Jew_Ashkenazi.HO. Three alternative Italian source configurations were tested while holding the Lebanese and Russian source populations constant. The purpose was to compare Southern Italian, Northern Italian, and Central Italian source behavior under the same target and right-set configuration.

The three tested models were:

1. Jew_Ashkenazi.HO = Italian_South.HO + Lebanese.HO + Russian.DG
2. Jew_Ashkenazi.HO = Italian_North.HO + Lebanese.HO + Russian.DG
3. Jew_Ashkenazi.HO = Italian_Central.HO + Lebanese.HO + Russian.DG

The right-set populations were:

- Mbuti.DG
- Han.DG
- Chukchi.DG
- Karitiana.DG
- Papuan.DG
- Switzerland_Bichon_Epipaleolithic.SG
- Basque.DG
- Ju_hoan_North.DG
- Iranian.DG
- Yoruba.DG

The model specifications are stored in models/qpadm_model_specifications.tsv. The raw output logs are stored in outputs/raw/qpadm/. Derived results are stored in tables/table9_qpadm_results.csv and outputs/derived/table9_qpadm_results.csv.

Model fit was evaluated using the qpAdm p-value and feasibility status reported by the Admix Lab output. The Southern Italian model produced p = 0.1445 and was feasible. The Northern Italian model produced p = 0.0256 and was not feasible. The Central Italian model produced p = 0.0514 and was feasible but marginal.

## Autosomal FST analysis

Pairwise autosomal FST distances were calculated in the IllustrativeDNA Admix Lab using the Human Origins v62.0 dataset. The target population was Jew_Ashkenazi.HO. The selected comparator populations were:

- Sicilian.HO
- Italian_South.HO
- Maltese.HO
- Cretan.DG
- Jew_Iranian.HO
- Jew_Iraqi.DG
- Jew_Tunisian.HO
- Jew_Yemenite.HO
- Jew_Georgian.HO
- Jew_Moroccan.HO
- Jew_Libyan.HO
- Greek.HO

The output is stored in outputs/raw/fst/fst_jew_ashkenazi_raw_output.txt. The derived table is stored in tables/table10_fst_results.csv. The lowest reported distances to Jew_Ashkenazi.HO were Cretan.DG and Italian_South.HO at FST = 0.0049, followed by Sicilian.HO at 0.0052, Greek.HO at 0.0055, and Maltese.HO at 0.0066. Non-European Jewish comparator populations were more distant in this comparison set.

## FST calibration benchmarks

To provide interpretive scale for low FST values, additional calibration comparisons were reported. These include Italian_South.HO versus Maltese.HO at FST = 0.0036, Jew_Ashkenazi.HO versus Italian_South.HO at FST = 0.0049, and IBS_CanaryIslands.DG versus Spanish.HO at FST = 0.0038. The calibration table is stored in tables/table11_fst_calibration.csv.

The Canary Islands comparison was used as an external scale reference because modern Canary Islanders are Iberian-derived but also carry additional Indigenous North African ancestry. This comparison was included to show that FST values in the approximate range 0.003 to 0.005 can occur between closely related regional populations even when one population has additional ancestry and drift.

## Global25 coordinate analyses

Modern Global25 analyses used scaled modern Global25 population-average coordinates from the Davidski Global25 dataset. These analyses are descriptive and are not treated as formal ancestry proportion estimates. Euclidean distance in 25-dimensional scaled Global25 space was used for similarity ranking.

The Ashkenazi_Germany coordinate used in the manuscript is stored in data/global25_targets.csv and reproduced here:

Ashkenazi_Germany,0.097319,0.142377,-0.014406,-0.049936,0.010925,-0.018769,-0.001974,-0.001754,0.009858,0.018843,0.003962,-0.001124,0.002512,-0.002670,-0.005049,0.003089,0.002203,-0.001698,-0.000779,-0.001126,-0.003344,-0.002696,0.000875,0.001386,0.000814

The Italian_Jew coordinate used in the manuscript is also stored in data/global25_targets.csv:

Italian_Jew,0.094928,0.145627,-0.018667,-0.056493,0.011294,-0.024542,-0.003995,-0.002792,0.012885,0.019135,0.004514,0.000210,0.002156,-0.002876,-0.006610,-0.001233,-0.001200,-0.001052,-0.001119,-0.003589,-0.003906,-0.001546,-0.000123,0.002362,0.002874

The ExploreYourDNA G25 Similarity Map tool was used to generate distance rankings and geographic map screenshots. The top 30 ranked populations for Ashkenazi_Germany are stored in tables/table8_ashkenazi_germany_top30_global25.csv. The top 30 ranked populations for Italian_Jew are stored in tables/table12_italian_jew_top30_global25.csv.

The script scripts/01_reproduce_global25_distances.py can reproduce Euclidean distance rankings after the full modern scaled population-average comparator file is placed at data/external/modern_scaled_population_averages.csv. Because redistribution terms for the full comparator file may vary, only the exact target coordinates and derived top-30 tables are bundled here.

## PCA visualization

The Ashkenazi_Germany Global25 coordinate was entered into the ExploreYourDNA PCA Viewer for modern population comparison. The resulting PC1-PC2 visualization is included as a descriptive figure in figures/. This PCA plot is used as a visual companion to the Global25 distance table and is not treated as a formal admixture model.

## Literature-derived Y-DNA and autosomal summary tables

Y-DNA and literature-derived autosomal tables summarize published findings and do not introduce newly generated genotype analyses. Extracted values should be stored in data/y_dna_frequency_sources.csv with the following fields: study, year, population, sample_size, marker, frequency, value_type, and citation. Missing values are coded as NR. This allows the supplementary tables to be rebuilt from extraction records rather than only from retyped manuscript tables.

## Reproducibility workflow

The repository is structured so that reviewers can audit or reproduce each reported output:

1. Genotype and coordinate sources are documented in DATA_AVAILABILITY.md and data/access/GENOTYPE_RETRIEVAL.md.
2. qpAdm models are specified in models/qpadm_model_specifications.tsv.
3. FST comparisons are specified in models/fst_comparisons.tsv.
4. Raw qpAdm and FST outputs are stored in outputs/raw/.
5. Derived tables are stored in tables/ and outputs/derived/.
6. Global25 target coordinates are stored in data/global25_targets.csv.
7. Table-rebuild scripts and web-platform reproduction notes are stored in scripts/. The original qpAdm and FST analyses were not generated from local shell scripts.

The reported qpAdm and FST outputs were generated in the IllustrativeDNA Admix Lab web interface, not from local shell scripts. Reproduction of the submitted runs should be performed by entering the exact documented target, source, right-set, comparator labels, and settings into the same Human Origins v62.0 Admix Lab environment. The raw logs, screenshots, model specification tables, and derived CSV files preserve the submitted web-platform output trail.
