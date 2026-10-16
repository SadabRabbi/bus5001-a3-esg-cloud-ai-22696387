# E3 accuracy check (study guide and FAQ)

Checked 16 Oct 2026 by against TEXT of the University of Melbourne 2022 report (S1) returned by the fetch tool (most of S1 was received). RMIT claims could not be checked, but the study guide made none: it declared RMIT sources "not provided". Page citations ("pp. 7, 8" and so on) and citation numbers NOT checked: open item:.
Raw output: `raw_outputs/E3_studyguide.txt`.

## Headline finding (observed)
The study guide states that the RMIT 2024 and 2025 reports "were not provided in the source context" and marks every RMIT item NOT SUPPORTED, including FAQ 7 and 8 and the whole comparison matrix. But the same notebook answered E1-b, E1-c and E2 using those RMIT reports. So within one notebook, one feature (chat) used all three sources and another (Studio study guide) behaved as if only Melbourne existed. Cause NOT YET ESTABLISHED. open item: check which sources were ticked in the Sources panel when you generated the study guide (a Studio output uses the selected sources). If RMIT was unticked, this is a setup error, not a tool fault; if all three were ticked, it is a tool inconsistency. Record which.
Second finding: the guide was told to mark unsupported answers, and it marked the RMIT items, but it did NOT mark several of its own additions that the report does not support (rows 8, 10, 14, 21 and 22 below).

| # | Claim in study guide | Classification | Evidence in S1 / note |
|---|---|---|---|
| 1 | SP2030 launched May 2022, eight-year roadmap | Correct | "launched in May 2022"; "over the next eight years" |
| 2 | Three domains: Amplifying action, Mobilising knowledge, Walking the talk | Correct | Section headings in the report |
| 3 | Sustainability Charter "defines the overarching principles and institutional commitments to environmental stewardship" | Partly correct | Charter exists ("commitments of the University's Sustainability Charter"); the description is not in the report |
| 4 | Advancing Melbourne is the institutional strategy | Correct | "institutional strategy, Advancing Melbourne" |
| 5 | SAG convened 2022; executives, staff, students; meets quarterly; advises COO Paul Axup | Correct | Governance section |
| 6 | SAG "replacing" the Sustainability Executive; "chaired by senior leaders" | Partly correct | Report: SAG "builds on the work of" the Sustainability Executive; no chair is mentioned |
| 7 | Sustainability Strategy Team led by Katie Mee: SP2030 coordination, reporting, governance | Correct | "established and led by Katie Mee, coordinates implementation of SP2030, including reporting and governance" |
| 8 | Strategy Team sits in "Chancellery / CFO Group" | Unsupported | No such placement in the text received (no "CFO" in the report text) |
| 9 | Sue Hopkins leads the Sustainability Team in "Business Services / COO Portfolio" | Partly correct | Name and duties correct; the report says "Sustainability Team, Campus Management", not Business Services or COO Portfolio |
| 10 | Organisation chart: Vice-Chancellor → University Council → University Executive → CFO Group and COO Portfolio → teams → SAG | Unsupported | No such hierarchy in the report; the diagram appears to be invented |
| 11 | Faculty roles (Schofield, McGain, Kayak, Helal, MGSE role) | Correct (names and roles) | Names and roles found; appointment years other than Helal (early 2023) not individually checked |
| 12 | Frameworks: GRI principles, draft ISSB, ISO 14001:2015 EMS, Climate Active | Correct | Verified in E1-c |
| 13 | Climate Active "toward net zero targets" | Partly correct | The report ties Climate Active to carbon neutral certification, not "net zero targets" |
| 14 | SDGs: "Maps activities across all 17 global SDGs" | Unsupported | Report says "We are currently exploring our impact in relation to the SDGs"; no "all 17" mapping found |
| 15 | Climate Change Bill 2022: 43% below 2005 by 2030, net zero by 2050 | Correct | Matches |
| 16 | QS ranking: 51st in the inaugural QS sustainability rankings | Correct | Matches |
| 17 | Pangolin GHGI; spend over $1 billion; upfront construction carbon | Correct | Matches |
| 18 | Gross 219,488; Scope 1 16,852; Scope 2 34,444; Scope 3 168,192 tCO2-e | Correct | Matches the table |
| 19 | Shares 76.6%, 7.7%, 15.7% | Correct | Computed from the table: 76.6%, 7.7%, 15.7% |
| 20 | All 21 category figures in the breakdown table | Correct | Match the inventory table |
| 21 | "Accounting Methodology / Notes" column (for example "location-based", "transmission/distribution grid losses", "refrigerant leakages in HVAC", "upstream fuel extraction", "telecommunications and cloud/data spend") | Unsupported | The report gives only numbers for most rows; it says some categories are estimated from spend and construction from LCAs. The other notes are the tool's own descriptions |
| 22 | Scope 3 electricity (4,559) labelled "Scope 3 Losses" | Unsupported (number correct) | The label is not in the report |
| 23 | Net zero electricity in 2021 and 2022 | Correct | "second year in 2022" |
| 24 | PPAs with Murra Warra and Crowlands; 67 GWh | Correct | Energy section |
| 25 | 49,575 LGCs; 64% renewable | Correct | Matches |
| 26 | Solar: 44 buildings, over 11,000 panels, over 3 GWh, about 3,000 tonnes, 650 houses | Correct | Matches |
| 27 | $6 million upgrades; 3.8 GWh; about 820 homes | Correct | Matches |
| 28 | Gas program: 2021 Parkville audit, matrix, 13 units in 10 buildings, Burnley scoping | Correct | Matches |
| 29 | 2025 target "across all institutional operational scopes"; climate positive "reducing and offsetting beyond net zero footprint" | Partly correct | Targets and years correct; "all operational scopes" and the definition are not in the report |
| 30 | Offsets table (project names, volumes, total 54,584; Scope 2 total 39,003, flights 15,581, fleet 754) | Correct | Figures and names match the offsets table; 39,003 + 15,581 = 54,584 |
| 31 | Greenfleet note: fleet emitted 253; offsets "exceeding fleet emissions"; not Climate Active so excluded | Partly correct | Fleet Scope 1 is 253 but total fleet is 315 (253 + 63 Scope 3). Report text says 315 "was more than was offset" by the 754 purchase, which reads oddly given 754 > 315 (source wording inconsistent). Non-certification and exclusion are correct |
| 32 | "RMIT 2024 and 2025 reports were not provided in the source context" (also FAQ 7, FAQ 8, matrix) | Incorrect (relative to the notebook) | Both RMIT reports were uploaded and used in E1 and E2. Pending your tick-box check (see headline) |
| 33 | Page citations ("pp. 7, 8", "pp. 5, 13", "p. 14", "p. 13") | NOT CHECKED | Printed page 7 does carry the SP2030 text, which fits the first citation; the rest are unverified |

## Totals (E3)
Claims 33 | Correct 20 | Partly correct 6 (3, 6, 9, 13, 29, 31) | Incorrect 1 (32) | Unsupported 5 (8, 10, 14, 21, 22) | NOT CHECKED 1 (33). Among 32 checked: 20/32 = 62.5% fully correct.
Error types observed [OBSERVED]: invented organisation chart; invented portfolio placement; overstated SDG mapping ("all 17"); invented methodology notes; mis-stated Climate Active purpose; elaborations of definitions; whole-feature failure to use two of three sources; failure to flag its own unsupported additions. Numerical data copied from tables was accurate throughout.
