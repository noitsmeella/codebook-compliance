# Verification guide: checking direction and code without an advisor

Principle: check direction against the reference paper and pre-registered decisions; check code against small examples whose answers you know.

## A. Is the direction right?

### A1. Stay close to the reference paper
- Follow the test procedures of Halterman & Keith (2026).
- Record every deviation in the "Differences" section of `notes/tests_spec.md`. No unrecorded deviations.
- Check the paper and the authors' pages for released code or prompts; if they exist, compare them with your implementation.

### A2. Write things down before running
- Create thresholds, metrics, and empty table and figure shells first.
- For each RQ, write two or three lines in Research Journal: "if the result looks like this, I will read it as that".
- Do not change thresholds after running. If you must, record the reason and the date.

### A3. Run small first
- In W2, push 5–10 probes through the whole pipeline: collection → prompt → run → parse → metrics.
- Check at this stage: does the output come back as one of the five labels; do the A/B/C prompts differ only in the codebook block; can a run be reproduced from the log alone?

### A4. Get outside feedback
- Who: a course TA, a graduate student in your department, the authors of the reference paper, a student session at a relevant conference.
- What to send: a one-page summary and two specific questions. Examples: "Is the probe design convincing?", "Is the single-coder limitation acceptable for this format?"
- Record the feedback and your planned response in Research Journal.

### A5. Review yourself
- At the end of each phase, write three ways a reviewer would attack the work, and prepare an answer or a limitation statement for each.

## B. Is the code right?

### B1. Hand-computed example
Compute these values on paper first, then compare with the code.

| id | gold | pred_A | pred_C |
|---|---|---|---|
| 1 | SUPPORT | SUPPORT | SUPPORT |
| 2 | SUPPORT | SUPPORT | ENGAGE |
| 3 | OPPOSE | OPPOSE | OPPOSE |
| 4 | OPPOSE | ENGAGE | OPPOSE |
| 5 | ENGAGE | SUPPORT | ENGAGE |
| 6 | ENGAGE | OPPOSE | ENGAGE |
| 7 | ENGAGE | ENGAGE | ENGAGE |
| 8 | MENTION | MENTION | MENTION |
| 9 | MENTION | MENTION | MENTION |
| 10 | UNCLEAR | MENTION | UNCLEAR |

Compute by hand: accuracy per condition, per-class precision, recall and F1, macro-F1, and the A-vs-C flip rate.
The answers are deliberately not given here. Put your own values into `tests/` as expected values.

### B2. Compare with libraries
- Your own F1 must match scikit-learn to several decimal places.
- Use libraries for kappa and alpha, but feed them a worked example from a textbook or paper and check you get the same value.

### B3. Extreme inputs
| Input | Expected result |
|---|---|
| All predictions correct | Accuracy and F1 = 1.0 |
| All predictions wrong | Accuracy = 0 |
| Same predictions for two conditions | Flip rate = 0 |
| Identical predictions across all five orders | Unchanged share = 1.0 |
| Output "Support.", "support", empty string | As fixed in `tests_spec.md` (the guide: INVALID unless an exact match) |

### B4. Reproducibility
- Run twice with the same seed and compare the output files.
- Sampling, splitting and bootstrap all take the seed as an argument and log it.

### B5. Read the raw data
At each stage, sample 20 rows at random and read them yourself.

| Stage | What to look for |
|---|---|
| Collection | Year range, duplicate filings, empty descriptions |
| Sentence splitting | No cuts at the period in "H.R. 1234"; how semicolon lists were split |
| Bill-number extraction | Variants such as H.R., S., H.Res., S.J.Res.; missed numbers |
| Boundary patterns | Does each matched sentence actually fall under its rule? |
| LLM output | Does the parsed label match the raw output? |

### B6. Invariant checks
Add short code checks at the end of each stage.
- Row counts: can every change in row count between stages be explained?
- Overlap: do the random sample, boundary cases, probes and codebook examples overlap?
- Split: is any sentence in both dev and test? Is the ratio close to 40/60?
- Prompts: apart from the codebook block, are the A/B/C prompts identical character for character?

### B7. Use Tests I–III as checks
- If the valid-label share in Test I is low, look at the end of the prompt and the parsing code before blaming the model.
- If Tests II or III are low, first check that the codebook text and examples actually made it into the prompt.

## C. Using AI as a reviewer only

- Give it code you wrote and ask: "Find bugs and wrong assumptions. Do not write corrected code."
- Verify each point it raises with the examples in B1–B3. AI feedback can be wrong too.
- For design, ask only: "How would a reviewer attack this?"
- Do not use it for probes, the codebook, gold labels or error coding.
- Each time you use it, add one line to Research Journal: date, purpose, whether you adopted the suggestion.

## D. Checklist by phase

### Phase 0
- [ ] Every threshold in `tests_spec.md` is filled in
- [ ] The full pipeline ran once on 5–10 probes
- [ ] Pattern hits counted and a keep-or-change decision recorded
- [ ] 20 rows each read from collection and sentence splitting

### Phase 1
- [ ] Confirmed that prompts differ across conditions only in the codebook block
- [ ] Flip rate and accuracy checked against the B1 example
- [ ] Rerun with the same seed gave the same results
- [ ] Test IV expectations written before running

### Phase 2
- [ ] Prediction columns hidden while labeling
- [ ] Split grouped by sentence, with no overlap
- [ ] Test-split errors not inspected
- [ ] Every codebook revision has dev evidence in `revisions.md`

### Phase 3
- [ ] First labels not seen while re-labeling
- [ ] Own F1 matches scikit-learn
- [ ] Test split evaluated exactly once
- [ ] A fresh clone regenerates every table and figure
