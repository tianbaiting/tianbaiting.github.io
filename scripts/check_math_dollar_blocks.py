#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Issue:
    file_path: Path
    line_no: int
    code: str
    message: str


def is_fence_line(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def is_blank_line(lines: list[str], idx: int) -> bool:
    if idx < 0 or idx >= len(lines):
        return True
    return lines[idx].strip() == ""


def list_markdown_files(paths: Iterable[Path]) -> list[Path]:
    collected: list[Path] = []
    for p in paths:
        if p.is_file():
            if p.suffix.lower() == ".md":
                collected.append(p)
            continue
        if p.is_dir():
            collected.extend(sorted(p.rglob("*.md")))
    return sorted(set(collected))


def list_staged_markdown_files(repo_root: Path) -> list[Path]:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
    result = subprocess.run(
        cmd,
        cwd=repo_root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git diff --cached failed")

    files: list[Path] = []
    for raw in result.stdout.splitlines():
        raw = raw.strip()
        if not raw or not raw.endswith(".md"):
            continue
        candidate = (repo_root / raw).resolve()
        if candidate.exists():
            files.append(candidate)
    return sorted(set(files))


def analyze_file(file_path: Path) -> list[Issue]:
    issues: list[Issue] = []
    lines = file_path.read_text(encoding="utf-8").splitlines()

    in_fence = False
    fence_markers: list[int] = []
    markers: list[int] = []

    for idx, line in enumerate(lines):
        line_no = idx + 1

        if is_fence_line(line):
            in_fence = not in_fence
            fence_markers.append(line_no)
            continue

        if "$$" not in line:
            continue

        stripped = line.strip()
        if in_fence:
            issues.append(
                Issue(
                    file_path=file_path,
                    line_no=line_no,
                    code="DOLLAR_IN_CODE_FENCE",
                    message="Found `$$` inside fenced code block; this can hide real math mistakes.",
                )
            )
            continue

        if stripped != "$$":
            issues.append(
                Issue(
                    file_path=file_path,
                    line_no=line_no,
                    code="NON_STANDALONE_DOLLAR_BLOCK",
                    message="`$$` must be on its own line with no surrounding text.",
                )
            )
            continue

        markers.append(line_no)

    if len(fence_markers) % 2 != 0:
        issues.append(
            Issue(
                file_path=file_path,
                line_no=fence_markers[-1],
                code="UNBALANCED_FENCE",
                message="Unbalanced fenced code block; math checks may be unreliable below this line.",
            )
        )

    if len(markers) % 2 != 0:
        issues.append(
            Issue(
                file_path=file_path,
                line_no=markers[-1],
                code="UNPAIRED_DOLLAR_BLOCK",
                message="Missing closing `$$` for display math block.",
            )
        )

    in_math = False
    open_line = -1
    for marker_line in markers:
        marker_idx = marker_line - 1
        if not in_math:
            if not is_blank_line(lines, marker_idx - 1):
                issues.append(
                    Issue(
                        file_path=file_path,
                        line_no=marker_line,
                        code="MISSING_BLANK_BEFORE_OPEN",
                        message="Add a blank line before opening `$$`.",
                    )
                )
            if is_blank_line(lines, marker_idx + 1):
                issues.append(
                    Issue(
                        file_path=file_path,
                        line_no=marker_line,
                        code="EMPTY_MATH_BLOCK",
                        message="Math block is empty right after opening `$$`.",
                    )
                )
            in_math = True
            open_line = marker_line
        else:
            if is_blank_line(lines, marker_idx - 1):
                issues.append(
                    Issue(
                        file_path=file_path,
                        line_no=marker_line,
                        code="EMPTY_MATH_BLOCK",
                        message="Math block is empty right before closing `$$`.",
                    )
                )
            if not is_blank_line(lines, marker_idx + 1):
                issues.append(
                    Issue(
                        file_path=file_path,
                        line_no=marker_line,
                        code="MISSING_BLANK_AFTER_CLOSE",
                        message="Add a blank line after closing `$$`.",
                    )
                )
            if marker_line - open_line <= 1:
                issues.append(
                    Issue(
                        file_path=file_path,
                        line_no=marker_line,
                        code="EMPTY_MATH_BLOCK",
                        message="Display math block has no content between opening and closing `$$`.",
                    )
                )
            in_math = False
            open_line = -1

    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check Markdown display math `$$ ... $$` formatting before commit."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["docs"],
        help="Markdown files or directories to check (default: docs).",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Check staged Markdown files only.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path.cwd()

    if args.staged:
        try:
            files = list_staged_markdown_files(repo_root)
        except RuntimeError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2
    else:
        raw_paths = [Path(p) for p in args.paths]
        normalized = [(repo_root / p).resolve() if not p.is_absolute() else p for p in raw_paths]
        files = list_markdown_files(normalized)

    if not files:
        print("No Markdown files to check.")
        return 0

    issues: list[Issue] = []
    for file_path in files:
        issues.extend(analyze_file(file_path))

    if not issues:
        print(f"OK: checked {len(files)} Markdown file(s), no `$$` block issues found.")
        return 0

    print(f"FAILED: found {len(issues)} issue(s) in {len(files)} Markdown file(s):")
    for issue in sorted(issues, key=lambda x: (str(x.file_path), x.line_no, x.code)):
        rel = issue.file_path.relative_to(repo_root)
        print(f"{rel}:{issue.line_no}: [{issue.code}] {issue.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
