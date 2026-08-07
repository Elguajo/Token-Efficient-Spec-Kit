# Security Policy

Token-Efficient Spec Kit is an AI engineering workflow/template. Security issues can therefore exist both in repository files and in instructions that could cause unsafe agent behavior.

---

## What counts as a security issue

Examples:

- instructions that expose or commit credentials/secrets;
- prompts that encourage bypassing authentication/authorization controls;
- unsafe destructive update behavior;
- workflow changes that can overwrite project-owned state without approval;
- instructions that weaken tests/security to make checks pass;
- malicious or unsafe installation/update guidance;
- supply-chain behavior that silently installs untrusted tooling;
- prompt instructions that cause private project data to be sent to an unintended external service;
- unsafe defaults for auth, payments, private files or permissions.

---

## Reporting

Please avoid publishing sensitive exploit details or real credentials in a public issue.

For non-sensitive bugs and workflow inconsistencies, use a normal GitHub issue.

For a security-sensitive report, contact the repository owner privately through an appropriate GitHub/private contact channel when available.

Do not include:

- passwords;
- API keys;
- access tokens;
- private customer data;
- production secrets;
- confidential source code that you are not authorized to disclose.

---

## Supported versions

Until stable `1.0.0`, security fixes are expected to target the latest available Token-Efficient Spec Kit version.

Check the installed version in:

```text
VERSION
```

and framework changes in:

```text
CHANGELOG.md
```

---

## Security principles of the workflow

The framework expects agents to follow these defaults:

```text
server-authoritative privileged state
least privilege
input validation
no client-side secrets
negative tests for sensitive flows
idempotency where retries matter
current primary documentation for security-sensitive APIs
explicit approval for destructive/high-impact actions
```

For auth, payments, private files, permissions, webhooks, destructive migrations or sensitive data, normal happy-path implementation is not sufficient evidence of completion.

---

## Tooling and supply chain

External tools such as Superpowers, gstack, Context7 or optional GitHub Spec Kit change independently from this repository.

Before installation/update, agents should:

1. verify the current official upstream source;
2. prefer native/supported installation paths;
3. avoid committing credentials;
4. avoid silently installing optional tooling without a documented need;
5. report global runtime/package changes that require user approval.

---

## Safe workflow updates

Framework updates must follow:

```text
docs/system/WORKFLOW_UPDATE_POLICY.md
```

Project-owned files must not be blindly replaced by template defaults.

If an update requires destructive or ambiguous migration of project-owned state, it must stop for explicit approval.
