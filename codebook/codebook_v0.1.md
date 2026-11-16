# Codebook v0.1

Format follows Halterman & Keith (2026), Figure 1. Each class has the same fields so that components can be removed one at a time in the ablation.

Version: v0.1 · Status: draft · Last revised: 2026-11-13

## Task instruction

You will read one sentence from a U.S. Lobbying Disclosure Act (LDA) report and one bill number it mentions. Classify the interest group's position on that bill into exactly one of the labels below. Use only the definitions in this codebook, not general knowledge about the words.

## Unit and decision order

- Unit: (interest group, bill, report sentence). If a sentence mentions several bills, judge each bill separately.
- Decision order: explicit support or opposition → SUPPORT / OPPOSE → otherwise substantive involvement → ENGAGE → otherwise a plain mention → MENTION → cannot decide → UNCLEAR.
- The label must be justified by a phrase that can be quoted from the sentence.

## SUPPORT

- **Label:** SUPPORT
- **Definition:**
- **Clarification:**
- **Negative clarification:**
- **Positive example:**
- **Negative example:**

## OPPOSE

- **Label:** OPPOSE
- **Definition:**
- **Clarification:**
- **Negative clarification:**
- **Positive example:**
- **Negative example:**

## ENGAGE

- **Label:** ENGAGE
- **Definition:**
- **Clarification:**
- **Negative clarification:**
- **Positive example:**
- **Negative example:**

## MENTION

- **Label:** MENTION
- **Definition:**
- **Clarification:**
- **Negative clarification:**
- **Positive example:**
- **Negative example:**

## UNCLEAR

- **Label:** UNCLEAR
- **Definition:**
- **Clarification:**
- **Negative clarification:**
- **Positive example:**
- **Negative example:**

## Boundary rules to cover

| Phrase | Correct label | Covered in class |
|---|---|---|
| supported the goals of | ENGAGE | |
| supported with amendments | ENGAGE | |
| expressed concerns | ENGAGE | |
| opposed Title III | ENGAGE | |
| opposed unless amended | OPPOSE | |

## Output reminder

Answer with exactly one label from SUPPORT, OPPOSE, ENGAGE, MENTION, UNCLEAR. Output the label only, with no explanation.
