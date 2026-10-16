# E1-b accuracy check (NotebookLM vs RMIT Sustainability Annual Report 2024, S2)

Checked 16 Oct 2026 by against the TEXT of S2 returned by the fetch tool. IMPORTANT LIMIT: that text stops at report page 68 (the received text ends in Section 7.3, "Student gender equality"), so the Operations section later in the report was NOT received. Claims that depend on later pages are marked NOT CHECKED and need you to open the PDF.
Raw output saved as `raw_outputs/E1b_chat.txt`.

| # | NotebookLM claim (exact) | Classification | Where in S2 | Explanation | Note |
|---|---|---|---|---|---|
| 1 | Share of onshore grid electricity that is renewable: 100% | Correct | Early page of the report (page marker 7 in the received text): "RMIT maintained its 100% onshore grid electricity supplied by renewable sources through our wind farm partnerships in regional Victoria." | Matches | Page number approximate; confirm in the viewer |
| 2 | Quote: "maintained its 100% onshore grid electricity supplied by renewable sources" | Correct | Same passage | Verbatim match | |
| 3 | Sourced "through our wind farm partnerships in regional Victoria" | Correct | Same passage | Verbatim match | |
| 4 | Quote: "From 1 January 2023, all onshore grid electricity was sourced from renewable energy" | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Not in the text I received (likely in the Operations section after page 68) | Cannot confirm or reject; do not treat as verified | In the PDF, press Ctrl+F for "1 January 2023" |
| 5 | "Melbourne Renewable Energy Projects 1 & 2 supplied 50,107MWh of renewable electricity to RMIT in 2024" | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Not in the text I received | The figure 50,107 MWh and the exact wording must be checked in the PDF | In the PDF, press Ctrl+F for "50,107" and "MREP" |

## Totals so far (E1-b)
Claims 5 | Correct 3 | Partly correct 0 | Incorrect 0 | Unsupported 0 | NOT CHECKED 2. Accuracy rate among CHECKED claims: 3/3. Overall rate cannot be stated until claims 4 and 5 are checked (maximum possible 5/5, minimum 3/5).
Other observations [OBSERVED]: the answer directly addressed the question; it gave quotation marks around three phrases, one of which I verified verbatim, so quoting seems reliable where checked; the two unverified quotes are the ones I could not reach.
Citation check: NOT DONE (click [1] and [2] in NotebookLM and note whether each opens the passage that supports the quote).


**Update after reading the full RMIT PDFs (16 Oct 2026):** the previously NOT CHECKED claims in this file were resolved; see `RMIT_pdf_verification.md` for the labels, PDF page numbers and new totals.
