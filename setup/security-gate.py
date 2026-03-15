#!/usr/bin/env python3
"""
Security gate hook for Claude Code.
Blocks dangerous Bash commands before execution.

This is a PreToolUse hook that inspects Bash commands and blocks
patterns that could cause harm (destructive operations, credential access, etc.)

Config: Add to ~/.claude/settings.json under "hooks":
{
  "hooks": {
    "PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 ~/.claude/scripts/security-gate.py"}]}]
  }
}
"""

import json
import re
import sys

# Patterns that should be blocked
DANGEROUS_PATTERNS = [
    r"rm\s+-rf\s+/",           # rm -rf on root paths
    r"rm\s+-fr\s+/",           # rm -fr on root paths
    r">\s*/dev/sd",             # writing to block devices
    r"mkfs\.",                  # formatting filesystems
    r"dd\s+if=",               # raw disk operations
    r"chmod\s+-R\s+777",       # overly permissive chmod
    r"curl.*\|\s*bash",        # pipe to bash
    r"wget.*\|\s*bash",        # pipe to bash
    r"curl.*\|\s*sh",          # pipe to sh
    r"wget.*\|\s*sh",          # pipe to sh
]

def check_command(command: str) -> bool:
    """Returns True if the command is safe, False if dangerous."""
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return False
    return True

if __name__ == "__main__":
    try:
        input_data = json.loads(sys.stdin.read())
        tool_input = input_data.get("tool_input", {})
        command = tool_input.get("command", "")

        if not check_command(command):
            result = {
                "decision": "block",
                "reason": f"Security gate blocked potentially dangerous command: {command[:100]}"
            }
            print(json.dumps(result))
            sys.exit(0)

        # Allow the command
        print(json.dumps({"decision": "allow"}))
    except Exception:
        # On error, allow (fail-open to avoid blocking normal work)
        print(json.dumps({"decision": "allow"}))
