# Reproducibility limitations and next steps

The reported qpAdm and FST analyses were performed in the IllustrativeDNA Admix Lab web interface using the Human Origins v62.0 dataset. No local shell scripts were used to generate those submitted qpAdm and FST outputs.

This repository corrects that record by documenting the web-platform workflow directly. It provides the exact target, source, right-set, and comparator population labels; the selected settings; the raw copied outputs; the screenshots; and the derived tables.

The main reproducibility limitation is that reproduction depends on access to the same IllustrativeDNA Admix Lab Human Origins v62.0 environment. The repository therefore makes the original web-platform analyses auditable and repeatable by another user in the same interface, but it does not include the underlying genotype files.

For an additional command-line replication, the same model definitions could be rerun in ADMIXTOOLS-compatible software using a separately available Human Origins or AADR genotype release. Such a command-line rerun would be an independent replication pathway, not the original analysis workflow used in the submitted manuscript.
