# Troubleshooting Matrix for MkDocs Math Rendering

## Symptom 1: Raw `$...$` or `$$...$$` appears on page

Likely causes:

- MathJax script not loaded
- `pymdownx.arithmatex` not enabled or misconfigured

Actions:

1. Check `mkdocs.yml` has `pymdownx.arithmatex`.
2. Check `extra_javascript` includes MathJax.
3. Ensure `docs/js/mathjax.js` is loaded before the MathJax v3 script.
4. Rebuild with `mkdocs build` and hard-refresh browser cache.

Note:

- Under `generic: true`, seeing `\(...\)` or `\[...\]` in generated HTML wrappers is normal. Seeing raw delimiters in the browser-rendered page is not.

## Symptom 2: Some formulas render, some do not

Likely causes:

- Mixed delimiter styles in the same file
- Unbalanced delimiters
- List/admonition indentation swallowing the math block
- Missing re-typeset after instant navigation

Actions:

1. Normalize delimiters to strict contract.
2. Check pair balance for `$`, `$$`, `\left`, `\right`.
3. Ensure `document$.subscribe(...)` exists in `docs/js/mathjax.js`.
4. Move unstable blocks outside lists/admonitions and test again.

## Symptom 3: Formula breaks near Chinese text or punctuation

Likely causes:

- Unmatched or ambiguous inline `$...$`
- Missing `\text{...}` for plain language inside math mode

Actions:

1. Keep source syntax as `$...$`, and ensure each inline formula closes on the same line.
2. Wrap plain language inside `\text{...}`.

## Symptom 4: Multi-line equation not rendering

Likely causes:

- Multi-line content written as inline math
- Display delimiters not on standalone lines

Actions:

1. Use display block only:
   ```
   $$
   \begin{aligned}
   ...
   \end{aligned}
   $$
   ```
2. Ensure blank lines around the display block.

## Symptom 5: Equations fail inside table cells

Likely causes:

- Markdown table parsing conflicts with math delimiters

Actions:

1. Move equations below the table.
2. Keep table cell content plain text and reference equations by label.

## Symptom 6: Regression after switching to MathJax v3 generic mode

Likely causes:

- `window.MathJax` config file not loaded
- Old MathJax v2 URL still present
- Existing pages still rely on legacy delimiter patterns

Actions:

1. Verify `extra_javascript` order: `js/mathjax.js` first, v3 script second.
2. Run migration scans from `qa-checklist.md`.
3. Batch-convert legacy delimiters.
4. Rebuild and verify all locales/pages.
