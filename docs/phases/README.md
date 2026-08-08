# Phases

Project-owned. A framework update must never overwrite anything in this directory.

## Naming

```text
docs/phases/NN-kebab-name.md
```

- `NN` is zero-padded and starts at `00`;
- the name is lowercase and hyphen-separated;
- the file name must match the entry in `docs/project/ROADMAP.md`.

Examples:

```text
docs/phases/00-foundation.md
docs/phases/01-authentication.md
docs/phases/02-asset-library.md
```

## Which phase is current

Not decided here. `docs/project/ROADMAP.md` carries the `[>]` marker and is the
single source of truth. Never scan this directory to guess.

## Creating a phase

Copy `templates/PHASE.template.md` and keep only the sections that carry
information for this phase.
