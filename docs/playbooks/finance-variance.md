# Finance variance narrative with independent arithmetic

**Workflow:** Turn an approved budget-versus-actual table into a first draft of a monthly operating review. The workbook or accounting system remains the numerical source of truth. A finance reviewer approves all interpretations and distribution.

**Owner:** FP&A or finance operations. **Approver:** The finance lead responsible for the reporting period. This workflow prepares internal commentary; it does not make investment, tax, or accounting-policy decisions.

## Approved input

Start with a synthetic, aggregated table. For an authorized pilot, supply the period, currency, units, reporting scope, metric type, approved figures, and a short source reference for each row. Exclude personal payroll records, customer identifiers, bank credentials, and unnecessary transaction details. Define the sign convention before prompting.

Use `variance = actual − budget` and `variance percent = (actual − budget) / budget × 100` for a positive nonzero budget. A positive revenue variance is favorable; a positive expense variance is unfavorable. Zero, negative, missing, or incomparable budgets need an explicit exception rule approved by finance; do not silently divide or infer a meaningful percentage.

## Copy-ready prompt

```text
Prepare a DRAFT monthly variance narrative from the supplied table only.
Do not alter the source data. Do not infer causes from numerical differences.
Use variance = actual - budget. For a positive nonzero budget, calculate
variance percent = variance / budget * 100. Show the inputs and arithmetic.
For a zero, negative, missing, or incomparable budget, write N/A for percent
and explain that finance review is required.

For each row return: source ID; budget; actual; absolute variance; percent
variance; favorable/unfavorable based on its supplied metric type; one factual
sentence; and an unanswered question for the finance owner.
Keep observed differences separate from causes provided by the owner.
If a cause is not supported by a supplied source, write CAUSE NOT ESTABLISHED.
If units, scope, or period conflict, stop and list the mismatch.
Finish with DRAFT — FINANCE APPROVAL REQUIRED and a reconciliation checklist.

PERIOD / CURRENCY / UNITS / SCOPE: [fill in]
TABLE WITH SOURCE IDS AND METRIC TYPES: [paste approved data]
OPTIONAL VERIFIED CAUSE NOTES WITH SOURCE IDS: [paste or leave blank]
```

## Synthetic worked example

Period: October 2026. Currency: USD. Units: dollars. Scope: demo business only.

| Source ID | Metric | Type | Budget | Actual | Actual − budget | Percent variance | Interpretation |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| DEMO-F01 | Revenue | Revenue | 100,000 | 108,000 | +8,000 | +8.0% | Favorable |
| DEMO-F02 | Software | Expense | 20,000 | 23,000 | +3,000 | +15.0% | Unfavorable |
| DEMO-F03 | New program | Expense | 0 | 2,000 | +2,000 | N/A | Unbudgeted expense; review |

**Acceptable narrative:** “Revenue was $8,000 above budget, an 8.0% favorable variance (DEMO-F01: $108,000 − $100,000; $8,000 ÷ $100,000). Software expense was $3,000 above budget, a 15.0% unfavorable variance (DEMO-F02). The new program incurred $2,000 against a zero budget; a percentage variance is not defined (DEMO-F03). Causes are not established by the supplied data.”

**Independent reviewer check:** Recalculate all three differences in the source workbook or calculator; confirm the two percentages and the zero-budget exception. A fluent narrative is not evidence that the arithmetic is right. Ask the owners whether timing, volume, pricing, or classification explains the differences; do not choose a cause without support.

## Failure cases to test

| Input variation | Required behavior |
| --- | --- |
| An expense overspend is called favorable | Reject and correct the interpretation. |
| Budget is zero or negative | Show N/A percent and require an approved exception rule. |
| Dollars and thousands are mixed | Stop until units are reconciled. |
| Actuals and budget cover different months | Stop; do not compare them. |
| Notes say “probably due to marketing” | Mark cause unconfirmed unless an owner validates it. |
| A total does not reconcile to its rows | Flag the discrepancy; do not repair silently. |

## Acceptance checklist

- [ ] Every number ties to a supplied source ID with matching period and units.
- [ ] Differences, denominators, rounding, and totals were independently checked.
- [ ] Favorability matches the metric type and the approved convention.
- [ ] Causes are supported or explicitly unknown.
- [ ] Finance approved the narrative before it entered a report.

## Pilot measurement and stop rules

Measure arithmetic errors per checked row, unsupported causal statements per narrative, source reconciliation failures, reviewer correction time, and total preparation-plus-review time. Use the same report scope for the existing and assisted process. Report medians and sample size; do not extrapolate a few rows to annual savings.

**Proposed starting gate:** zero numerical errors and zero unsupported causal assertions in the approved output across at least three reporting packs. Any data exposure or uncorrected reconciliation failure stops the pilot. These are proposed gates, not measured results. Preserve rejected drafts and correction time in the [outcome log](../../templates/pilot-outcome-log.md).
