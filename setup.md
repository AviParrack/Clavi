# First-Time Setup

*Claude reads this file on first launch. It walks you through personalizing the workspace interactively.*

---

## Claude: Read This

If the "Who You Are" section in `CLAUDE.md` still contains the placeholder text `[Give Claude background context on who you are and what you need.]`, this workspace hasn't been set up yet.

**Start a setup conversation with the user.** Be warm, be direct, keep it moving. The user can skip any step by saying "skip" — don't block on anything.

### Opening

Say something like:

> Hey! This workspace is a fresh clone of the Claude Code scaffold. I'll walk you through making it yours — should take about 5-10 minutes, and you can skip anything you want to come back to later. Ready?

If the user says no or asks to skip setup entirely, say "No problem — everything works out of the box. Just fill in CLAUDE.md whenever you're ready, it'll make our collaboration much better." Then stop.

### Step 1: Who You Are (→ CLAUDE.md)

Ask the user to tell you about themselves. Prompt with:

> **First, tell me about yourself.** This goes into CLAUDE.md — it's the context I read at the start of every session. The more I know, the better I can help. Some things that are useful:
>
> - What do you do? What are you working toward?
> - What's your background — what shaped how you think?
> - How do you like to work? (Intensity, hours, energy management)
> - What do you want from this collaboration specifically?
>
> Don't overthink it. Talk to me like you'd talk to a new collaborator on day one.

Take their response and write it into the "Who You Are" section of `CLAUDE.md`. Show them what you wrote and ask if it captures them well. Revise if needed.

### Step 2: Working Style (→ CLAUDE.md)

Ask:

> **How do you want us to work together?** The defaults in CLAUDE.md are a good starting point, but some things to consider:
>
> - Do you want me to be proactive — suggesting things, pushing back, flagging patterns?
> - Or more reactive — do what you ask, stay focused, minimal commentary?
> - How much bandwidth do you typically have? (Running 10 agents at once? Deep-focused single session?)
> - Anything that drives you crazy about AI assistants that I should avoid?

Update the "Working Together" section based on their answers. Keep the structural elements (🚩 flags, visual language table, scannable defaults) but customize the tone and expectations.

### Step 3: Principles (→ CLAUDE.md)

Ask:

> **What principles matter to you in your work?** The "How We Work" section is for the stuff beyond the task — your values, your standards, what you hold yourself to. The defaults include epistemic rigor, kindness, and continuous improvement. Keep what resonates, cut what doesn't, add what's missing.

Update accordingly.

### Step 4: Writing Voice (→ .claude/rules/writing-voice.md)

Ask:

> **Do you do any writing in this workspace?** (Blog posts, research papers, essays, documentation...)
>
> If so, I can set up a writing voice profile. I'll ask about your influences and style — it means my drafts will sound like *you* instead of generic AI.

If yes, walk them through the prompts already defined in `.claude/rules/writing-voice.md` (influences, key moves, tone range, which file paths it should apply to). Fill it in.

If no, say "No problem — the writing voice file is there whenever you need it."

### Step 5: Projects (→ Projects/, CLAUDE.md)

Ask:

> **What are you working on right now?** I'll set up project folders with handoff files so future sessions pick up where we leave off. Just name the projects — even rough descriptions are fine.

For each project they name:
1. Create `Projects/<project-name>/HANDOFF.md` with a basic template
2. Add a row to the Active Projects table in `CLAUDE.md`

### Step 6: Security & Hooks (optional)

Ask:

> **Want to set up the security layer and desktop notifications now?** This is optional — the workspace works without it — but it adds:
> - A hook that blocks dangerous Bash commands before they run
> - Desktop notifications when I need your attention
> - Secret scanning on every git commit
>
> It also unlocks `Bash(*)` auto-allow, so I can run commands without prompting you each time. Without it, I'll ask permission for every shell command.
>
> Takes about 2 minutes. Want me to walk you through it?

If yes, run through the commands from the Quick-Start section of `README.md` (steps 3-4). Walk them through installing terminal-notifier, copying the hook scripts, and setting up detect-secrets. Once security-gate.py is installed, offer to upgrade their permissions to Tier 2 (`Bash(*)` auto-allow).

**Important:** Do NOT add `Bash(*)` to their allow list unless security-gate.py is confirmed installed. If they skip this step, leave Bash on the default ask-each-time behavior. The deny list alone is not sufficient for blanket Bash auto-allow.

If no, move on — everything works fine without it, just with more permission prompts.

### Step 7: Wrap Up

Say something like:

> **You're set up.** Here's what we configured:
> - [list what was filled in]
>
> A few things to know:
> - I maintain `user.md` with notes back to you — check it occasionally
> - Each project has a `HANDOFF.md` I'll update so future sessions have context
> - The logbooks (`Logbooks/`) are where I'll keep session notes
> - Run `/health-check` anytime to verify everything's wired up
>
> What do you want to work on?

Then proceed normally. Setup is done.

---

## If Setup Was Partially Completed

If CLAUDE.md has some sections filled in but others still have placeholder text, don't re-run the full setup. Just note which sections are incomplete and offer to fill them in:

> I notice your "Writing Voice" hasn't been set up yet. Want to do that now, or save it for later?

Be lightweight about it. Don't nag.
