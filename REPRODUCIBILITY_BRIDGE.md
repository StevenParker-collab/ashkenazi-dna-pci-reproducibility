# Reproducibility Bridge for Ashkenazi DNA Analysis

## 1. Genotype Data Source

All analyses are based on the Human Origins dataset (v62.0).  
Genotype access is through publicly available Human Origins format files as used in population genetics literature.

No proprietary or private genotype data were used.

## 2. Analytical Environment

All analyses were performed using:
- IllustrativeDNA AdmixLab qpAdm interface (web-based qpAdm implementation)
- FST calculations via standard population genetics distance methods
- Global25 coordinates from IllustrativeDNA ecosystem

No custom scripts or command-line ADMIXTOOLS runs were used.

## 3. qpAdm Configuration

Target: Jew_Ashkenazi.HO

Left populations: defined in models/qpadm_target_and_sources.txt  
Right populations: defined in models/qpadm_right_set.txt  

Settings:
- ALLSNPS: TRUE (AdmixLab default)
- LD pruning: not applied (handled internally by dataset defaults)
- MAF filtering: not applied beyond Human Origins preprocessing
- Missingness: dataset default

## 4. Reproducibility Steps

1. Load Human Origins v62.0 in AdmixLab
2. Select target Jew_Ashkenazi.HO
3. Load left/right populations from repository files
4. Run qpAdm using default AdmixLab settings
5. Export results

## 5. Statement

All results are reproducible using Human Origins v62.0 and IllustrativeDNA AdmixLab without additional custom scripts.
