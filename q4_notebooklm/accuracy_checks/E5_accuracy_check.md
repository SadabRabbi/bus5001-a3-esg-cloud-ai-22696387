# E5 accuracy check (three-report comparison table)

Checked 16 Oct 2026 by against TEXT returned by the fetch tool. Melbourne text was nearly complete. RMIT text was partial (RMIT 2024 stops at p.68; RMIT 2025 is partial), so most RMIT figures are NOT CHECKED. Citation numbers NOT checked: open item:.
Raw output: `raw_outputs/E5_compare.txt`.

## Correction to my own earlier expectation
I told you RMIT's carbon targets were expected to read "not stated" (E5 trap). That was based on partial text and was wrong in effect: NotebookLM reported RMIT content (2007 baseline, 92% reduction, a net zero pathway). Whether that content is accurate is for you to check in the PDFs.

## Checked claims (34)
| # | Cell | Classification | Note |
|---|---|---|---|
| M1 | Melbourne: "Certified carbon neutral across operations" | Partly correct | Same add-on wording as E1 ("across operations" not in the report) |
| M2 | Melbourne: climate positive status | Correct | Progress table |
| M3 | "Include full Investment Portfolio in climate positive target" | Partly correct | Report says "Investment Portfolio"; "full" is added; the report also says only about half of investments are reportable |
| M4 | Deadlines 2025 and 2030 | Correct | |
| M5 | Gas electrification "over the next decade" | Correct | "expected to be rolled out over the next decade" |
| M6 | Net GHG 164,904 tCO2-e | Correct | |
| M7 | "Scope 1: 16,599; Scope 2 net: 0 / 39,003 offset; Scope 3: 148,305" | Unsupported | The figures 16,599 and 148,305 are not in the report. The report gives Scope 1 = 16,852 and Scope 3 = 168,192 (gross) and subtracts offsets from the total. They add to 164,904 (16,599 + 148,305) so they look derived by the tool, but not stated in the source |
| M8 | 64% renewable via 49,575 LGCs | Correct | |
| M9 | Waste to landfill 11.8 kg per person | Correct | "11.8kg per person" |
| M10 | Equity investment emissions 95,649 | Correct | |
| M11 | GRI principles; draft ISSB | Correct | |
| M12 | "Mapped to UN SDGs" | Partly correct | Report says it is "currently exploring our impact in relation to the SDGs" |
| M13 | Whole-report assurance "not stated" | Correct | No statement in the text received |
| M14 | Green Bond audited under Green Bond Principles | Correct | |
| M15 | "EMS certified to ISO 14001:2015" | Partly correct | Report: "compliant with requirements of"; the same "certified" error as E2 |
| M16 | GHG inventory by Pangolin Associates | Correct | |
| M17 | Governance: SP2030, Charter, Advancing Melbourne, faculty deans, Curriculum Fellows | Correct | |
| M18 | Climate risk in risk register and Business Continuity Plans | Correct | |
| M19 | Environmental-sustainability scope only; social areas elsewhere | Correct | "Report scope" section |
| M20 | Investments: equities about 50%; other asset classes lack robust data | Correct | |
| M21 | Greenfleet offsets excluded from Climate Active inventory | Correct | |
| M22 | SP2030 lacks fixed action lists or indicators | Correct | "does not outline a detailed list of actions"; indicators still being determined |
| R1 | RMIT 2024: GRI Core option; AA1000 | Correct | |
| R2 | RMIT 2024: "not externally assured" | Correct | |
| R3 | RMIT 2024: 100% renewable onshore grid electricity | Correct | (the 50,107 MWh detail is NOT CHECKED, below) |
| R4 | RMIT 2024: Sustainability Committee is the peak governance body reporting through the Chair (a Deputy Vice-Chancellor) to VCE | Correct | Text found; the title "DVC Education" is cut off in my text |
| R5 | RMIT 2024: Sustainability is one of 19 Risk Domains | Correct | |
| R6 | RMIT 2024: Sustainability and Equity Evaluation (SEE) Tool | Correct | |
| R7 | RMIT 2024: 1,463 active course units aligned with SDGs | Correct | |
| R8 | RMIT 2025: GRI Core, AA1000, UN SDGs, UN Global Compact | Correct | |
| R9 | RMIT 2025: Section 1.1 not externally assured | Correct | |
| R10 | RMIT 2025: Sustainability Committee, SEE Tool, Global Resilience Office exist | Correct | |
| R11 | RMIT 2025: 1,255 active course units | Correct | |
| R12 | RMIT 2025: Sustainability Committee reports to University Executive | Correct | |

## NOT CHECKED (RMIT claims whose text I did not receive), 20 items
1 RMIT 2024: 2007 baseline of 78,048 tCO2-e; Carbon Management Plan. 2 RMIT 2024 and 2025: 92% Scope 1 and 2 reduction. 3 RMIT 2024: 33,995 total with 7,558 / 4,631 / 21,805 (see arithmetic note). 4 RMIT 2024: 50,107 MWh via MREP 1 and 2. 5 RMIT 2024: air travel 13,095 tCO2-e. 6 RMIT 2024: five ISO standards for Property Services; GEAP assessed by the Victorian Gender Equality Commission. 7 RMIT 2024: ARMC oversight. 8 RMIT 2024: prioritise eliminating emissions at source over offsets. 9 RMIT 2025: transitioned from Climate Active to a science-based net zero pathway. 10 RMIT 2025: fossil fuel exclusion on new natural gas assets. 11 RMIT 2025: landfill target 10 kg per EFTSL, achieved 9.3 kg. 12 RMIT 2025: Climate Resilience Plan due 2026. 13 RMIT 2025: Treasury climate disclosures by 2030. 14 RMIT 2025: inventory 25,698 (7,980; 0 / 39,581 offset; 18,021). 15 RMIT 2025: 50,744 MWh; 548 MWh solar. 16 RMIT 2025: 30,000 tCO2-e credits. 17 RMIT 2025: air travel 7,382 tCO2-e. 18 RMIT 2025: two-year assurance cycle (GRI 2-5). 19 RMIT 2025: Indigenous Governance Committee established 2025; Responsible Investment Principles. 20 RMIT 2025: restatements (Indigenous workforce error, air travel, water intensity), legacy carbon neutrality exclusions, data platform migration.

## Arithmetic flags for you 
- RMIT 2024: 7,558 + 4,631 + 21,805 = 33,994, not 33,995 (difference of 1; may be rounding in the report).
- RMIT 2025: 7,980 + 18,021 = 26,001 (Scope 2 net shown as 0), not the stated total of 25,698 (difference of 303). Either NotebookLM mis-copied a figure or the report's table has a different structure. CHECK in the PDF (Ctrl+F `25,698`).
- Percentages 22% / 14% / 64% for RMIT 2024 are consistent with the stated figures.

## Observed table-quality problems [OBSERVED]
- The "Deadlines" column holds non-deadlines for RMIT 2024 (a 2007 baseline, "2030 Agenda / UN SDGs" and a 92% result) and a result ("Maintained 92% reduction") for RMIT 2025; it did not write "not stated" where no deadline was given, as instructed.
- Several "Reported Metrics" and "Stated Limitations" cells blend outcomes, targets and context.
- "Fossil fuel exclusion" and "Responsible Investment Principles" are not emissions targets.
- The instruction "attribute every cell to a specific report and passage" was met only with numbered citations; no page numbers.

## Totals (E5)
Claims checked 34: Correct 29 | Partly correct 4 (M1, M3, M12, M15) | Unsupported 1 (M7) | Incorrect 0. NOT CHECKED: 20. Accuracy among checked 29/34 = 85.3%. Overall rate cannot be stated until the 20 are checked.
Repeated error types across experiments [OBSERVED]: "certified" for "compliant with" (E2, E5); add-on words ("across operations", "full/entire Investment Portfolio"); SDG overstatement (E3, E5).

**Update after reading the full RMIT PDFs (16 Oct 2026):** the 20 NOT CHECKED items were resolved: 18 Correct and 2 Partly correct (items 1 and 20). E5 now stands at 54 items: 47 Correct, 6 Partly correct, 1 Unsupported, 0 Not checked (47/54 = 87.0%). The arithmetic flag for RMIT 2025 (7,980 + 18,021 = 26,001 vs 25,698) is an inconsistency inside the report (its Scope 3 line items sum to 17,718), not a NotebookLM error. See `RMIT_pdf_verification.md`.
