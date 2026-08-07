# Next Session

Status: Not initialized.

This file is the single human-friendly answer to:

> **What should I do next?**

At the end of every meaningful coding session, the AI agent must replace this file with a compact handoff containing:

```text
Project status:
Current phase:
Phase status: IN PROGRESS / COMPLETE / PROJECT COMPLETE
What was completed:
What remains:
Recommended next action:

COPY-PASTE PROMPT FOR THE NEXT SESSION
--------------------------------------
<ready-to-paste prompt>
```

Rules:

- If the current phase is incomplete, the prompt continues the same phase.
- If the current phase is complete, the prompt starts the next roadmap phase.
- If the project is complete, the prompt should propose the final release/audit flow or explain how to start a new change request.
- The prompt must be self-sufficient but token-efficient: reference canonical project files instead of retelling the whole project.
- Do not include secrets, tokens or credentials.
