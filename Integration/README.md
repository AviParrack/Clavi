# Integration Layer

*Making Claude Code a living part of daily life, not just a project workspace.*

```
     ┌─────────────────────────────────────────────────────────┐
     │                    YOUR DAILY LIFE                      │
     │                                                         │
     │  Calendar ──┐                              ┌── Slack    │
     │  G-Docs  ───┤                              ├── Notion   │
     │  Gmail   ───┤    ┌──────────────────┐      ├── Twitter  │
     │  Todoist ───┼────│   Claude Code    │──────┤            │
     │  Apple   ───┤    │   + MCP servers  │      ├── Typefully│
     │  Obsidian ──┤    └──────────────────┘      ├── Forum    │
     │  Files   ───┘          │    │              └── Substack │
     │                   ┌────┘    └────┐                      │
     │              Skills/         Hooks/                      │
     │              Commands        Notifications               │
     └─────────────────────────────────────────────────────────┘
```

---

## First-Party MCP Connectors

Available at [claude.ai/settings/connectors](https://claude.ai/settings/connectors), auto-sync to Claude Code:

**GitHub, Slack, Notion, Sentry, Jira, Figma, Gmail, Google Calendar, Linear**

These are OAuth-integrated, maintained by Anthropic. Check what's already enabled there first.

---

## Key MCP Servers

| Need | Best Option | Notes |
|---|---|---|
| **Google Calendar** | First-party connector | Easiest. Read/write events, find free time |
| **Google Docs** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | Calendar + Docs + Gmail in one |
| **Apple Calendar + Reminders** | [supermemoryai/apple-mcp](https://github.com/supermemoryai/apple-mcp) | Native macOS. Also Contacts, Notes, Messages, Mail |
| **Todoist** | [Official Todoist MCP](https://www.pulsemcp.com/servers/todoist) | First-party from Todoist |
| **Obsidian** | [iansinnott/obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp) | Built specifically for Claude Code |

### Registries
- [Official MCP Registry](https://registry.modelcontextprotocol.io/)
- [mcp.so](https://mcp.so/) — community marketplace
- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) — curated list
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Claude Code-specific

---

## Hooks

Claude Code has 18 hook events. The most useful:

| Hook | What to use it for |
|---|---|
| `Notification` | macOS desktop alerts when Claude needs input |
| `Stop` | Notification when a background agent finishes |
| `PreToolUse` | Block dangerous commands, protect sensitive files |
| `PostToolUse` | Auto-format after file edits |

Hook types: `command` (shell), `http` (POST to URL), `prompt` (single-turn Haiku eval), `agent` (multi-turn subagent).

---

## Scheduled Tasks

| Approach | Persistence | Best For |
|---|---|---|
| **`/loop 5m <task>`** | Dies when you close terminal | Polling, in-session reminders |
| **Claude Code Desktop** | Survives restarts (app must be open) | Daily briefings, check-ins |
| **GitHub Actions** | Fully unattended | True cron: tweet queues, monitoring |

---

## Setup Recipes

### Desktop Notifications (2 min)
```bash
brew install terminal-notifier
mkdir -p ~/.claude/scripts
cp setup/notify.py ~/.claude/scripts/
# Then merge hooks from setup/global-settings-template.json into ~/.claude/settings.json
```

### Apple Native (5 min)
```bash
claude mcp add apple-mcp -- npx -y @supermemory/apple-mcp
# Grants access to Calendar, Reminders, Notes, Contacts, Messages, Mail
```

### Secret Scanning (2 min)
```bash
pip3 install detect-secrets
cp setup/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
