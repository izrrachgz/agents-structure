#!/usr/bin/env python3
"""Screen a shell tool request for the command patterns listed below.

The registration supplies one JSON event on stdin. The handler inspects
tool_input.command as text. A match emits a PreToolUse denial on stdout.
A recognized command with no match produces no output. Malformed JSON is
ignored. Keep command contents out of diagnostics because arguments may
contain private data.

For a new pattern, document the operation and its impact, then exercise the
script with a matching event and an ordinary command with similar wording.
Include quoting, shell flags and platform-specific variants relevant to the
rule. Regex matching can miss shell forms or match text inside arguments.
The sandbox and execution policy supply the underlying access controls.
"""

from __future__ import annotations

import json
import re
import sys


BLOCKED = (
    (re.compile(r"(?:^|[;&|]\s*)rm\s+-(?:rf|fr)\s+(?:/|~|\$HOME|\$\{HOME\})(?:\s|$)", re.I),
     "Refusing recursive deletion of a filesystem or home root."),
    (re.compile(r"\bgit\s+reset\s+--hard\b", re.I),
     "Refusing git reset --hard because it can discard uncommitted work."),
    (re.compile(r"\bgit\s+clean\s+-[a-z]*f[a-z]*\b", re.I),
     "Refusing git clean with force because it can delete untracked work."),
    (re.compile(r"\bRemove-Item\b[^\r\n]*\b-Recurse\b[^\r\n]*\b-Force\b", re.I),
     "Refusing recursive forced deletion; use an exact, verified target."),
    (re.compile(r"\b(?:format|format-volume)\b", re.I),
     "Refusing a filesystem format command."),
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return 0

    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str):
        return 0

    for pattern, reason in BLOCKED:
        if pattern.search(command):
            response = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
            json.dump(response, sys.stdout, separators=(",", ":"))
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
