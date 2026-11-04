# Pilot outcome log

Copy this record for one pilot. Fields below are placeholders; no measured results are supplied. Keep personal or customer data out of a public log. Store private evidence in an approved location and reference it with sanitized IDs.

## Run record

| Field | Fill in |
| --- | --- |
| Pilot ID / run ID / date | [fill in] |
| Brief version / prompt version / source snapshot | [fill in] |
| Tool / plan / model version when exposed / settings | [fill in] |
| Assigned units / included units / excluded units | [counts and reasons] |
| Baseline or assisted arm / assignment method | [fill in] |
| Reviewer / approval owner | [roles or approved identifiers] |
| Data handling or access exceptions | [none, or incident reference] |

## Per-unit record

Duplicate rows as needed. Record every assigned unit, including failures and abstentions. Time is active human time in minutes; avoid counting unattended elapsed time as labor. Use `N/A` with a reason for an unmeasured field, never zero.

| Unit ID | Category / difficulty | Arm | Prep min | Execution min | Review min | Correction min | Correct? | Supported claims / checked claims | Abstained? | Severe failure? | Approved? | Evidence ID |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- |
| [ID] | [category] | [baseline/assisted] | [min] | [min] | [min] | [min] | [yes/no/N/A] | [counts] | [yes/no] | [type/none] | [yes/no] | [sanitized reference] |

**Unit notes:** [Reasons for abstention, rejection, exclusion, missing observations, or correction. Record whether a repeated task exposed a reviewer to the prior answer.]

## Aggregate results

| Measure | Baseline | Assisted | Denominator / method / limitation |
| --- | --- | --- | --- |
| Assigned / reviewed / approved units | [counts] | [counts] | [include all failures] |
| Correct units / reviewed units | [counts; rate] | [counts; rate] | [who labeled correctness] |
| Supported claims / checked claims | [counts; rate] | [counts; rate] | [treat no-claim outputs separately] |
| Correct abstentions / must-abstain units | [counts; rate] | [counts; rate] | [fixed expected labels] |
| Severe failures | [count; types] | [count; types] | [incident references] |
| Median total active min / unit | [value] | [value] | [prep + execution + review + correction] |
| Range of total active min / unit | [min–max] | [min–max] | [sample size and categories] |
| Measured total cost for pilot scope | [currency; amount] | [currency; amount] | [cost worksheet in brief] |

**Results by difficulty/category:** [Repeat relevant rows by category; explain whether the comparison arms were balanced.]

**Time difference:** baseline median minus assisted median = [minutes per unit]. A difference between two medians is descriptive; it is not proof of causation or a confidence interval.

**Cost difference:** baseline measured total minus assisted measured total = [currency and amount]. State one-time setup costs, recurring costs, and labor-cost assumptions separately. Do not annualize an unrepresentative sample.

## Gate review and decision

- Gates fixed in the brief: [IDs and thresholds]
- Observed pass/fail/inconclusive for each gate: [evidence]
- Stop rule triggered: [no, or incident and action]
- Missing data and limitations: [sample size; selection; reviewer effects; version changes]
- Decision: [continue / revise / stop / inconclusive]
- Decision owner / date: [fill in]
- Follow-up owner / action / due date: [fill in]
- Approved public statement, if any: [bounded factual wording; no private details]

Keep the frozen test inputs, outputs, reviewer labels, rejected cases, and calculation sheet with the run record. Only describe adoption, savings, or business outcomes when actual evidence supports that exact scope. Return to the [pilot brief](pilot-brief.md) before changing the workflow or expanding the pilot.
