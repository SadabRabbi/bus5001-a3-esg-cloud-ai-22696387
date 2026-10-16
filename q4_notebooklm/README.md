# BUS5001 A3 Q4: Evaluating Google NotebookLM for sustainability-report analysis
Student: Khondaker Sadab (22696387) | Unit: BUS5001 Cloud Platform and Analytics, La Trobe University | Experiments run 16 October 2026

## Purpose
An evaluation of Google NotebookLM as a first-pass reading aid for a university sustainability analyst who must compare three public sustainability reports (an assumed scenario).

## Repository contents
| Folder or file | What it holds |
|---|---|
| `Q4_critical_evaluation.md` | Accuracy summary, twelve-dimension evaluation and recommendation |
| `Q4_experiment_log.md` | Scenario, sources, exact prompts, one block per experiment (E1 to E6), accuracy totals |
| `sources/sources.md` | The three sources (links only, no copies of the PDFs) |
| `raw_outputs/` | NotebookLM replies saved unchanged, and the audio transcript (supplied by the student) |
| `accuracy_checks/` | Claim-by-claim checks against the source text (Correct, Partly correct, Incorrect, Unsupported, NOT CHECKED) |
| `screenshots/` | Screenshots of each experiment |
| `LIMITATIONS.md` | What this evaluation cannot show |
| `ETHICS_PRIVACY.md` | What was uploaded and why |

## How to reproduce
1. Open notebooklm.google.com and create a notebook.
2. Add the three sources listed in `sources/sources.md` and keep all three ticked.
3. Run the prompts in `Q4_experiment_log.md` in order (E1 chat, E2 briefing, E3 study guide, E4 audio overview, E5 comparison, E6 trap questions).
4. Check each claim against the source text and label it using the four labels above.

## Experiments
E1 source-grounded chat (three prompts), E2 executive briefing, E3 study guide with FAQ, E4 audio overview (20 min 35 s), E5 cross-source comparison table, E6a unsupported-information trap, E6b false-premise trap.

## Main findings (from the log only)
1. Of 204 claims across all experiments, 203 were checked; 157 of those (77.3%) were fully correct, 28 partly correct, 2 incorrect and 16 unsupported. One claim (E3 page citations) was not checked.
2. Chat answers were the most reliable (37 of 40 claims correct) and carried citations. The study guide and the audio overview were weaker: both had all three sources attached but covered only the Melbourne report, and the audio contained 10 unsupported elaborations out of 39 claims (for example a role-play and drought-simulation method that the report does not describe).
3. NotebookLM declined to invent a 2040 Scope 3 target and challenged a false "abandoned its goal" premise, and in the second case the unrequested claim it added about a different university was confirmed in the RMIT 2025 PDF.

## Recommendation
Use chat as a first-pass reading aid with every figure traced to the cited passage; do not use study guides or audio overviews as evidence; run a trap question for each new source set; have a named person sign off any number that enters a report. This supports a limited pilot, not an organisation-wide rollout. See `Q4_critical_evaluation.md` for the full evaluation.

## Ethics and privacy
Only public documents were uploaded. No personal or confidential data was used. See `ETHICS_PRIVACY.md`.

## Use of AI
The experiments were run in NotebookLM. An AI assistant helped draft prompts, check claims against source text and organise this repository; the student ran the experiments, supplied the outputs and is responsible for the content. An AI Acknowledgement form accompanies the submission.
