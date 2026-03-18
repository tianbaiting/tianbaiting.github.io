---
name: mkdocs-math-render-guardrails
description: Enforce strict and deterministic math rendering rules for MkDocs Markdown (Material + pymdownx.arithmatex + MathJax v3). Use when writing or repairing formulas in docs/*.md, converting imported notes with mixed delimiters, or debugging equations that fail to render and show raw TeX text.
---

# MkDocs Math Render Guardrails

Use this skill to stop equation rendering regressions by forcing a single canonical syntax and a repeatable troubleshooting flow.

## Canonical Contract (Strict)

Apply these rules unless the user explicitly asks for a different delimiter policy:

1. Use `$...$` for inline math in source Markdown. Do not use `\(...\)` or `\[...\]` in new content.
2. Use `$$` blocks for display math. Keep opening and closing `$$` on separate lines.
3. Keep one blank line before and after each `$$` block.
4. Do not put display math on the same line as regular text.
5. Do not mix raw HTML tags and math delimiters on the same line.
6. Do not write formulas inside Markdown tables unless absolutely required.
7. Keep math delimiters out of code fences.
8. Keep delimiter pairs balanced: `$...$`, `$$...$$`, `\left...\right`.
9. Use `\text{...}` for natural language text inside formulas.
10. In list/admonition contexts, prefer moving formula blocks outside the container if rendering is unstable.

## Workflow

1. Read `mkdocs.yml` and confirm `pymdownx.arithmatex` and MathJax are enabled.
   - Require `pymdownx.arithmatex: generic: true`
   - Require `extra_javascript` includes `js/mathjax.js` and MathJax v3 script
2. Normalize target markdown files to the canonical contract in source Markdown.
3. Run the checks in `references/qa-checklist.md`.
4. If issues remain, follow `references/troubleshooting.md`.
5. Rebuild with `mkdocs build` and verify equations render instead of showing raw TeX delimiters.

## Rewrite Rules

- Inline: `\(E=mc^2\)` -> `$E=mc^2$`
- Display:
  - From `\[ ... \]` to:
    ```
    $$
    ...
    $$
    ```
- Mixed line: `结论：$$ ... $$` -> split into paragraph + standalone display block.

## Repo-Specific Hardening

For this repository, use Material official instant-loading MathJax setup:

```yaml
markdown_extensions:
  - pymdownx.arithmatex:
      generic: true

extra_javascript:
  - js/mathjax.js
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js
```

In `docs/js/mathjax.js`, configure `window.MathJax` and trigger re-typeset with `document$.subscribe(...)` after each instant navigation.

Under `pymdownx.arithmatex: generic: true`, the generated HTML may still contain `\(...\)` and `\[...\]` as MathJax-facing runtime wrappers. That is expected in the render pipeline. Keep `$...$` and `$$...$$` as the authoring syntax in Markdown source.

## Resources
- `references/strict-syntax.md`: Allowed/disallowed syntax and deterministic examples.
- `references/qa-checklist.md`: Fast checks before and after edits.
- `references/troubleshooting.md`: Symptom-to-fix mapping for rendering failures.
