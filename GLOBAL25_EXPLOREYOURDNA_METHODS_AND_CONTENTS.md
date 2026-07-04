Global25 and ExploreYourDNA methods and file contents

This file explains exactly what was done, which websites were used, which data were used, and what each uploaded file contains.

1. Data source

The coordinate system used here is Davidski Global25.

The specific coordinate type used for these runs was the modern scaled Global25 population-average coordinate format.

Source page for Davidski Global25:
https://eurogenes.blogspot.com/2019/07/getting-most-out-of-global25_12.html

The coordinate vectors used in this upload are:

Ashkenazi_Germany:
Ashkenazi_Germany,0.097319,0.142377,-0.014406,-0.049936,0.010925,-0.018769,-0.001974,-0.001754,0.009858,0.018843,0.003962,-0.001124,0.002512,-0.002670,-0.005049,0.003089,0.002203,-0.001698,-0.000779,-0.001126,-0.003344,-0.002696,0.000875,0.001386,0.000814

Italian_Jew:
Italian_Jew,0.094928,0.145627,-0.018667,-0.056493,0.011294,-0.024542,-0.003995,-0.002792,0.012885,0.019135,0.004514,0.000210,0.002156,-0.002876,-0.006610,-0.001233,-0.001200,-0.001052,-0.001119,-0.003589,-0.003906,-0.001546,-0.000123,0.002362,0.002874

These coordinates are preserved in:
global25_targets.csv

2. Websites used

Website 1:
ExploreYourDNA G25 Similarity Map
https://www.exploreyourdna.com/Tools/SimilitudeG25

How it was used:
The Ashkenazi_Germany Global25 coordinate vector was pasted into the G25 Similarity Map input box. The tool generated a geographic similarity map and a top-30 closest-populations ranking. The Italian_Jew Global25 coordinate vector was then pasted into the same tool, generating a second geographic similarity map and a second top-30 closest-populations ranking.

What the tool reports:
The page states that the map is built using the modern Davidski G25 dataset. Colored dots represent modern populations. Darker or more purple dots are closer genetically to the input coordinate. The displayed distance categories are:
GREAT (<0.02)
GOOD (<0.03)
AVERAGE (<0.04)
DISTANT (<0.06)
VERY DISTANT (>0.06)

Website 2:
ExploreYourDNA PCA Viewer - Modern Populations Comparison
https://www.exploreyourdna.com/Tools/PcaViewer

How it was used:
The Ashkenazi_Germany Global25 coordinate vector was pasted into the PCA Viewer input box. The tool generated a PC1 vs PC2 plot against modern populations.

What the tool reports:
The page states that the PCA viewer compares the input coordinate with modern world populations using PC1 vs PC2. It also states that the plot shows only PC1 and PC2, meaning 2 of the 25 dimensions, and that the closest-populations list uses the full 25-dimensional G25 distance.

3. Method for Ashkenazi_Germany similarity map

Input:
Ashkenazi_Germany modern scaled Global25 population average.

Tool:
ExploreYourDNA G25 Similarity Map.

Output preserved:
figure3_ashkenazi_germany_similarity_map.png
table8_ashkenazi_germany_top30_screenshot.png
table8_ashkenazi_germany_top30_global25.csv

Interpretation preserved in the manuscript:
The geographic similarity map localizes the strongest Ashkenazi_Germany similarity signal to Malta, southern Italy, Sicily, and the Aegean island zone. Northern Italy and Tuscany do not appear among the closest affinity centers.

4. Method for Ashkenazi_Germany PCA viewer

Input:
Ashkenazi_Germany modern scaled Global25 population average.

Tool:
ExploreYourDNA PCA Viewer - Modern Populations Comparison.

Output preserved:
figure6_ashkenazi_germany_pca_viewer.png

Interpretation preserved in the manuscript:
In the PC1-PC2 projection, Ashkenazi_Germany appears embedded in Southern European and central Mediterranean population space. It clusters visually near Italian Jewish and Southern Italian samples, especially Calabria and Sicily, and is separated from Levantine, Caucasus, and Armenian populations on the displayed axes.

5. Method for Ashkenazi_Germany full 25-dimensional ranking

Input:
Ashkenazi_Germany modern scaled Global25 population average.

Tool/source:
The full 25-dimensional ranking was taken from the ExploreYourDNA output associated with the PCA/similarity workflow and preserved as a screenshot and CSV table.

Output preserved:
ashkenazi_germany_full25_ranking_screenshot.png
ashkenazi_germany_full25_top10.csv

Recorded top 10:
1. Ashkenazi_Germany, 0.0000
2. Ashkenazi_Jew_Germany, 0.0000
3. Ashkenazi_Jew_France, 0.0067
4. Ashkenazi_France, 0.0067
5. Italian_Jew, 0.0132
6. Italian_Calabria_Reggio_Calabria (Calabrese), 0.0147
7. Ashkenazi_Jew_Austria, 0.0156
8. Ashkenazi_Austria, 0.0156
9. Italki (Italian_Jew), 0.0159
10. Ashkenazi_Poland, 0.0163

Interpretation preserved in the manuscript:
The nearest non-Ashkenazi populations in the full 25-dimensional ranking are Italian Jews and Southern Italians, specifically Calabrians. Levantine, Near Eastern, Caucasus, and Armenian populations do not appear among the closest populations in this preserved top-10 ranking.

6. Method for Italian_Jew similarity map

Input:
Italian_Jew modern scaled Global25 population average.

Tool:
ExploreYourDNA G25 Similarity Map.

Output preserved:
figure7_italian_jew_similarity_map.png
table12_italian_jew_top30_screenshot.png
table12_italian_jew_top30_global25.csv

Interpretation preserved in the manuscript:
The Italian_Jew similarity profile localizes overwhelmingly to southern Italy, Sicily, Malta, and the adjacent Aegean. Northern Italian populations are absent from the closest similarity ranks. This serves as an independent falsification test of Northern Italian proxy models, because Italian Jews would be expected to show Northern Italian nearest-neighbor peaks if the relevant Jewish Italian affinity were predominantly Northern Italian.

7. What each file contains

README_GLOBAL25_EXPLOREYOURDNA.md:
A short repository README describing the purpose of the upload, the tools used, the coordinate source, and the reproducibility limitation.

GLOBAL25_EXPLOREYOURDNA_METHODS_AND_CONTENTS.md:
This file. It explains the exact methods, websites, data inputs, output files, and interpretation.

global25_targets.csv:
Machine-readable CSV containing the two Global25 coordinate vectors used as inputs:
Ashkenazi_Germany
Italian_Jew

table8_ashkenazi_germany_top30_global25.csv:
Transcribed top-30 closest modern populations to Ashkenazi_Germany from the ExploreYourDNA G25 similarity map output.

table12_italian_jew_top30_global25.csv:
Transcribed top-30 closest modern populations to Italian_Jew from the ExploreYourDNA G25 similarity map output.

ashkenazi_germany_full25_top10.csv:
Transcribed top-10 full 25-dimensional Global25 distance ranking for Ashkenazi_Germany.

figure3_ashkenazi_germany_similarity_map.png:
Screenshot/export of the ExploreYourDNA G25 Similarity Map result for Ashkenazi_Germany.

figure6_ashkenazi_germany_pca_viewer.png:
Screenshot/export of the ExploreYourDNA PCA Viewer result for Ashkenazi_Germany.

figure7_italian_jew_similarity_map.png:
Screenshot/export of the ExploreYourDNA G25 Similarity Map result for Italian_Jew.

table8_ashkenazi_germany_top30_screenshot.png:
Screenshot of the top-30 closest modern populations to Ashkenazi_Germany.

table12_italian_jew_top30_screenshot.png:
Screenshot of the top-30 closest modern populations to Italian_Jew.

ashkenazi_germany_full25_ranking_screenshot.png:
Screenshot of the full 25-dimensional Global25 distance-ranking text for Ashkenazi_Germany.

reproduce_global25_distances.py:
A simple local Euclidean-distance script. It can recompute 25-dimensional Global25 distances if a compatible modern scaled Global25 comparator CSV is supplied by the user. This script documents the mathematical distance calculation used for ranking but does not redistribute the ExploreYourDNA backend comparator panel.

COPY_THIS_FILE_LIST.txt:
A simple list of the files in this upload.

8. What is preserved

Preserved:
Exact Ashkenazi_Germany coordinate input.
Exact Italian_Jew coordinate input.
ExploreYourDNA similarity-map output screenshots.
ExploreYourDNA PCA-viewer output screenshot.
Transcribed top-30 Ashkenazi_Germany similarity ranking.
Transcribed top-30 Italian_Jew similarity ranking.
Transcribed top-10 Ashkenazi_Germany full 25-dimensional ranking.
Simple Euclidean distance script for local reproduction with a supplied comparator panel.

9. What is not preserved

Not preserved:
The ExploreYourDNA backend source code.
The ExploreYourDNA full modern comparator database.
The complete full-distance output for every comparator population, unless supplied separately.
A local copy of the full Davidski modern scaled population-average dataset.

Reason:
Those are external resources. This addendum preserves the exact inputs, visible outputs, transcribed tables, and method notes needed to audit the manuscript figures and tables.

10. Plain methods paragraph for the repository or manuscript supplement

Global25 analyses used modern scaled Davidski Global25 population-average coordinates. The Ashkenazi_Germany and Italian_Jew coordinate vectors were entered into the ExploreYourDNA G25 Similarity Map to generate modern-population geographic similarity maps and top-30 nearest-neighbor rankings. Ashkenazi_Germany was also entered into the ExploreYourDNA PCA Viewer to generate a PC1-PC2 modern-population projection. The G25 Similarity Map page states that it uses the modern Davidski G25 dataset and displays colored dots by genetic distance to the input coordinate. The PCA Viewer page states that PC1-PC2 displays only two of the twenty-five Global25 dimensions and that the closest-populations list uses full 25-dimensional G25 distances. The repository preserves the exact coordinate inputs, exported screenshots, transcribed top-ranked populations, and a Euclidean distance script for local replication when a compatible modern scaled Global25 comparator file is supplied.
