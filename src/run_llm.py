"""run_llm.py — run the LLM under conditions A/B/C (pseudo-code skeleton)

Input:  item CSV (sentence, bill), prompt template (prompts/cond_*.txt), model name, seed
Output: one CSV per run under results/<phase>/raw/
        columns: item ID, condition, raw output, parsed label, prompt hash, model ID, seed, timestamp
Checks: notes/verification_guide.md A3, B3 (parsing), B4 (reproducibility), B6 (prompts)

Before starting:
- Check the Ollama docs for the local API request format and how to set temperature and seed.
- Choose the placeholders for the sentence and the bill in the templates. They must be the same in all three conditions.
"""

# Constants: the five valid labels, Ollama address, default model name, temperature 0, default seed


def load_template(path):
    """Read a template file. Do not include the version line at the top in the prompt."""
    raise NotImplementedError


def build_prompt(template, sentence, bill):
    """Fill the template's placeholders with the sentence and the bill."""
    raise NotImplementedError


def prompt_hash(template):
    """Return a hash of the template string (hashlib), to track which prompt a run used."""
    raise NotImplementedError


def call_model(prompt, model, seed):
    """Send a request to Ollama and return the raw output.

    Temperature 0, fixed seed. Decide how many times to retry on failure.
    """
    raise NotImplementedError


def parse_label(raw_output):
    """Turn the raw output into a label.

    Write the rule in tests_spec.md first. The guide: INVALID unless it exactly matches one of the five labels.
    Decide before running whether to strip whitespace or allow case and trailing periods, and do not change it afterwards.
    """
    raise NotImplementedError


def run_condition(items, condition, template_path, model, seed, out_path):
    """Run one condition from start to finish.

    1. Read the template and compute its hash
    2. For each item: build_prompt → call_model → parse_label
    3. Collect the rows and save them (save as you go so an interrupted run can resume)
    4. Print the number of INVALID labels
    5. Add one row to Experiment Log
    """
    raise NotImplementedError


def reorder_classes(codebook_block, order):
    """For Test IV: change the order of classes in the codebook block.

    order is one of: original, reversed, and three shuffles with fixed seeds.
    """
    raise NotImplementedError


def main():
    """Read command-line arguments (input CSV, condition, model, seed, output path) and call run_condition."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
