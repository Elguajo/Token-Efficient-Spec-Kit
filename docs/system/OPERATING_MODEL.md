# AI Engineering Operating Model

## 1. Intake
Extract outcome, users, core jobs, platforms, constraints, integrations, data sensitivity, payments/commercial needs and design expectations. Unknown fields are not automatically questions.

## 2. Project classification
Choose one or more: static/content site, web app, ecommerce, marketplace, API/service, automation, CLI, desktop, mobile, browser extension, creative plugin, data pipeline, AI app, internal tool, library/SDK, infrastructure/tooling, other.

## 3. Complexity router

### Tier S — Small
Examples: landing page, small CLI, static portfolio, isolated feature, small automation.
Workflow: brief -> short plan -> tasks -> implement -> verify.
Do not create a heavy roadmap.

### Tier M — Medium
Examples: authenticated SaaS MVP, ecommerce MVP, plugin+backend, internal dashboard, mobile MVP.
Workflow: brief -> architecture -> roadmap -> phase specs -> implement batches -> converge.

### Tier L — Large
Examples: marketplace, multi-role SaaS, sensitive data, complex sync, many integrations, enterprise multi-tenant app.
Workflow: brief -> architecture -> risk model -> roadmap -> smaller independent specs -> selective quality gates -> implementation batches -> converge.

## 4. Risk level
Evaluate Low / Medium / High independently from size. High-risk triggers: payments, financial/private/health data, complex permissions, irreversible deletion, production infrastructure, critical data migrations, public contracts, compliance.

## 5. Research trigger
Use current official sources before committing when framework/API freshness, payment/auth/security APIs, deployment limits, pricing, licensing, niche libraries or uncertain signatures matter. Save conclusions, not research dumps.

## 6. Decision behavior
Normally choose one recommended approach. Explain rejected alternatives only for consequential tradeoffs.

## 7. Phase design
A phase should produce a verifiable outcome. Prefer vertical slices over arbitrary frontend/backend/database layers when possible.

## 8. Implementation batch
Default 1–3 cohesive tasks per run. Split a huge phase before increasing context.

## 9. Convergence
Compare code vs spec vs acceptance criteria vs tests. Gaps become small follow-up tasks.
