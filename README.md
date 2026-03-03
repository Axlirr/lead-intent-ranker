# lead-intent-ranker

A tiny CLI that scores lead CSV rows so you can prioritize cold outreach.

## Why
Most outbound files are noisy. This tool gives each lead an **Intent Score** + **Intent Tier** so you can email highest-probability leads first.

## Input
Works with CSV columns like:
- `Company`
- `Hiring Signal Role` (or `Niche Signal`)
- `Recommended Offer`
- `Email`
- `Email Quality`

## Usage

```bash
python3 ranker.py input.csv -o ranked_leads.csv
```

## Output
Adds:
- `Intent Score` (0-100+)
- `Intent Tier` (A/B/C)
- `Score Reasons`

Sorted descending by score.

## Example

```bash
python3 ranker.py ../sg_niche_leads_verified_clean_2026-02-27.csv -o ranked.csv
head -n 10 ranked.csv
```

## License
MIT
