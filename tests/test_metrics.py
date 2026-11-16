"""test_metrics.py — metric checks (skeleton; fill in expected values computed by hand)

Run from the repository root:  python -m pytest tests/   (requires pytest)
The toy data is the same as the table in notes/verification_guide.md B1.
"""

GOLD = ["SUPPORT", "SUPPORT", "OPPOSE", "OPPOSE", "ENGAGE",
        "ENGAGE", "ENGAGE", "MENTION", "MENTION", "UNCLEAR"]
PRED_A = ["SUPPORT", "SUPPORT", "OPPOSE", "ENGAGE", "SUPPORT",
          "OPPOSE", "ENGAGE", "MENTION", "MENTION", "MENTION"]
PRED_C = ["SUPPORT", "ENGAGE", "OPPOSE", "OPPOSE", "ENGAGE",
          "ENGAGE", "ENGAGE", "MENTION", "MENTION", "UNCLEAR"]


# For each test below: put the value you computed on paper in `expected` and compare it with the metrics function.

# def test_accuracy_A():             expected = ?
# def test_accuracy_C():             expected = ?
# def test_flip_rate_A_vs_C():       expected = ?
# def test_macro_f1_A():             expected = ?   (also compare with scikit-learn)
# def test_all_correct_gives_one():  if predictions == GOLD, accuracy and F1 are 1.0
# def test_same_preds_no_flip():     flip_rate(PRED_A, PRED_A) is 0
# def test_parse_label_variants():   "Support.", "support", "" are handled as fixed in tests_spec.md
# def test_bootstrap_reproducible(): same seed gives the same interval
