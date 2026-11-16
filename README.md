# Codebook Compliance in LLM Classification of Lobbying Positions

**Question.** Given label names only versus a full codebook, does an LLM that classifies lobbying positions follow the codebook's boundary rules, or the everyday meaning of words like *support* and *oppose*?

The task: classify an interest group's position on a bill, from one sentence of a U.S. Lobbying Disclosure Act (LDA) report, as `SUPPORT`, `OPPOSE`, `ENGAGE`, `MENTION` or `UNCLEAR`.

The design follows the codebook framework and behavioral tests of Halterman & Keith (2026), *Political Analysis* 34, 188–204 ([doi:10.1017/pan.2025.10017](https://doi.org/10.1017/pan.2025.10017)).

## Research questions

| | Question | Measured by |
|---|---|---|
| RQ1 | How much do predictions on boundary cases change across prompt conditions? | Flip rates and F1 across conditions A, B, C |
| RQ2 | Does the LLM actually apply the codebook's exclusion rules? | Test V |
| RQ3 | Does it follow the definitions when label names and definitions are swapped? | Test VII |
| RQ4 | On boundary cases, which is closer to the codebook: a rule-based classifier (M0) or the LLM? | Accuracy by boundary rule |

## Why boundary cases

| Phrase | Going by the word alone | Codebook rule |
|---|---|---|
| supported the goals of | SUPPORT | ENGAGE |
| supported with amendments | SUPPORT | ENGAGE |
| expressed concerns | OPPOSE | ENGAGE |
| opposed Title III | OPPOSE | ENGAGE |
| opposed unless amended | ambiguous | OPPOSE |

These are the points where the everyday meaning of a word and the codebook rule disagree, so codebook compliance can be measured directly.

## Prompt conditions

| Condition | What the model sees |
|---|---|
| A · Labels only | Task instruction + the five label names |
| B · + Definitions | A + a one-sentence definition per label |
| C · Full codebook | Definitions, clarifications, negative clarifications, positive and negative examples, output reminder |

Only the codebook block differs between conditions; the instruction, input and output formats are identical.

## Data and models

- **Data:** LDA filings for 2021–2022 (117th Congress), collected from the public LDA API. Sentences that cite a bill number are the unit of analysis.
- **Test sets:** 40 hand-written probes (minimal contrast pairs), 60–100 real boundary cases found by pattern, and a random sample of 100.
- **Gold labels:** about 250 items, with 100 re-labeled after at least 14 days to measure intra-rater agreement. Real items are split into dev (40%) and test (60%); the codebook is revised on dev only and the test split is evaluated once.
- **Models:** `llama3.1:8b` via Ollama (temperature 0, fixed seed), plus one low-cost API model.
- **Metrics:** macro-F1 (primary) and weighted F1, with bootstrap 95% intervals.

## Roadmap

| Phase | Weeks | Content | Gate |
|---|---|---|---|
| 0 · Setup | 1–2 (16–29 Nov 2026) | Readings, environment, 40 probes, codebook v0.1, LDA collection | G0: probes and codebook v0.1 ready |
| 1 · Label-free | 3–4 (30 Nov–13 Dec) | Conditions A/B/C, Tests I–IV, M0 vs LLM, real boundary cases | G1: model passes Tests I–III |
| 2 · Gold & errors | 5–6 (14–27 Dec) | Gold labels, dev/test split, Tests V and VII, ablation, error analysis, codebook v1.0 | |
| 3 · Final & writing | 7–8 (28 Dec–10 Jan) | Re-labeling, single final test run, report, reproducible repository | |
| 4 · Sharing | from 11 Jan | Feedback, decide on presentation or preprint | |

The full plan, including readings, weekly tasks and deliverables for each phase, is in [`docs/phase_task_guide.pdf`](docs/phase_task_guide.pdf).

## Repository layout

```
codebook/          codebook_v0.1.md, codebook_v1.0.md, revisions.md
data/raw/          LDA filings as downloaded (not committed)
data/processed/    sentences, samples, probes, boundary cases, gold labels, split
prompts/           cond_A.txt, cond_B.txt, cond_C.txt, test_VII_swapped.txt
src/               collect_lda.py, extract_sentences.py, run_llm.py, m0_rules.py, metrics.py
results/           phase1/, phase2/, final/
notes/             tests_spec.md, memos
report/            report.pdf, summary.pdf
docs/              phase_task_guide.pdf
```

## Status

Phase 0 (setup). The codebook and test specification are templates to be filled in.

## Working notes

- [`notes/review_2026-11-16.md`](notes/review_2026-11-16.md): design review and AI-use boundaries.
- [`notes/verification_guide.md`](notes/verification_guide.md): how to check direction and code without an advisor.
- `src/*.py` and `tests/test_metrics.py` are pseudo-code skeletons; the implementations are written by hand.
