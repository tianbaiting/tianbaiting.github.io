# QA Checklist for Markdown Math

## Pre-edit checks

1. Confirm math stack in `mkdocs.yml`:
   - `pymdownx.arithmatex` present
   - `pymdownx.arithmatex: generic: true`
   - `extra_javascript` includes `js/mathjax.js`
   - MathJax v3 script `https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js` included
2. Determine delimiter policy for the task:
   - Default policy in this skill: inline `$...$`, display `$$...$$` in source Markdown
3. Identify target files under `docs/`.

## Mechanical scans

Run these scans from repo root:

```bash
rg -n '\\\\\\(|\\\\\\)|\\\\\\[|\\\\\\]' docs
python3 scripts/check_math_dollar_blocks.py docs
rg -n '^\\s*\\$\\$.*\\S' docs
```

Interpretation:

- First command finds legacy `\(...\)` and `\[...\]` delimiters to migrate.
- Second command validates display `$$ ... $$` block structure across the target files.
- Third command flags `$$` lines with trailing content.

## Structural checks

1. Verify each `$$` block has blank lines around it.
2. Verify formulas are not mixed with HTML tags on one line.
3. Verify formulas in lists/admonitions still align with container indentation.
4. Verify formulas are not placed inside tables unless unavoidable.
5. Verify inline `$...$` formulas stay on one line and do not use spaced delimiters like `$ E $` unless literal spaces are intended.

## Build checks

1. Run:
   ```bash
   mkdocs build
   ```
2. Open generated pages and confirm formulas are rendered as math, not raw delimiters.
3. Navigate between pages and verify formulas still render after instant loading.
4. If rendered output is still broken, use `troubleshooting.md`.
