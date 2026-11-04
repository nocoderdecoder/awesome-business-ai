# Awesome Business AI

> A practical, openly reusable field guide for business professionals choosing, testing, and reviewing AI workflows.

Move from **“Which AI tool?”** to **“Which workflow, what evidence, and who approves the result?”** This project combines a curated resource directory with original workflow playbooks, pilot templates, and an offline evaluation example. Start with a small task your team can review.

Maintained by [Anshul Gupta](https://github.com/nocoderdecoder). Resource source review: **November 4, 2026**. [CC0 dedication](LICENSE).

## Start with a business task

| I need to… | Start here | A useful first test |
| --- | --- | --- |
| Triage support requests | [Support playbook](docs/playbooks/support-triage.md) | Catch a refund promise that policy does not authorize |
| Explain a budget variance | [Finance playbook](docs/playbooks/finance-variance.md) | Reconcile every number before drafting a narrative |
| Research an account | [Sales playbook](docs/playbooks/sales-research.md) | Separate cited facts from sales hypotheses |
| Answer internal questions | [Knowledge playbook](docs/playbooks/knowledge-qa.md) | Abstain when approved evidence is missing |
| Select a platform | [Resource guide](docs/resource-guide.md) | Ask the review question attached to each entry |
| Plan a pilot | [Pilot brief](templates/pilot-brief.md) | Define quality, cost and stop conditions before starting |

## What is included

- **30 resources** across business functions, risk management and learning, with official URLs, source-review dates and pilot review questions. [Machine-readable catalog](data/resources.json).
- **Four original playbooks** with copy-ready prompts, synthetic worked examples, acceptance checks and human approval steps.
- **Three reusable templates**: [pilot brief](templates/pilot-brief.md), [vendor review](templates/vendor-review.md), and [outcome log](templates/pilot-outcome-log.md).
- **A reproducible support-triage evaluation** with synthetic inputs, manually authored responses, deliberate failure cases and deterministic checks. [Run the example](examples/support-triage/README.md).

These are project artifacts, not adoption statistics. Source review confirms the public page and stated purpose; it does **not** establish product quality, privacy guarantees, current pricing, or fitness for a particular organization. Inclusion is not endorsement or a ranking. Read the [curation method](docs/methodology.md).

## A practical pilot sequence

1. Pick one repeatable, reviewable task. Record the current manual process and baseline time.
2. Use approved, minimized inputs; begin with synthetic data. Complete the [vendor review](templates/vendor-review.md) before connecting real systems.
3. Choose a playbook and define acceptance thresholds in the [pilot brief](templates/pilot-brief.md).
4. Test ordinary requests, missing evidence, conflicting instructions and escalation cases. Record failures as well as successes.
5. Compare quality, review effort and total cost with the baseline. Require accountable approval before expanding access or automating actions.

## Run the offline checks

Python 3.10 or newer is sufficient. No installation, account, API key, model download or network access is needed for these commands:

```bash
python3 scripts/render_catalog.py --check
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/evaluate.py
```

The example evaluates **manually authored fixtures**, not a live AI model. Passing it demonstrates only the stated rule checks on those fixtures. It does not establish model accuracy, production readiness, or business ROI. See [evaluation limitations](examples/support-triage/README.md).

## Contribute and reuse

Add a resource with a primary source and a concrete business use, improve a playbook with reproducible examples, or report a broken link. Start with [CONTRIBUTING.md](CONTRIBUTING.md). Do not submit private business data or promotional claims as evidence.

The [adoption and evidence guide](docs/adoption-and-evidence.md) explains how to record real use without confusing project output, interest and demonstrated outcomes. [CHANGELOG.md](CHANGELOG.md) records the substantive updates; [CITATION.cff](CITATION.cff) provides citation metadata.

Original project content is dedicated under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Linked third-party products, documents, trademarks and materials retain their own terms.
