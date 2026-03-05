# extract_ner

## Daily automatic GitHub update

This repository now includes a GitHub Actions workflow that runs every day and updates `daily-heartbeat.md` automatically.

- Workflow file: `.github/workflows/daily-update.yml`
- Update script: `scripts/daily_update.py`
- Output file: `daily-heartbeat.md`

The workflow also supports manual runs from the **Actions** tab using `workflow_dispatch`.
