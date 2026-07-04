#!/usr/bin/env python3
"""Compute Euclidean distances from a Global25 target to a comparator file.

Expected files:
  data/global25_targets.csv
  data/external/modern_scaled_population_averages.csv

The comparator file should be CSV with label in the first column followed by 25 numeric coordinates.
Example row:
  Population,PC1,PC2,...,PC25
or
  Population,0.1,0.2,...

Usage:
  python scripts/01_reproduce_global25_distances.py --target Ashkenazi_Germany
  python scripts/01_reproduce_global25_distances.py --target Italian_Jew
"""
import argparse, csv, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ROOT / 'data' / 'global25_targets.csv'
COMPARATORS = ROOT / 'data' / 'external' / 'modern_scaled_population_averages.csv'
OUTDIR = ROOT / 'outputs' / 'derived'

def read_coords(path):
    rows = {}
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        first = next(reader)
        # Detect header by trying to parse second field
        try:
            float(first[1])
            rows[first[0]] = [float(x) for x in first[1:26]]
        except Exception:
            pass
        for r in reader:
            if not r or len(r) < 26:
                continue
            try:
                rows[r[0]] = [float(x) for x in r[1:26]]
            except ValueError:
                continue
    return rows

def dist(a,b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', required=True, choices=['Ashkenazi_Germany','Italian_Jew'])
    ap.add_argument('--comparators', default=str(COMPARATORS))
    ap.add_argument('--top', type=int, default=50)
    args = ap.parse_args()

    targets = read_coords(TARGETS)
    comp_path = Path(args.comparators)
    if not comp_path.exists():
        raise SystemExit(f'Missing comparator coordinate file: {comp_path}. Place the public Global25 modern scaled population-average file there.')
    comps = read_coords(comp_path)
    target = targets[args.target]
    rows = []
    for label, coords in comps.items():
        if label == args.target:
            continue
        rows.append((label, dist(target, coords)))
    rows.sort(key=lambda x: x[1])
    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / f'global25_{args.target.lower()}_distances.csv'
    with out.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['rank','population','distance'])
        for i,(label,d) in enumerate(rows[:args.top], 1):
            w.writerow([i,label,f'{d:.6f}'])
    print(out)

if __name__ == '__main__':
    main()
