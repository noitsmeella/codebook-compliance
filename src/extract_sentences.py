"""extract_sentences.py — extract sentences that cite a bill from activity descriptions (pseudo-code skeleton)

Input:  raw JSON in data/raw/
Output: data/processed/lda_117_sentences.csv
        data/processed/random_sample.csv (100 rows, fixed seed)
        hit counts per boundary pattern (check these first, in W2; see notes/review_2026-11-16.md 5.1)
Checks: notes/verification_guide.md B5 (sentence splitting, bill numbers), B6 (row counts, overlap)

Decide before writing code (record in Research Journal):
- What counts as a "sentence". LDA descriptions are often semicolon-separated noun phrases.
  Split on periods only, or also on semicolons and line breaks?
- Which bill-number forms to accept: H.R., S., H.Res., S.Res., H.J.Res., S.J.Res., etc.,
  and which spacing/period variants (HR 1234, H.R.1234).
"""

# Constants: bill-number regex, list of boundary patterns (for extraction, broad), seed, sample size
# Note: keep these extraction patterns separate from the rules in m0_rules.py (review memo 5.2)


def load_filings(raw_dir):
    """Read the raw JSON and flatten it into rows of
    (filing ID, year, registrant, client, issue code, activity description).

    A filing can have several activity descriptions; one description per row.
    Count empty descriptions and duplicate rows.
    """
    raise NotImplementedError


def split_sentences(description):
    """Split one activity description into a list of sentences.

    Careful: do not split at the periods in "H.R. 1234", "S. 567", "U.S.", "No.".
    One approach: replace bill numbers and abbreviations with placeholders, split, then restore.
    """
    raise NotImplementedError


def find_bills(sentence):
    """Return the bill numbers in a sentence, normalized to one standard form.

    Pick a single standard form (e.g. "H.R. 1234").
    """
    raise NotImplementedError


def build_sentence_table(filings):
    """Build a table with one row per (sentence, bill) pair.

    1. split_sentences for each description
    2. find_bills for each sentence; drop sentences with no bill
    3. If a sentence has several bills, one row per bill (same sentence_id; used to group the split)
    4. Handle exact (sentence, bill) duplicates as decided
    5. Print the row count after each step
    """
    raise NotImplementedError


def count_pattern_hits(sentences):
    """Count matched sentences per boundary pattern.

    Use the result to decide whether to keep the design (write the decision rule down before running).
    """
    raise NotImplementedError


def draw_random_sample(sentences, n, seed):
    """Draw n rows with a fixed seed. Do not read them closely yet."""
    raise NotImplementedError


def main():
    """load_filings → build_sentence_table → save → count_pattern_hits → draw_random_sample → save
    Record row counts and the seed in data/README.md and Research Journal.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
