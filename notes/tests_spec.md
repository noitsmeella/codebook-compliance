# Test specification

Fix every entry below before running the corresponding test. Thresholds are set in advance and not changed after seeing results.

| Test | Input | Expected output | Metric | Threshold |
|---|---|---|---|---|
| I · Legal labels | All items, all conditions | One of the five labels | Share of valid labels | |
| II · Definition recovery | Each class definition as the input | That class | Accuracy | |
| IIIa · Positive examples | Codebook positive examples | Their class | Accuracy | |
| IIIb · Negative examples | Codebook negative examples | Not their class | Accuracy | |
| IV · Order invariance | Original, reversed and 3 seeded shuffles of class order | Same prediction | Share unchanged; Fleiss' kappa | |
| V · Exclusion criteria | Items where an exclusion rule applies (dev + probes) | The rule's label | Accuracy per rule | |
| VI · Generic labels (optional) | Labels renamed LABEL_1…LABEL_5 | Same class | Accuracy | |
| VII · Swapped labels | Definitions kept, label names permuted | Label that matches the definition | Follow-definition rate | |

## Reliability (self re-labeling)

- Metrics: Krippendorff's alpha (nominal), Cohen's kappa
- Minimum acceptable value:
- Gap between first and second labeling: at least 14 days

## Differences from Halterman & Keith (2026)

- Inputs are single sentences rather than documents.
- Five classes.
- LDA report text.
