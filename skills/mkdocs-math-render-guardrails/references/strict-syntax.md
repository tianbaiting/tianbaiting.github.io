# Strict Syntax Rules for MkDocs Math

## 0) Runtime expectation

- `pymdownx.arithmatex` must run in `generic: true` mode.
- Material instant-loading must re-typeset formulas through `document$.subscribe(...)`.
- MathJax engine must be v3.

## 1) Canonical delimiters

- Inline math: `$...$`
- Display math:
  ```
  $$
  ...
  $$
  ```

Source Markdown must use dollar delimiters. Under `pymdownx.arithmatex: generic: true`, generated HTML may still contain `\(...\)` or `\[...\]` wrappers for MathJax. That runtime detail is expected; do not mirror those wrappers back into Markdown source.

Do not use `\(...\)` or `\[...\]` in new content.

## 2) Display block placement

- Keep opening `$$` and closing `$$` on their own lines.
- Keep one blank line before and after each display block.
- Do not append trailing text on the same line as `$$`.

Good:

```markdown
结论如下：

$$
f(x)=\int_{-\infty}^{\infty} e^{-t^2}\,dt
$$
```

Bad:

```markdown
结论如下：$$ f(x)=\int e^{-t^2}dt $$
```

## 3) Inline constraints

- Use inline math only for short expressions.
- Keep inline math on one physical line and keep delimiters tight near Chinese punctuation, for example `这是$E$，不是 $ E $`.
- If expression includes `\begin{...}` or multi-line structure, convert to display math.
- Natural language inside math must use `\text{...}`.

## 4) Containers and special blocks

- Avoid display math inside Markdown tables.
- Prefer placing display math outside list items and admonitions when possible.
- If math must stay inside list/admonition, keep indentation consistent and preserve blank lines around `$$`.

## 5) Delimiter integrity

- Ensure each inline `$` has a matching closing `$` on the same line.
- Ensure every `$$` has a matching closing `$$`.
- Ensure `\left` and `\right` are paired.
- Keep braces balanced for `_` and `^` arguments where needed.

## 6) Keep math separate from code

- Never place real formulas in fenced code blocks.
- When showing examples of source syntax, use code fences intentionally.
