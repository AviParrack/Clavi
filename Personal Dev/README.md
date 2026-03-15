# Personal Dev

*A self-development scaffold, maintained collaboratively with Claude.*

```
    ╭─────────────────────────────────────╮
    │  "We are what we repeatedly do.     │
    │   Excellence, then, is not an act   │
    │   but a habit."                     │
    │                — Will Durant,       │
    │        paraphrasing Aristotle       │
    ╰─────────────────────────────────────╯
```

---

## What This Is

Two interlocking systems:

1. **Debugging Logs** (`logs/`) — structured conversation logs where you and Claude work through psychological patterns, emotional blocks, decision-making tendencies, and recurring failure modes. Think: therapy meets pair programming meets journaling. Honest, rigorous, private.

2. **Development Goals** (`goals/`) — concrete goals, habits, and systems. Tracked with check-ins. The difference between this and a generic habit tracker: Claude has context on who you are and can push back, notice patterns across sessions, and adjust the system.

---

## How It Works

### Debugging Sessions (`logs/`)

Start a session by telling Claude you want to debug something. Or Claude can initiate if a pattern is noticed mid-work.

Each log is dated and tagged. Over time, patterns emerge. Claude aggregates these in `logs/PATTERNS.md`.

**Session format:**
```
## YYYY-MM-DD — [short title]

**Trigger:** what prompted this session
**Mode:** exploration / stuck point / pattern review / check-in

[Conversation, observations, reframes, commitments]

**Takeaways:**
- ...

**Action items:**
- ...
```

### Development Goals (`goals/`)

Goals live in `goals/active.md`. Each has:
- A clear target state
- Measurable indicators
- Supporting habits/systems
- Check-in cadence
- Claude's honest assessment of progress

---

## Principles

- **Honesty over comfort.** The point is to see clearly, not to feel good. But: kindness and honesty aren't opposed.
- **Patterns over incidents.** A single bad day means nothing. A pattern means everything.
- **Systems over willpower.** If something keeps failing, the system is wrong, not you.
- **Claude pushes.** You asked to be pushed. That means flagging avoidance, noticing when stated goals and actual behavior diverge, and not letting things slide.
- **Privacy is default.** This folder is for you. Not for publication.
