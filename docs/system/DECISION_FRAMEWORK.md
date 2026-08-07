# Technology & Architecture Decision Framework

## Weighted criteria
Suggested default weighting:
- Requirement fit 25%
- Simplicity 20%
- Maintainability 15%
- Ecosystem/maturity 10%
- Security 10%
- Operational burden 10%
- Cost 5%
- Developer productivity 5%

Adjust to project context.

## Rules
- Prefer boring mature technology when options are otherwise equal.
- Novelty is not a benefit by itself.
- Ask if a separate backend is actually needed.
- Prefer relational databases for strongly related business data unless requirements clearly favor another model.
- Large/private files usually belong in object storage.
- Prefer mature provider/framework auth.
- Prefer established payment providers; do not custom-handle card data casually.
- Start with one app + one primary DB + managed infrastructure.
- Escalate architecture only for concrete scaling, isolation, ownership or runtime needs.

## Build vs buy
Build core differentiation. Buy/use managed services for commodity infrastructure where mistakes are expensive or ownership cost is higher.

## ADR threshold
Create an ADR only for difficult-to-reverse, cross-cutting, security-sensitive, expensive or likely-to-be-questioned decisions.
