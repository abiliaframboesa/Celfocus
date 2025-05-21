#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
import sys

def load_plans(csv_path):
    """
    Reads the plans CSV file and converts each row into a dictionary
    with appropriate data types.
    """
    plans = []
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for lineno, row in enumerate(reader, start=2):  # start=2 to account for header
            try:
                plan = {
                    "provider":      row["Provider"].strip(),
                    "plan_name":     row["Plan Name"].strip(),
                    "voice_minutes": int(row["Voice Minutes"]),
                    "data_mb":       int(row["Data (MB)"]),
                    "sms":           int(row["SMS"]),
                    "extras":        row.get("Extras", "").strip(),
                    "monthly_cost":  float(row["Monthly Cost"])
                }
            except KeyError as ke:
                print(f"[Error] Missing column on line {lineno}: {ke}", file=sys.stderr)
                continue
            except ValueError as ve:
                print(f"[Warning] Could not convert value on line {lineno}: {ve}", file=sys.stderr)
                continue

            plans.append(plan)
    return plans

def summarize_plans(plans):
    """
    Prints a brief summary of the loaded plans.
    """
    total = len(plans)
    if total == 0:
        print("No valid plans were loaded.")
        return

    # Find the cheapest and most expensive plans
    cheapest = min(plans, key=lambda p: p["monthly_cost"])
    most_expensive = max(plans, key=lambda p: p["monthly_cost"])

    print(f"Total plans loaded: {total}")
    print(f"Cheapest plan:     {cheapest['provider']} – {cheapest['plan_name']} at €{cheapest['monthly_cost']:.2f}/month")
    print(f"Most expensive plan: {most_expensive['provider']} – {most_expensive['plan_name']} at €{most_expensive['monthly_cost']:.2f}/month")

def main():
    # Absolute path to your mock plans CSV file
    csv_path = r"C:\Users\marti\Desktop\hackaton_celfocus\Celfocus\dashboard-comparativa-de-plafonds\public\plafonds_examples.csv"

    try:
        plans = load_plans(csv_path)
    except FileNotFoundError as fnf:
        print(fnf, file=sys.stderr)
        sys.exit(1)

    summarize_plans(plans)

    # You can extend this script to:
    # - Load the user's invoice CSV
    # - Calculate current costs based on usage
    # - Compare against each plan in `plans` to find maximum savings
    # - Return or save the recommendation data for further processing

if __name__ == "__main__":
    main()
