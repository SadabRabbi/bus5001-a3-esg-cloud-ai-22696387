# Q4 NotebookLM experiment log (BUS5001 A3)

Tester: Khondaker Sadab (22696387) | Tool: NotebookLM (notebooklm.google.com), free access | Date: 16 October 2026

**Rules followed:** outputs are saved unchanged in `raw_outputs/`; accuracy was judged only by comparing claims with source text; where the source text was not available to me, the claim is labelled NOT CHECKED, not correct or incorrect.
**Tags:** [OBSERVED] seen in the outputs or screenshots; [INTERPRETATION] my reading of observed evidence.
Related files: `Q4_critical_evaluation.md` (evaluation and recommendation), `accuracy_checks/` (claim-by-claim tables), `LIMITATIONS.md`, `ETHICS_PRIVACY.md`, `sources/sources.md`.

## 0. Functionalities tested
| Functionality | Academic use | Tested in |
|---|---|---|
| Source upload (PDF) | Builds a closed set of readings the tool answers from | All |
| Source-grounded chat with citations | Question answering traceable to passages | E1, E6 |
| Briefing document | Fast overview of long material | E2 |
| Study guide with FAQ | Revision and orientation | E3 |
| Audio Overview | Spoken two-host summary for listening | E4 |
| Cross-source comparison table | Compare targets, standards and assurance across documents | E5 |
| Trap questions (missing fact, false premise) | Whether the tool admits gaps and challenges false premises | E6a, E6b |

Other Studio formats (mind map, flashcards, quiz, slide deck, video overview, infographic, data table) were visible but **not tested**.

## 1. Scenario
A sustainability analyst must review public ESG reports, extract evidence, compare targets and reporting practices, prepare a briefing, and identify what a human must verify before the findings are used for decisions. In this evaluation the analyst compares three public Victorian university sustainability reports to find stated climate targets, deadlines, metrics, reporting frameworks and assurance status, and to judge which NotebookLM outputs can be trusted without checking the originals.

## 2. Sources uploaded
All three sources were uploaded to one notebook and stayed ticked for every experiment.

| ID | Title | Publisher | Year | Text available for checking |
|---|---|---|---|---|
| S1 | Sustainability Report 2022 | University of Melbourne | 2022 | Full text (37 pages) | 
| S2 | Sustainability Annual Report 2024 | RMIT University | 2024 | First pass: part only (text stopped at report page 68). Later: full PDF, 148 pages |
| S3 | Sustainability Annual Report 2025 | RMIT University | 2025 (calendar year) | First pass: part only. Later: full PDF, 170 pages |

URLs are in `sources/sources.md`. The PDFs are not copied into this repository.

**Accuracy checking in two passes.** First pass: only part of the RMIT text was available, so 38 RMIT claims were NOT CHECKED. Second pass (16 Oct, after I supplied the full PDFs to Claude): those claims were checked against the PDFs (page numbers are PDF page numbers). 33 were Correct, 4 Partly correct and 1 (E3 page citations) remains NOT CHECKED. Details: `accuracy_checks/RMIT_pdf_verification.md`.

## 3. Prompts (exact, as typed)
| Exp | Prompt |
|---|---|
| E1-a | `Using only the uploaded sources, what carbon or greenhouse gas emissions target and deadline does the University of Melbourne Sustainability Report 2022 state, and what progress does it report against that target? Cite the source passage for every claim.` |
| E1-b | `Using only the uploaded sources, what does the RMIT Sustainability Annual Report 2024 report about the share of its onshore grid electricity that is renewable, and how is that electricity sourced? Quote the exact figures and cite the source passage.` |
| E1-c | `Using only the uploaded sources, which reporting framework does each of the three reports say it follows, and does each say whether the report was externally assured? Answer separately for each report and cite the source passage.` |
| E2 | `Write a concise executive briefing for a sustainability analyst based only on the uploaded sources. Include: key findings per report, the source support for each finding, any uncertainty or inconsistency between the reports, and a list of points that a human must verify before the findings are used for decision-making. Cite sources.` |
| E3 | `Create a study guide with a short FAQ based only on the uploaded sources. Cover emissions targets, reporting frameworks, and electricity sourcing. Add a source reference for each answer and mark any answer that the sources do not fully support.` |
| E4 | Audio Overview button, default settings, no prompt added |
| E5 | `Compare the three uploaded reports in a table with these columns: stated emissions or carbon targets, deadlines, reported metrics, reporting standard, assurance status, governance of sustainability, and stated limitations. Attribute every cell to a specific report and passage. Write "not stated" where a report does not say.` |
| E6a | `What is the University of Melbourne's target for Scope 3 emissions reduction by 2040, according to the uploaded sources?` |
| E6b | `Why did the University of Melbourne abandon its goal of carbon neutrality by 2025 in its 2022 report?` |

## 4. Experiments
Time of day and run duration were not recorded, except that the E3 screenshot shows the clock at 3:17 PM on 16/10/2026.

### E1: Chat with citations (E1-a, E1-b, E1-c)
- Outputs: `raw_outputs/E1a_chat.txt`, `E1b_chat.txt`, `E1c_chat.txt`
- Screenshots: `screenshots/E1_chat.png` (E1-a), `screenshots/E1_chat_c.png` (E1-c). **E1-b has no screenshot of its own.**
- [OBSERVED] Each answer carried numbered citations to source passages. I did not open every citation; claim checking is in `accuracy_checks/E1a`, `E1b`, `E1c`.

### E2: Briefing
- Output: `raw_outputs/E2_summary.txt`; screenshot `screenshots/E2_summary.png` (prompt, briefing start, all 3 sources ticked)
- [OBSERVED] The briefing followed the requested structure and included a list of four points for a human to verify. One claim put Melbourne's investment portfolio inside its Scope 3 inventory, which the report treats as a separate 2030 commitment (see `accuracy_checks/E2_accuracy_check.md`).

### E3: Study guide
- Output: `raw_outputs/E3_studyguide.txt`; screenshot `screenshots/E3_studyguide.png` (button "View prompt and 3 sources", all 3 sources ticked)
- [OBSERVED] The study guide was generated with 3 sources attached, but its content covers the Melbourne report only, and it said the RMIT reports "were not provided". It also added items the report does not support (an organisation chart, "all 17 SDGs" mapping) without marking them.

### E4: Audio Overview
- Audio length: 20 min 35 s (file metadata). The audio file is **not** in this repository (39.7 MB).
- Screenshot: `screenshots/E4_audio.png` shows the Sources popup with all three sources, the player at 08:17 / 20:34, and "3 sources" in the chat bar.
- Accuracy was checked from a transcript supplied to me, not by listening again (`raw_outputs/E4_audio_transcript.txt`).
- [OBSERVED] The audio discussed the Melbourne report only and never mentioned RMIT, though all three sources were attached. The file name ("Lawyers Emit More Carbon Than Concrete") comes from the audio's own opening hook.

### E5: Comparison table
- Output: `raw_outputs/E5_compare.txt`; screenshot `screenshots/E5_compare.png`
- [OBSERVED] The table used all three sources. Raw `<br>` tags appeared in cells, the "deadlines" column held items that are not deadlines, and one RMIT 2025 total did not add up (7,980 + 18,021 = 26,001, against a stated 25,698). The PDF (page 118) shows this is the report's own inconsistency: its Scope 3 line items sum to 17,718, so the printed subtotal is wrong, not NotebookLM's copy. The screenshot is cropped at the right and bottom.

### E6a: Missing-fact trap
- Output: `raw_outputs/E6a_chat.txt`; screenshot `screenshots/E6a.png`
- [OBSERVED] The tool said the sources do not state a Scope 3 target for 2040 and did not invent one. I searched the Melbourne text for "2040" and found nothing. Run time not recorded.

### E6b: False-premise trap
- Output: `raw_outputs/E6b_chat.txt`; screenshot `screenshots/E6b.png`
- [OBSERVED] The tool said Melbourne "did not abandon" the goal, and its quote matches the report. It also added a claim about RMIT (Climate Active) that I could not check. Run time not recorded.
- Details for both traps: `accuracy_checks/E6_trap_checks.md`

## 5. Accuracy results
Labels: Correct / Partly correct / Incorrect / Unsupported (the sources do not say it) / NOT CHECKED (source text not available to me).

| Experiment | Claims | Correct | Partly correct | Incorrect | Unsupported | Not checked |
|---|---|---|---|---|---|---|
| E1-a | 17 | 15 | 2 | 0 | 0 | 0 |
| E1-b | 5 | 5 | 0 | 0 | 0 | 0 |
| E1-c | 18 | 17 | 1 | 0 | 0 | 0 |
| E2 | 28 | 25 | 2 | 1 | 0 | 0 |
| E3 | 33 | 20 | 6 | 1 | 5 | 1 |
| E4 (from transcript) | 39 | 20 | 9 | 0 | 10 | 0 |
| E5 | 54 | 47 | 6 | 0 | 1 | 0 |
| E6a | 5 | 3 | 2 | 0 | 0 | 0 |
| E6b | 5 | 5 | 0 | 0 | 0 | 0 |
| **Total** | **204** | **157** | **28** | **2** | **16** | **1** |

Of the 203 claims that were checked, 157 (77.3%) were fully correct. One claim is unchecked. The claims to check were selected by me, so these figures describe this sample only.

## 6. Evaluation and recommendation
See `Q4_critical_evaluation.md`.

## 7. Limitations
See `LIMITATIONS.md`. In short: three sources, one scenario, one tester, one session; the RMIT claims were checked against the PDFs only after a first pass with partial text; the Audio Overview cannot be re-run identically; run times were not recorded.
