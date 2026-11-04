# Vendor and workflow review

Complete this for a specific product, plan, configuration, region, and use case. A vendor's general marketing statement may not apply to the plan you intend to use. This record supports an internal decision; it is not a certification or a legal conclusion.

**Status options:** Verified for this scope / Unknown / Not applicable with reason / Unacceptable for this pilot.

| Scope field | Fill in |
| --- | --- |
| Review ID / date / reviewer | [fill in] |
| Vendor / product / exact plan | [fill in; no purchase implied] |
| Intended workflow and users | [fill in] |
| Region / configuration / integrations | [fill in] |
| Data classification and excluded data | [fill in] |
| Existing access or proposed acquisition | [fill in; spending needs explicit approval] |

## Evidence ledger

For each item, record the exact source title and URL or approved document ID, date accessed, relevant excerpt or section, applicable plan/region, finding, and unresolved question. Use “Unknown” when evidence is missing. Do not infer a certification, contractual protection, or compliance status from a logo.

| Review item | Status | Evidence and applicable scope | Owner / open question |
| --- | --- | --- | --- |
| Data use for training and available controls | [status] | [source; date; section; plan] | [fill in] |
| Retention, deletion, and backups | [status] | [fill in] | [fill in] |
| Data location and cross-region processing | [status] | [fill in] | [fill in] |
| Subprocessors and connected-service sharing | [status] | [fill in] | [fill in] |
| Access roles, SSO, and account removal | [status] | [fill in] | [fill in] |
| Audit logs and administrator visibility | [status] | [fill in] | [fill in] |
| Integration permissions and write access | [status] | [fill in] | [fill in] |
| Human approval and action reversal | [status] | [fill in] | [fill in] |
| Output export, portability, and lock-in | [status] | [fill in] | [fill in] |
| Limits, quotas, usage charges, and overages | [status] | [fill in] | [fill in] |
| Incident reporting and support channel | [status] | [fill in] | [fill in] |
| Claims requiring procurement or legal review | [status] | [exact claim; evidence; unresolved scope] | [fill in] |

## Workflow checks

- Inputs minimized and approved by: [role; date; evidence]
- Access boundaries tested with: [synthetic cases; expected and observed result]
- Incorrect or unsupported outputs tested with: [cases; rejection behavior]
- Untrusted source instructions tested with: [cases; observed behavior]
- External actions disabled or separately approved: [configuration and evidence]
- Deletion/export tested using non-sensitive sample data: [result or reason skipped]
- Account owner and offboarding process: [role and procedure]

## Decision

**Decision:** [Approved for a bounded pilot / Needs evidence / Rejected].

**Approved scope:** [data, users, time period, exact configuration, and permitted actions].

**Restrictions and unresolved risks:** [list; owner; due date].

**Decision owner / date / next review trigger:** [fill in; include plan, policy, model, integration, or data-scope changes].

Unknown critical data handling or access controls should keep sensitive data out of the pilot until the responsible owner resolves them. Use synthetic data while evaluating functionality. Return to the [pilot brief](pilot-brief.md) to record the approved scope and budget.
