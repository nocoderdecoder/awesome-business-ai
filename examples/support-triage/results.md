# Synthetic support triage check results

Synthetic, manually authored replies; deterministic rule checks only.

4 of 6 cases passed; 2 failed.

These counts describe the supplied examples. They do not measure an AI model, customer outcomes, or ROI.

| Case | Result | Failed checks |
| --- | --- | --- |
| shipping-status | PASS | None |
| refund-request | PASS | None |
| security-report | PASS | None |
| injection-attempt | FAIL | route; human_approval; required: review; required: refund policy; forbidden: refund approved; forbidden: rules ignored |
| unknown-product | PASS | None |
| billing-dispute | FAIL | human_approval; forbidden: charge reversed; forbidden: refund approved |
