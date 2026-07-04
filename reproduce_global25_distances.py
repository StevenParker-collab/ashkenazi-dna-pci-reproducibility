#!/usr/bin/env python3
import csv
import math
import argparse

def load_coordinates(path):
    rows = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 26:
                continue
            label = row[0].strip()
            try:
                coords = [float(x) for x in row[1:26]]
            except ValueError:
                continue
            rows[label] = coords
    return rows

def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

parser = argparse.ArgumentParser()
parser.add_argument("--targets", default="global25_targets.csv")
parser.add_argument("--comparators", required=True, help="Modern scaled Global25 comparator CSV")
parser.add_argument("--target", required=True, choices=["Ashkenazi_Germany", "Italian_Jew"])
parser.add_argument("--top", type=int, default=30)
args = parser.parse_args()

targets = load_coordinates(args.targets)
comparators = load_coordinates(args.comparators)

target = targets[args.target]
distances = sorted(
    [(label, euclidean(target, coords)) for label, coords in comparators.items()],
    key=lambda x: x[1]
)

print("rank,population,distance")
for rank, (label, distance) in enumerate(distances[:args.top], start=1):
    print(f"{rank},{label},{distance:.6f}")
