---
description: Verify workspace integrity — submodules, symlinks, hooks, settings, and key files
user_invocable: true
---

# Health Check

Run a comprehensive workspace integrity check. Verify everything is pointing in the right direction.

## Checklist

### 1. Submodules
```bash
git submodule status
```
All submodules should show a commit hash (not a `-` prefix, which means uninitialized).

### 2. Skill Symlinks
Verify all symlinks in `.claude/skills/` resolve to real targets:
```bash
for link in .claude/skills/*/; do
  if [ -L "${link%/}" ]; then
    target=$(readlink "${link%/}")
    if [ ! -e "${link%/}" ]; then
      echo "❌ BROKEN: ${link%/} -> $target"
    else
      echo "✅ OK: ${link%/}"
    fi
  fi
done
```

### 3. Hooks
Check that hook scripts exist and are executable:
```bash
ls -la ~/.claude/scripts/security-gate.py 2>/dev/null && echo "✅ security-gate.py" || echo "⚠️ security-gate.py not found"
ls -la ~/.claude/scripts/notify.py 2>/dev/null && echo "✅ notify.py" || echo "⚠️ notify.py not found"
```

### 4. Security Layer
Verify deny rules exist in project settings:
```bash
cat .claude/settings.json 2>/dev/null || echo "⚠️ No project-level settings.json"
```

### 5. Key Files
Verify core orientation files exist and aren't empty:
```bash
for f in CLAUDE.md user.md MASTER_TODO.md Logbooks/user-log.md Logbooks/claude-log.md easter-eggs.md README.md; do
  if [ -s "$f" ]; then
    echo "✅ $f ($(wc -l < "$f") lines)"
  else
    echo "❌ MISSING OR EMPTY: $f"
  fi
done
```

### 6. Rules Files
```bash
ls -la .claude/rules/*.md
```

### 7. Dependencies
```bash
which terminal-notifier 2>/dev/null && echo "✅ terminal-notifier" || echo "⚠️ terminal-notifier not installed (brew install terminal-notifier)"
which gitleaks 2>/dev/null && echo "✅ gitleaks" || echo "⚠️ gitleaks not installed"
npx ccusage@latest --version 2>/dev/null && echo "✅ ccusage" || echo "⚠️ ccusage not available"
```

### 8. .gitignore
Verify sensitive patterns are excluded:
```bash
cat .gitignore
```
Should include: `.env`, `.claude/settings.local.json`, `*.local`, `.DS_Store`, `node_modules/`

## Output Format

Present results as a summary table:

```
┌─────────────────────┬────────┬───────────────────────────┐
│ Component           │ Status │ Notes                     │
├─────────────────────┼────────┼───────────────────────────┤
│ Submodules          │ 🟢/🔴  │                           │
│ Symlinks            │ 🟢/🔴  │ X broken                  │
│ Hooks               │ 🟢/🔴  │                           │
│ Security deny rules │ 🟢/🔴  │ N rules                   │
│ Key files           │ 🟢/🔴  │                           │
│ Rules files         │ 🟢/🔴  │                           │
│ Dependencies        │ 🟢/🟡  │ missing: X                │
│ .gitignore          │ 🟢/🟡  │                           │
└─────────────────────┴────────┴───────────────────────────┘
```

Flag anything that needs attention with 🚩.
