"""metrics.py — compute metrics (pseudo-code skeleton)

Input:  prediction CSVs, gold-label CSV
Output: tables (CSV) and figures under results/
Checks: notes/verification_guide.md B1 (hand computation), B2 (library comparison), B3 (extreme inputs)

Rule: every time you implement a metric, add hand-computed expected values to tests/test_metrics.py.
"""

# Constants: the five labels (fixed order), 1000 bootstrap resamples, seed


def valid_label_share(parsed_labels):
    """Test I: share of labels that are not INVALID."""
    raise NotImplementedError


def accuracy(gold, pred):
    """Accuracy. Used for Tests II, III, V and the probe table."""
    raise NotImplementedError


def accuracy_by_group(df, group_col, gold_col, pred_cols):
    """Accuracy table by group (e.g. rule_tested). Always include a count column per group."""
    raise NotImplementedError


def flip_rate(pred_x, pred_y):
    """Share of items where two conditions' predictions differ. Handle INVALID as decided."""
    raise NotImplementedError


def f1_scores(gold, pred):
    """Per-class F1, macro-F1, weighted F1.

    Implement it yourself first, then compare with scikit-learn.
    Handle classes missing from gold or predictions as fixed in tests_spec.md.
    """
    raise NotImplementedError


def bootstrap_ci(gold, pred, metric_fn, n_boot, seed):
    """Bootstrap 95% interval.

    1. Resample item indices with replacement (same size as the original)
    2. Compute metric_fn on the resampled items
    3. Repeat n_boot times
    4. Return the 2.5th and 97.5th percentiles
    Note: if one sentence produced several rows, decide whether to resample by sentence.
    """
    raise NotImplementedError


def order_invariance(preds_by_order):
    """Test IV: share of predictions unchanged vs the original order; Fleiss' kappa across the five orders (statsmodels)."""
    raise NotImplementedError


def follow_definition_rate(pred, label_by_definition, label_by_name):
    """Test VII: share of predictions that follow the definition, follow the name, or neither."""
    raise NotImplementedError


def intra_rater(labels_first, labels_second):
    """Re-labeling reliability: Krippendorff's alpha (nominal), Cohen's kappa."""
    raise NotImplementedError


def main():
    """Take the table to build as a command-line argument, call the matching function and save a CSV.
    This is where README's "one command per table and figure" is implemented.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
