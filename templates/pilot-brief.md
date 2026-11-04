# AI workflow pilot brief

Copy this template for one workflow. Replace every bracketed field. Approval authorizes only the scope recorded here; it does not authorize purchases or production deployment.

## Decision and ownership

| Field | Fill in |
| --- | --- |
| Pilot ID / version / date | [identifier; version; date] |
| Decision to inform | [continue, revise, or stop this workflow] |
| Workflow and output | [one task; where the output goes] |
| Business owner / reviewer / access owner | [names or roles] |
| Start / end / review date | [dates] |
| Allowed actions | [e.g., prepare a draft in a test folder] |
| Actions requiring separate approval | [e.g., send, publish, write to CRM, expand data access] |
| Tool and configuration | [product; model/version if exposed; settings; prompt version] |
| Budget and purchasing approval | [approved amount or zero; approver; existing entitlement checked] |

## Question and comparison

**Hypothesis:** [One falsifiable statement, such as lower total handling time without more unsupported claims.]

**Current process:** [Who does the task today; inputs; handoffs; existing review requirements.]

**Comparison design:** [Randomized control if practical, otherwise a matched baseline; assignment method; matching variables; limits.]

**Sample fixed before testing:** [Number of units; inclusion/exclusion criteria; difficulty categories; held-out examples; dates.]

**Avoid confounding:** [How task complexity, reviewer skill, learning effects, repeat exposure, and changing policies will be handled. Do not let the same reviewer remember the baseline answer without recording that limitation.]

## Data and output boundaries

- Approved input and source owner: [data types, document IDs, scope]
- Excluded input: [secrets, unnecessary identifiers, restricted sources]
- Authorization and minimization check: [who checks access before input]
- Storage, retention, and deletion: [locations and dates, including drafts]
- External actions: [disabled, or individually approved action and approver]
- Human approval step: [who checks what, before which action]

## Metrics and gates fixed before results

| Metric | Definition and denominator | Baseline collection | Proposed pass gate | Owner |
| --- | --- | --- | --- | --- |
| Output correctness | [correct units / all reviewed units; define correct] | [method] | [threshold] | [role] |
| Unsupported claims | [unsupported claims / checked claims; include zero-claim cases] | [method] | [threshold] | [role] |
| Total active time | [input preparation + draft + review + correction; minutes per unit] | [method] | [threshold] | [role] |
| Severe failures | [define disclosure, unauthorized action, or critical error] | [method] | [threshold] | [role] |
| Coverage / abstention | [completed, abstained, and rejected units / all assigned units] | [method] | [threshold] | [role] |

Count failed and excluded units; do not report only approved drafts. Record sample sizes, category results, median and range of time, and the reasons for exclusion. An inconclusive result is a valid outcome.

## Cost worksheet

Use observed costs, including review labor. Separate existing license allocation from incremental cash spending.

| Cost component | Baseline | Assisted | Evidence / assumption |
| --- | ---: | ---: | --- |
| Preparation + execution labor | [hours × stated hourly cost] | [hours × same convention] | [time log] |
| Review + correction labor | [hours × stated hourly cost] | [hours × same convention] | [time log] |
| Incremental tool or usage charge | [amount] | [amount] | [approved invoice or zero] |
| Setup / training / maintenance | [amount] | [amount] | [one-time vs recurring] |
| Total for the measured period | [sum] | [sum] | [currency; period] |

**Net measured cost difference:** baseline total minus assisted total. This is a cost comparison for the measured scope, not revenue, realized headcount savings, or annual ROI. Do not monetize saved time without explaining the hourly-cost assumption and whether that time was actually redeployed.

## Stop and decision rules

- Stop immediately for: [specific severe failures and escalation owner].
- Pause for revision when: [quality or time gate fails; minimum sample not reached].
- Resume only after: [fix; independent retest; named approval].
- Expand only when: [all gates met; limitations accepted; separate access/action approval].
- Final decision / approver / date: [continue, revise, stop, or inconclusive; reasoning].

Attach the [vendor review](vendor-review.md), relevant playbook, frozen test set, and [pilot outcome log](pilot-outcome-log.md). Preserve rejected outputs with sensitive values removed.
