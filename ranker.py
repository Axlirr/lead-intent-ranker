#!/usr/bin/env python3
import csv
import argparse
from pathlib import Path

HIGH_INTENT_ROLES = [
    "reception", "customer service", "admin", "operations", "front desk", "clinic", "support"
]

OFFER_BONUS = {
    "AI Receptionist Automation": 20,
    "AI Customer Support + CRM Automation": 18,
    "Back-office Automation + Workflow Ops": 16,
    "Lead Capture + Follow-up Automation": 14,
    "Website Revamp / Conversion Landing Pages": 10,
}

def score_row(row: dict) -> tuple[int, list[str]]:
    score = 0
    reasons = []

    role = (row.get("Hiring Signal Role") or row.get("Niche Signal") or "").lower()
    email = (row.get("Email") or "").lower()
    quality = (row.get("Email Quality") or "").lower()
    offer = row.get("Recommended Offer") or ""

    if any(k in role for k in HIGH_INTENT_ROLES):
        score += 30
        reasons.append("high-intent-role")

    if email:
        score += 20
        reasons.append("has-email")

    if quality in ("verified_scraped", "scraped_high", "existing"):
        score += 15
        reasons.append(f"email-quality:{quality}")
    elif quality == "scraped_medium":
        score += 8
        reasons.append("email-quality:medium")

    if email.endswith(".sg") or ".sg" in email:
        score += 10
        reasons.append("sg-domain-email")

    if offer in OFFER_BONUS:
        score += OFFER_BONUS[offer]
        reasons.append("offer-fit")

    if any(x in email for x in ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]):
        score -= 8
        reasons.append("personal-email-penalty")

    return max(score, 0), reasons


def rank(input_csv: Path, output_csv: Path):
    rows = list(csv.DictReader(input_csv.open(encoding="utf-8")))
    ranked = []
    for r in rows:
        s, reasons = score_row(r)
        r["Intent Score"] = str(s)
        r["Intent Tier"] = "A" if s >= 70 else "B" if s >= 50 else "C"
        r["Score Reasons"] = ";".join(reasons)
        ranked.append(r)

    ranked.sort(key=lambda x: int(x["Intent Score"]), reverse=True)

    fields = []
    for r in ranked:
        for k in r.keys():
            if k not in fields:
                fields.append(k)

    with output_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(ranked)

    print(f"Ranked {len(ranked)} leads -> {output_csv}")


def main():
    ap = argparse.ArgumentParser(description="Rank lead CSV by outreach intent score")
    ap.add_argument("input", help="Input CSV path")
    ap.add_argument("-o", "--output", default="ranked_leads.csv", help="Output CSV path")
    args = ap.parse_args()
    rank(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()
