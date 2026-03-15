#!/usr/bin/env python3
"""
macOS desktop notification hook for Claude Code.
Sends a notification via terminal-notifier when Claude needs your attention.

Install: brew install terminal-notifier
Config: Add to ~/.claude/settings.json under "hooks"

Usage in settings.json:
{
  "hooks": {
    "Notification": [{"matcher": "", "hooks": [{"type": "command", "command": "python3 ~/.claude/scripts/notify.py Notification"}]}],
    "Stop": [{"matcher": "", "hooks": [{"type": "command", "command": "python3 ~/.claude/scripts/notify.py Stop"}]}]
  }
}
"""

import subprocess
import sys

def notify(title: str, message: str = ""):
    try:
        subprocess.run([
            "terminal-notifier",
            "-title", title,
            "-message", message or "Claude Code needs your attention",
            "-sound", "default",
            "-group", "claude-code",
        ], check=True, capture_output=True)
    except FileNotFoundError:
        print("terminal-notifier not installed. Run: brew install terminal-notifier", file=sys.stderr)
    except subprocess.CalledProcessError:
        pass

if __name__ == "__main__":
    event = sys.argv[1] if len(sys.argv) > 1 else "Notification"
    notify(f"Claude Code — {event}")
