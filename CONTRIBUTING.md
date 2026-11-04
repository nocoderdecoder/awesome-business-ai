# Contributing

Help a business professional make a better decision or run a more reviewable pilot. Useful contributions include corrected official links, narrowly described resources, worked examples, failure cases, improved prompts, more usable documents, and fixes to offline checks.

## Add or update a resource

1. Read the [curation method](docs/methodology.md).
2. Retrieve the official source and confirm that it supports the stated purpose. Claim hands-on testing only if performed and documented.
3. Edit [data/resources.json](data/resources.json). Include every existing field, a unique stable ID, an HTTPS official URL, a real ISO review date, and a specific pilot review question.
4. State verification limits. Avoid affiliate links, unsupported statistics, rankings and guarantees.
5. Regenerate the guide and run checks:

```bash
python3 scripts/render_catalog.py
python3 scripts/render_catalog.py --check
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/evaluate.py
```

## Improve a workflow

Use synthetic examples or material you have permission to publish. Include expected behavior, an unsafe or ambiguous case, an acceptance checklist, a human approval boundary and outcome measures. A prompt alone does not demonstrate that a workflow works.

Keep examples vendor-neutral where feasible. Distinguish manually authored examples from model-generated responses, and rule-based checks from human evaluation. Report limitations alongside results.

## Review process

Open a pull request explaining the user problem, primary sources reviewed, changes and checks run. Disclose vendor or affiliate relationships. A maintainer reviews relevance, evidence, usability and scope before acceptance. The process does not imply independent adoption or endorsement.

Do not include credentials, customer records, identifiable candidate information, private transcripts or confidential documents in issues, tests or pull requests.

By contributing original material, you agree to its [CC0 dedication](LICENSE). Third-party works retain their own terms; link to them rather than copying protected content wholesale.
