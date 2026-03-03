# lead-intent-ranker

A practical Python CLI that scores and ranks outreach leads so you can prioritize high-intent prospects first.

## Why

Most lead sheets are noisy. Sending outreach in file order wastes time and lowers reply rates.

`lead-intent-ranker` adds a simple scoring layer and gives you:

- **Intent Score** (numeric)
- **Intent Tier** (A / B / C)
- **Score Reasons** (transparent scoring explanation)

## Features

- ✅ CSV in / CSV out
- ✅ Human-readable scoring reasons per row
- ✅ Tiering for quick prioritization
- ✅ Works with hiring-signal and niche-signal lead files
- ✅ No external dependencies

## Installation

```bash
git clone https://github.com/Axlirr/lead-intent-ranker.git
cd lead-intent-ranker
```

## Usage

```bash
python3 ranker.py input.csv -o ranked_leads.csv
```

## Supported input columns

The tool is resilient to missing columns, but works best with:

- `Company`
- `Hiring Signal Role` (or `Niche Signal`)
- `Recommended Offer`
- `Email`
- `Email Quality`

## Output columns added

- `Intent Score`
- `Intent Tier` (`A` >= 70, `B` >= 50, else `C`)
- `Score Reasons`

Rows are sorted descending by `Intent Score`.

## Example

```bash
python3 ranker.py ../sg_niche_leads_verified_clean_2026-02-27.csv -o ranked.csv
head -n 8 ranked.csv
```

## Scoring logic (summary)

Current heuristic considers:

- high-intent role keywords
- email presence and quality
- Singapore domain signal
- offer relevance bonus
- penalty for generic personal inboxes

You can customize this in `ranker.py` (`HIGH_INTENT_ROLES`, `OFFER_BONUS`, and `score_row`).

## Roadmap

- configurable scoring via YAML
- domain enrichment hooks
- optional dedupe mode by company/email
- confidence calibration from response outcomes

## License

MIT
