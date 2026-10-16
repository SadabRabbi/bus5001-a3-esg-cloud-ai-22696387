# E1-c accuracy check (reporting framework and assurance, three reports)

Checked 16 Oct 2026 against TEXT returned by the fetch tool. LIMIT: the received text of each RMIT report is partial (RMIT 2024 stops at p.68; RMIT 2025 does not include the later GRI index), so claims that depend on later sections are NOT CHECKED. open item: to check those in the PDFs and to click citation numbers.
Raw output: `raw_outputs/E1c_chat.txt`.

| # | Report | NotebookLM claim (short form) | Classification | Where | Explanation / note |
|---|---|---|---|---|---|
| 1 | Melbourne 2022 | Informed by GRI Reporting Principles | Correct | "informed by Reporting Principles from the Global Reporting Initiative (GRI)" (about report page 4) | Matches |
| 2 | Melbourne 2022 | Draws on draft ISSB sustainability and climate-related disclosure standards | Correct | Same paragraph | Matches |
| 3 | Melbourne 2022 | Structured around SP2030 and links to SDGs | Correct | SP2030 reporting statement; SDG section | Matches |
| 4 | Melbourne 2022 | Does not state whole-report external assurance | Correct (absence) | No "assurance" statement in the text received | Absence claim; confirm by Ctrl+F "assur" in the PDF |
| 5 | Melbourne 2022 | Green Bond externally audited for period ending 31 Dec 2022, aligned with Green Bond Principles | Correct | Responsible investments section | Matches |
| 6 | Melbourne 2022 | EMS complies with ISO 14001:2015 | Correct | "compliant with requirements of ... ISO 14001:2015" | Matches |
| 7 | Melbourne 2022 | GHGI prepared by Pangolin Associates, Climate Active compliant | Correct | Greenhouse gas emissions section | Matches |
| 8 | RMIT 2024 | Prepared in accordance with GRI Standards: Core option | Correct | Section 1.1 | Matches verbatim |
| 9 | RMIT 2024 | Informed by GRI principles and guided by AA1000 | Correct | Section 1.2 Materiality | Matches |
| 10 | RMIT 2024 | Uses SDGs to map and evaluate impact across teaching, research and operations | Partly correct (verified in the full PDF; see RMIT_pdf_verification.md) | SDGs are referenced, but the exact "map and evaluate across teaching, research, operations" wording was not verified | Check the report's SDG section |
| 11 | RMIT 2024 | "has not been externally assured" | Correct | Section 1.1: "The information contained has not been externally assured." | Matches |
| 12 | RMIT 2024 | Property Services certified and externally audited against five ISO standards (9001, 14001, 41001, 45001, 55001) | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Not in received text (only ISO 31000 risk policy found) | Ctrl+F "41001" in the PDF |
| 13 | RMIT 2025 | GRI Standards: Core option | Correct | Section 1.1 | Matches |
| 14 | RMIT 2025 | GRI principles and AA1000 guide content and materiality | Correct | Section 1.2 | Matches |
| 15 | RMIT 2025 | Structured around SDGs and UN Global Compact | Correct | Global Compact and SDG references present | Matches in substance |
| 16 | RMIT 2025 | Section 1.1 says not externally assured | Correct | Section 1.1 | Matches |
| 17 | RMIT 2025 | GRI index Disclosure 2-5: two-year assurance cycle, external assurance completed for 2024 cycle, none in 2025 | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | GRI index not in received text | See flag below |
| 18 | RMIT 2025 | Property Services maintains external certification against five ISO standards | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Not in received text | Ctrl+F "41001" |

## Flag for you (high priority, claim 17)
This claim appears to conflict with the RMIT 2024 report, which says its information "has not been externally assured." If the 2025 index really says assurance was completed for 2024, the two reports contradict each other. It is also possible NotebookLM conflated two different things: the 2025 report says RMIT conducts a formal MATERIALITY assessment every two years (Section 1.2, verified), which is a different cycle from assurance. Open the RMIT 2025 PDF, press Ctrl+F for "2-5" and "assurance", and record the exact wording and page. Do not assume NotebookLM is right or wrong until you have read it.

## Totals (E1-c)
Claims 18 | Correct 14 | Partly correct 0 | Incorrect 0 | Unsupported 0 | NOT CHECKED 4 (claims 10, 12, 17, 18). Rate among checked claims 14/14; overall rate ranges from 14/18 (77.8%) to 18/18 depending on the four unchecked claims.
Other observations [OBSERVED]: the answer separated the three reports as asked; it added extra information beyond the question (ISO certifications, audits); it correctly distinguished "report not assured" from "component audited" for Melbourne.
Citation check: NOT DONE.


**Update after reading the full RMIT PDFs (16 Oct 2026):** the previously NOT CHECKED claims in this file were resolved; see `RMIT_pdf_verification.md` for the labels, PDF page numbers and new totals.
