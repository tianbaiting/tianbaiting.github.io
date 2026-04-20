#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class FileChange:
    file_path: Path
    replacements: int


def is_fence_line(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def list_markdown_files(paths: Iterable[Path]) -> list[Path]:
    collected: list[Path] = []
    for path in paths:
        if path.is_file():
            if path.suffix.lower() == ".md":
                collected.append(path)
            continue
        if path.is_dir():
            collected.extend(sorted(path.rglob("*.md")))
    return sorted(set(collected))


def strip_bold_markers_from_line(line: str) -> tuple[str, int]:
    if "**" not in line:
        return line, 0

    output: list[str] = []
    replacements = 0
    in_code_span = False
    code_span_ticks = 0
    idx = 0

    while idx < len(line):
        if line[idx] == "`":
            tick_end = idx
            while tick_end < len(line) and line[tick_end] == "`":
                tick_end += 1

            tick_count = tick_end - idx
            output.append(line[idx:tick_end])

            if not in_code_span:
                in_code_span = True
                code_span_ticks = tick_count
            elif tick_count == code_span_ticks:
                in_code_span = False
                code_span_ticks = 0

            idx = tick_end
            continue

        if not in_code_span and line.startswith("**", idx):
            replacements += 1
            idx += 2
            continue

        output.append(line[idx])
        idx += 1

    return "".join(output), replacements


def process_file(file_path: Path, apply_changes: bool) -> FileChange | None:
    original = file_path.read_bytes().decode("utf-8")
    lines = original.splitlines(keepends=True)

    updated_lines: list[str] = []
    in_fence = False
    replacements = 0

    for line in lines:
        if is_fence_line(line):
            updated_lines.append(line)
            in_fence = not in_fence
            continue

        if in_fence:
            updated_lines.append(line)
            continue

        updated_line, line_replacements = strip_bold_markers_from_line(line)
        updated_lines.append(updated_line)
        replacements += line_replacements

    if replacements == 0:
        return None

    if apply_changes:
        file_path.write_bytes("".join(updated_lines).encode("utf-8"))

    return FileChange(file_path=file_path, replacements=replacements)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove Markdown bold markers `**` from Markdown files."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["docs"],
        help="Markdown files or directories to process (default: docs).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files that would change without modifying them.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path.cwd()
    raw_paths = [Path(path) for path in args.paths]
    resolved_paths = [
        (repo_root / path).resolve() if not path.is_absolute() else path.resolve()
        for path in raw_paths
    ]
    files = list_markdown_files(resolved_paths)

    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 1

    changes: list[FileChange] = []
    for file_path in files:
        change = process_file(file_path, apply_changes=not args.check)
        if change is not None:
            changes.append(change)

    if not changes:
        print("No Markdown bold markers found.")
        return 0

    action = "Would update" if args.check else "Updated"
    for change in changes:
        print(f"{action} {change.file_path.relative_to(repo_root)} ({change.replacements} replacements)")

    print(f"{action} {len(changes)} files, removed {sum(change.replacements for change in changes)} markers.")
    return 1 if args.check else 0


if __name__ == "__main__":
    raise SystemExit(main())
