# Curation and verification method

## Audience and scope

This guide serves non-technical business professionals and the colleagues who review their AI pilots. Prefer a resource that connects to a named workflow and a testable review question. Some automation platforms require technical ownership; inclusion does not imply that deployment is suitable for an unassisted beginner.

## Selection rules

Include a resource when:

1. An official product, documentation, standards-body or course-provider page identifies the resource and its purpose.
2. A business user can identify a concrete task it supports, or a practical risk or learning need it addresses.
3. The entry adds a distinct workflow, ecosystem option or educational function.
4. The description avoids unsupported superlatives, usage statistics, compliance promises and numerical performance claims.
5. A reviewer can ask a specific pilot question before adoption.

Catalog order groups resources by purpose. It is not a league table. The directory is selective, not exhaustive, and does not sell placement or use affiliate URLs.

## Meaning of the review date

For the November 4, 2026 refresh and November 5, 2026 additions, official public pages were reviewed through web browsing. Review covered resource identity and stated purpose. Redirects were followed; current destination URLs were used where appropriate. Each entry records the URL, `source_checked_on` date and `verification_scope` in [resources.json](../data/resources.json).

This was a **public-source review**, not hands-on testing. No vendor account was opened, paid plan activated, trial started, API called, security assurance validated or comparative benchmark performed. Vendor assertions are not independent evidence. Prices, plan entitlements, geographic availability, integrations and product names can change. Recheck relevant documentation and contracts before a pilot.

Failed or inaccessible candidate URLs were not treated as verified. The current catalog omits candidates whose official pages could not be retrieved during the refresh. A retrieved page can still become stale; the offline validator does not check external reachability.

The November 5 additions use the same public-source verification boundary. Individual resources retain their original review dates; the catalog update date is not a claim that every product was retested.

The previous README included a broad “active in 2025” assertion and unsupported quantitative descriptions. This refresh replaces them with scoped, dated source review. The original directory remains in Git history; its previous claims were not independently validated in this refresh.

## Review record fields

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier used to track the entry |
| `name`, `url` | Resource name and its official primary-source URL |
| `category`, `kind` | Business function and resource type |
| `business_use` | Narrow workflow for which readers can evaluate the resource |
| `review_question` | A question to resolve during selection or testing |
| `source_checked_on` | ISO date of public-source retrieval |
| `verification_scope` | Explicit boundary of what was reviewed |

## From source review to a real pilot

Product claims alone cannot demonstrate suitability. Use the [vendor review](../templates/vendor-review.md) to record data handling, access, retention, costs and unresolved questions. Use a [pilot brief](../templates/pilot-brief.md) to agree on quality thresholds and a comparison baseline before selecting outputs to showcase.

Risk-management references include the [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), its [companion playbook](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook), and [OWASP's Gen AI risk guidance](https://genai.owasp.org/llm-top-10/). These inform questions to ask; this repository is not a certification or a complete implementation of those frameworks. NIST's current page notes that AI RMF 1.0 is under revision; verify the version used in your records.

## Maintenance

Before a substantive catalog update, retrieve the official source again, narrow unsupported descriptions and record the new date. Open a correction for a redirected, discontinued or unclear resource. Do not simply roll all dates forward.

After editing the JSON, regenerate the guide with `python3 scripts/render_catalog.py`, run its `--check` mode, then run the repository validator and tests. Human review remains necessary for whether a page supports a description and whether an entry is useful.
