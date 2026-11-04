# Support triage: a runnable evaluation example

This is a small, offline demonstration of how to define acceptance criteria before selecting an AI tool. Every ticket and reply is synthetic and manually authored. No model was called and no customer data was used.

## Run it

From the repository root with Python 3.10 or newer:

```sh
python3 scripts/evaluate.py
python3 -m unittest discover -s tests -v
```

The first command deterministically rewrites [results.json](results.json) and [results.md](results.md). There are six cases: four acceptable replies and two deliberately unsafe examples. The unsafe examples verify that wrong routing, missing approval, missing required facts, and unsupported promises can be detected. The command normally exits successfully so the demonstration can be reproduced; use `--strict` to exit with status 1 when any candidate fails.

## What is being checked

- The route must exactly match the expected queue.
- The approval flag must be a Boolean and match the case requirement.
- Each required phrase must appear as a whole phrase in the reply, ignoring case.
- A reply must not contain any listed unsupported promise.
- Missing, duplicate, and unknown candidates are surfaced rather than silently skipped.

The synthetic policy follows the [support triage playbook](../../docs/playbooks/support-triage.md): allowed routes are `general`, `billing-review`, `technical-review`, and `security-escalation`. All outputs require human approval. Shipping questions use `general` and dates remain unconfirmed; refunds need `billing-review`; suspected account compromise uses `security-escalation`; undocumented integrations need `technical-review`. The two unsafe controls intentionally violate these rules. These are illustrative rules, not the policy of a real business.

## Adapt it to a real pilot

1. Replace the fictional cases with an approved, de-identified test set that represents routine and difficult tasks.
2. Have the workflow owner specify expected routes and approvals before seeing candidate outputs.
3. Generate candidates only through an independently approved tool and account; this repository contains no paid service integration.
4. Add human scoring for correctness, usefulness, tone, privacy, and refusal behavior. Include independent review of disagreements.
5. Run the same cases against the current workflow and proposed workflow. Record tool version, prompts, dates, reviewer decisions, full review time, and costs.
6. Keep failure cases and report the denominator, exclusions, and uncertainty. A passing example is not deployment approval.

## Limits

Literal phrase checks can miss paraphrased unsafe promises and can penalize safe negations. They cannot establish factual correctness, security, fairness, customer satisfaction, or model quality. The six examples are too small and too artificial for comparative performance claims. A 4/6 result here is a demonstration outcome, not an accuracy score or measured productivity gain.

See [the case definitions](cases.json), [candidate replies](candidates.json), and [evaluator](../../scripts/evaluate.py).
