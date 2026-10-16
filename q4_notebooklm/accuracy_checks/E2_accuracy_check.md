# E2 accuracy check (executive briefing)

Checked 16 Oct 2026 by against TEXT returned by the fetch tool. LIMIT: my text of RMIT 2024 stops at p.68 and RMIT 2025 is partial, so MOST RMIT emissions, assurance-index and strategy claims are NOT CHECKED. open item: check them in the PDFs using the Ctrl+F list at the end. Citations ([n]) not checked.
Raw output: `raw_outputs/E2_summary.txt`.
IMPORTANT CORRECTION to my earlier pre-run note: RMIT's reports contain emissions figures and strategy content that my partial text did not include. NotebookLM's output shows such content; I cannot confirm it myself.

| # | Report | NotebookLM claim | Classification | Evidence / note |
|---|---|---|---|---|
| 1 | Melbourne | Informed by GRI principles and draft ISSB standards | Correct | Introductory text |
| 2 | Melbourne | Target of Climate Active certified carbon neutrality by 2025 | Correct | Progress-against-targets table |
| 3 | Melbourne | Climate positive status by 2030 | Correct | Same table |
| 4 | Melbourne | Net GHG emissions 164,904 tCO2-e in 2022 | Correct | Emissions table (net of offsets; gross 219,488 not mentioned) |
| 5 | Melbourne | Scope 3 expanded to over $1 billion procurement spend and WFH emissions | Correct | GHG section and commuting section |
| 6 | Melbourne | Net zero emissions from electricity for second year; 64% renewable via LGCs | Correct | Same paragraph |
| 7 | Melbourne | Equity investment emissions 95,649 tCO2-e, below benchmark | Correct | Investments table (missing qualifiers: Scope 1 and 2 only; Australian equities above benchmark) |
| 8 | Melbourne | Report as a whole not externally assured | Correct (absence) | No assurance statement in the text received; confirm with Ctrl+F "assur" |
| 9 | Melbourne | Green Bond audited against Green Bond Principles | Correct (simplified) | Report: auditor found the bond meets the UoM Protocol criteria and is aligned with Green Bond Principles |
| 10 | Melbourne | EMS "was certified to ISO 14001:2015" | Partly correct | Report says the EMS "is compliant with requirements of" ISO 14001:2015; it does not say certified. Certification is a stronger claim |
| 11 | Melbourne | GHG inventory compiled by external specialists | Correct | Pangolin Associates |
| 12 | Melbourne | UoM has "a comprehensive Scope 3 inventory covering ... supply chain spend and investment portfolio equities" | **Incorrect** | The 2022 inventory table lists Scope 3 categories (procurement, flights, commuting, and so on) with no investment category. The report says the University is "committed to including its Investment Portfolio in its scope 3 emissions reporting ... by 2030", i.e. a future commitment. Investment emissions are reported separately (Scope 1 and 2 of investee companies, equities only) |
| 13 | Melbourne | Commits to Climate Active carbon neutrality certification by 2025 | Correct | As claim 2 |
| 14 | RMIT 2024 | GRI Core option; guided by AA1000 | Correct | Sections 1.1 and 1.2 |
| 15 | RMIT 2024 | Report contents not externally assured | Correct | Section 1.1 |
| 16 | RMIT 2024 | Onshore grid electricity 100% renewable | Correct | Early page (see E1-b) |
| 17 | RMIT 2025 | GRI Core option; AA1000; UN SDGs; UN Global Compact | Correct | Sections 1.1 and 1.2 and later text |
| 18 | RMIT 2025 | Section 1.1 says not externally assured | Correct | Section 1.1 |
| 19 | RMIT 2024 and 2025 | 92% Scope 1 and 2 reduction vs 2007 baseline | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Not in received text |
| 20 | RMIT 2024 | 50,107 MWh via MREP 1 and 2 | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | |
| 21 | RMIT 2024 | Total 33,995; Scope 1 7,558; Scope 2 4,631; partial Scope 3 21,805 tCO2-e | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Check arithmetic too: 7,558 + 4,631 + 21,805 = 33,994, not 33,995 (rounding difference of 1; check the report) |
| 22 | RMIT 2024 | Property Services certified against five ISO standards | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Also open from E1-c |
| 23 | RMIT 2025 | Transitioned away from Climate Active certification to a science-based net zero pathway; direct reductions over offsets | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | A major claim; verify exact wording |
| 24 | RMIT 2025 | 50,744 MWh from wind farms | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | |
| 25 | RMIT 2025 | 30,000 tCO2-e of high-integrity carbon credits for residual Scope 1 and high-confidence Scope 3 | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | |
| 26 | RMIT 2025 | Disclosure 2-5: two-year assurance cycle, external assurance completed for 2024 | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | Conflicts with RMIT 2024 "not externally assured"; see E1-c |
| 27 | RMIT 2025 | Report "includes retroactive adjustments, such as restated air travel emissions..." | Correct (verified in the full PDF; see RMIT_pdf_verification.md) | RMIT 2025 Section 1.1 says "Information from previous reports is not restated"; the claim may come from the GRI index (2-4). Verify |
| 28 | Both RMIT | Both reports acknowledge partial Scope 3 | Partly correct (verified in the full PDF; see RMIT_pdf_verification.md) | |

Note on NotebookLM's own "uncertainties" section: it correctly flagged the RMIT 2024 versus 2025 assurance wording as a contradiction and recommended human verification. That is useful behaviour, but its other two "inconsistencies" depend on unchecked claims.

## Totals (E2)
Claims 28 | Correct 16 | Partly correct 1 (claim 10) | Incorrect 1 (claim 12) | Unsupported 0 | NOT CHECKED 10 (claims 19 to 28). Rate among 18 checked: 16/18 = 88.9% fully correct. Overall rate cannot be stated until the 10 are checked.
Error types observed [OBSERVED]: stronger wording than the source ("certified" for "compliant with requirements of"); a merged-concept error (investment equities placed inside the Scope 3 inventory, which the report treats as a separate 2030 commitment); missing qualifiers (net vs gross; investments Scope 1 and 2 only).

## Your Ctrl+F checklist (open the PDFs; note the page for each)
RMIT 2024: `92%`, `2007`, `50,107`, `33,995`, `7,558`, `4,631`, `21,805`, `41001`, `assur`
RMIT 2025: `Climate Active`, `science-based`, `net zero`, `50,744`, `30,000`, `2-5`, `restate`


**Update after reading the full RMIT PDFs (16 Oct 2026):** the previously NOT CHECKED claims in this file were resolved; see `RMIT_pdf_verification.md` for the labels, PDF page numbers and new totals.
