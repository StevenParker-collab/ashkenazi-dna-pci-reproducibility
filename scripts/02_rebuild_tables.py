#!/usr/bin/env python3
"""Rebuild derived manuscript tables from stored CSV/TSV inputs.

This script does not rerun genotype analyses. It rebuilds derived tables from the
model specifications and stored output tables included in the repository.
"""
from pathlib import Path
import csv, shutil
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs' / 'derived'
OUT.mkdir(parents=True, exist_ok=True)

# Copy table CSVs into derived outputs.
for src in (ROOT / 'tables').glob('*.csv'):
    shutil.copy2(src, OUT / src.name)

# Build a compact qpAdm summary from model specifications.
spec = ROOT / 'models' / 'qpadm_model_specifications.tsv'
out = OUT / 'qpadm_model_summary_from_specs.csv'
with spec.open(newline='', encoding='utf-8') as f, out.open('w', newline='', encoding='utf-8') as g:
    r = csv.DictReader(f, delimiter='\t')
    w = csv.writer(g)
    w.writerow(['model_id','target','source_populations','p_value','feasible','coefficients_percent','standard_errors_percent'])
    for row in r:
        w.writerow([row['model_id'], row['target'], row['source_populations'], row['p_value'], row['feasible'], row['coefficients_percent'], row['standard_errors_percent']])

# Build a compact FST summary from comparison specifications.
spec = ROOT / 'models' / 'fst_comparisons.tsv'
out = OUT / 'fst_summary_from_specs.csv'
with spec.open(newline='', encoding='utf-8') as f, out.open('w', newline='', encoding='utf-8') as g:
    r = csv.DictReader(f, delimiter='\t')
    w = csv.writer(g)
    w.writerow(['population_1','population_2','fst_distance','standard_error'])
    for row in r:
        w.writerow([row['population_1'], row['population_2'], row['fst_distance'], row['standard_error']])

print(f'Rebuilt derived tables in {OUT}')
