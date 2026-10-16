# Q3: LLM triage of ESG operational messages (BUS5001 A3)
Student: Khondaker Sadab (22696387) | Runs on 16 October 2026

## What this folder shows
A revised triage prompt (v2), nine real runs of it (three messages, three runs each) in Google AI Studio with Gemini 3.5 Flash Lite, and a rule-based baseline on the same messages.

| Path | Contents |
|---|---|
| `prompts/prompt_M1.txt`, `prompt_M2.txt`, `prompt_M3.txt` | The revised prompt exactly as run; they differ only in the final message line |
| `outputs/Q3_run_log.txt` | All nine raw outputs with run times, settings and my expected labels (including a disclosed change to the M2 urgency label) |
| `baseline/rule_based_baseline.py` and `rule_based_baseline_output.json` | The keyword baseline and its output for five messages |
| `screenshots/` | AI Studio settings (account details removed), JSON validation, and the three runs of M1 |

## How to reproduce
1. Open Google AI Studio, choose Gemini 3.5 Flash Lite, set Thinking level to Minimal, and turn off grounding and tools.
2. Paste a prompt file as one message and run it in a new chat; repeat three times per message.
3. Validate each output as JSON and check that `evidence_span` is an exact quote from the message.
4. Run `python rule_based_baseline.py` in the `baseline` folder.

## Findings (see the report for the full analysis)
All nine outputs were valid JSON with exact evidence quotes. Urgency and team varied on identical input for M1 (HIGH once, MEDIUM twice), and the human-review flag was true in all runs because of a vague rule in my prompt. Three messages run three times are far too few to prove reliability.

## Limits
Temperature was not visible and was not recorded. Expected labels are one person's judgement. No controlled bias or prompt-injection test was run.
