"""m0_rules.py — rule-based baseline M0 (pseudo-code skeleton)

Input:  a CSV with sentences (and bill numbers)
Output: the same CSV with m0_label and m0_rule (name of the rule applied) columns added
Checks: expected labels on the probes' minimal contrast pairs; notes/verification_guide.md B3

Write the rules by hand. Follow the codebook's decision order:
  boundary rules (exceptions) → explicit SUPPORT/OPPOSE → ENGAGE → MENTION → UNCLEAR

Notes:
- Exception rules must come before general rules.
  e.g. check "supported with amendments" before "supported".
- Keep these rules separate from the extraction patterns in extract_sentences.py (review memo 5.2).
- When a sentence cites several bills, decide whether M0 ignores which phrase attaches to which bill
  (and report that as a limitation) or uses a simple proximity rule.
"""

# Rule list: (rule name, regex, label), in the order they are applied
# RULES = [ ... ]


def classify(sentence, bill=None):
    """Return (label, rule name) for one sentence.

    1. Normalize the sentence (e.g. lowercase)
    2. Check RULES in order; return the label of the first rule that matches
    3. If nothing matches, return the default label (decide in advance: MENTION or UNCLEAR)
    """
    raise NotImplementedError


def main():
    """Apply classify to each row of the CSV given as an argument and save the result."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
