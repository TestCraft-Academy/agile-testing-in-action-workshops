# Agile Testing in Action — Workshop Demos

> **One green acceptance check. Two costly defects. One release decision.**  
> A free, ten-minute introduction to testing *with* an Agile team, not just after it.

Imagine you are testing a promotion at **SwiftCart**. The story says shoppers should get a discount when they enter a valid code. The happy path passes. Would you release it?

This small repository accompanies a short video walkthrough. It contains three repeatable demonstrations that show how a conversation about rules and risk can find what a green check misses. It is a **fictional, intentionally flawed teaching model**, not a real checkout service or a full training course.

## Start here

You need **Python 3.10+**; no packages, API keys, server, account, or internet connection are needed to run the demos. From the repository root:

```bash
python3 demos/01_green_is_not_enough.py
python3 demos/02_retry_changes_the_risk.py
python3 demos/03_release_conversation.py
```

On Windows, use `py -3` instead of `python3`. If you do not want to run code, read each script and its printed output in the video; the concepts do not require programming experience.

| Demo | What you will see | Agile testing move |
|---|---|---|
| [01 — Green is not enough](demos/01_green_is_not_enough.py) | An acceptance check passes, but a gift-card basket gets a discount it should not receive | Ask for concrete examples during refinement |
| [02 — Retry changes the risk](demos/02_retry_changes_the_risk.py) | The same request applies a discount twice | Explore realistic failure paths, not only the happy path |
| [03 — Release conversation](demos/03_release_conversation.py) | A passing happy path alongside two business-critical risks | Explain evidence, impact, and conditions to the whole team |

All runs are deterministic and reset their own in-memory state. They do not call a real API or spend money.

## What you gain for free

- A concrete example of **shift-left thinking**: clarify eligibility before building more tests.
- A way to prioritise **risk-based checks**: gift-card eligibility and retries matter more than adding another happy-path assertion.
- A model for communicating a **release recommendation** without pretending QA alone owns the decision.
- Three runnable demos you can replay or discuss with your team.

> **Want to practise rather than just watch?** The separate, free **[Agile Testing in Action Mini Lab](https://github.com/TestCraft-Academy/agile-testing-in-action-lab)** is a 30–45 minute exercise with a sprint brief, three missions, a reusable quality canvas, and sample answers. This repository is the short video companion; the lab is the hands-on follow-up. **Before sharing the video, confirm the lab link is publicly accessible** (it currently returns 404).

## Go further with TestCraft Academy

The [**Agile Testing in Action** course](https://www.testcraftacademy.com/service-page/agile-testing-in-action-course) goes deeper into shift-left testing, Agile collaboration, sustainable automation, CI/CD, risk-based testing, and AI-augmented testing. It is distinct from these free demos and the free mini lab.

[**Register your interest for course details and upcoming dates →**](https://www.testcraftacademy.com/take-a-course-form)

## For video hosts

Use the [10-minute walkthrough guide](VIDEO_GUIDE.md) to plan a human-recorded video. It gives timings, commands, and the transition from this repository to the free lab and course. No video is hosted or generated here.

## Verify the demos

```bash
python3 -m unittest discover -s tests -v
```

Tests confirm the **documented observations of the intentionally broken model**; a passing suite does **not** mean the promotion behaviour is safe to ship.

## Licence

The code and documentation are available under the [MIT Licence](LICENSE). Contributions and corrections are welcome via a GitHub issue or pull request.
