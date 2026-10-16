# Q4 critical evaluation (built only from the experiment log and accuracy files)
*16 Oct 2026. Counts come from `Q4_experiment_log.md` and `accuracy_checks/`. The full RMIT PDFs were read later the same day (see `accuracy_checks/RMIT_pdf_verification.md`); 1 claim is still NOT CHECKED, so rates below are rates of checked claims. Scenario (assumed): a university sustainability analyst comparing the Melbourne 2022 and RMIT 2024 and 2025 reports.*

## 1. Accuracy summary (all experiments)
| Item | Claims | Correct | Partly correct | Incorrect | Unsupported | NOT CHECKED |
|---|---|---|---|---|---|---|
| E1-a, E1-b, E1-c (chat) | 40 | 37 | 3 | 0 | 0 | 0 |
| E2 briefing | 28 | 25 | 2 | 1 | 0 | 0 |
| E3 study guide | 33 | 20 | 6 | 1 | 5 | 1 |
| E4 audio (transcript-based) | 39 | 20 | 9 | 0 | 10 | 0 |
| E5 comparison table | 54 | 47 | 6 | 0 | 1 | 0 |
| E6a and E6b traps | 10 | 8 | 2 | 0 | 0 | 0 |
| **Total** | **204** | **157** | **28** | **2** | **16** | **1** |

Of the 203 checked claims, 157 (77.3%) were fully correct, 28 partly correct, 2 incorrect and 16 unsupported. One claim (page citations in E3) is unchecked.

## 2. Pattern by feature (observed)
- **Chat (E1) was the most reliable**: 37 of 40 claims correct, with citations next to each statement. Errors were small add-on wording or one paraphrase ("across its operations", "entire Investment Portfolio").
- **Studio outputs were weaker than chat**: the study guide (E3) and the audio overview (E4) both had all three sources attached (screenshots `E3_studyguide.png`, `E4_audio file.png`) but covered the Melbourne report only, and E4 contained 10 unsupported elaborations (for example drought role-play, variable frequency drives, timber versus steel) with no signal that they were not in the report.
- **Comparison (E5)**: the table helped: 47 of 54 items were correct after checking the PDFs. One figure was derived rather than reported. The RMIT 2025 total that looked wrong (7,980 + 18,021 = 26,001 against 25,698) is an error inside the report itself, whose Scope 3 line items sum to 17,718; NotebookLM copied the report faithfully.
- **Traps (E6)**: NotebookLM refused to invent a 2040 target and challenged the false "abandoned" premise, which is the behaviour you want. In E6b it also added an unrequested RMIT claim, which the RMIT 2025 PDF confirms (page 115).
- **Source inconsistencies surfaced**: RMIT 2025 says on one page that the report has not been externally assured and in its GRI index that assurance for 2024 was completed on a two-year cycle. NotebookLM reported the GRI wording correctly, so a human must reconcile the two statements.

## 3. Twelve-dimension evaluation (Claim, Evidence, Interpretation, Limitation, Recommendation)
| Dimension | Claim | Evidence | Limitation | Recommendation |
|---|---|---|---|---|
| Source grounding | Chat answers stay close to uploaded text | 37 of 40 chat claims correct | Add-on words slip in | Open the cited passage for every number |
| Citations | Chat citations make checking fast | Numbered markers in E1 and E2 screenshots | Citation present does not prove the claim is exact | Treat a citation as a pointer, not proof |
| Hallucination | Rare in chat, common in elaboration | E4: 10 of 39 unsupported; E3: 5 of 33 | Use Studio outputs for orientation only |
| Source coverage | Studio outputs may ignore attached sources | E3 and E4 cover Melbourne only | Cause not established | Check every source appears in the output |
| Numbers | Copied figures mostly right | E4 numbers accurate; E5 total mismatch traced to the report | Only RMIT figures I selected were checked | Re-verify any total or derived figure |
| Nuance | Qualifiers get dropped | E4 offsets (international credits omitted) | Single example set | Ask for caveats explicitly |
| Cross-source comparison | Useful but needs checking | E5 table, 47 of 54 correct | Seven items partly correct or unsupported | Verify before putting in a report |
| Trap handling | Good on false premises and missing facts | E6a and E6b | Two traps only | Keep trap prompts as a standing test |
| Bias | Not tested | None | No evidence either way | State as not evaluated |
| Privacy and data handling | Public reports only used | Sources are public | Provider data handling not reviewed | Do not upload confidential data without policy approval |
| Over-reliance risk | High for audio: fluent, confident, unflagged errors | E4 | Delivery tone not assessed | Do not let audio overviews stand in for the source |
| Workflow fit | Fast first pass for an analyst | Time not recorded | No time comparison with manual reading | Record time in the next trial |

## 4. Recommendation (conditional)
Use NotebookLM chat as a first-pass reading aid for a university sustainability unit, with these controls: every figure is traced to the cited passage before use; Studio outputs (study guide, audio) are not used as evidence; at least one trap prompt is run per new source set; and a named person signs off any number that enters a report. Do not adopt it for assurance, regulatory disclosure or decisions without human verification. This is based on one scenario, three sources and 204 claims, so it supports a limited pilot, not an organisation-wide rollout.
