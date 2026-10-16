"""Hugging Face zero-shot baseline for ESG message triage (BUS5001 A3 Q3).
Model: facebook/bart-large-mnli via the transformers zero-shot-classification pipeline.
Run in Google Colab (Runtime > Run all). No training. Output: hf_zero_shot_output.json
"""
# !pip -q install transformers torch   # (Colab: run this line in its own cell first)
import json, datetime, time
import transformers, torch
from transformers import pipeline

MESSAGES = {
  "M1": "There is a water leak in Building C that has been running all morning.",
  "M2": "I want to report that one of our suppliers may not meet our sustainability policy.",
  "M3": "The accessible entrance near the main building has been blocked for two days.",
  "M4": "The recycling bins are contaminated again and no one seems to be checking them.",
  "M5": "The air conditioning is running overnight in an empty office.",
}
# Natural-language labels (the model reads the words), mapped to the same categories as the LLM prompt (v2)
CATEGORY = {
  "a water leak, flooding or water waste": "ENVIRONMENTAL_WATER",
  "lighting, heating or cooling or equipment running unnecessarily": "ENVIRONMENTAL_ENERGY",
  "recycling, contamination or waste disposal": "ENVIRONMENTAL_WASTE",
  "a barrier for people with disability or an inclusion concern": "ACCESSIBILITY_INCLUSION",
  "a supplier or purchasing concern": "PROCUREMENT_SUPPLIER",
  "a possible policy breach, conduct or compliance concern": "GOVERNANCE_POLICY",
  "something else or unclear": "OTHER_UNCLEAR",
}
URGENCY = {
  "an immediate risk to people's safety or severe active damage": "CRITICAL",
  "ongoing damage, a blocked access route or a possible policy breach needing action within one day": "HIGH",
  "something that needs action within a week with no ongoing harm": "MEDIUM",
  "a minor or informational matter": "LOW",
}
clf = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def run(msg, labels):
    r = clf(msg, candidate_labels=list(labels.keys()), multi_label=False)
    return [{"label": labels[l], "score": round(s, 4)} for l, s in zip(r["labels"], r["scores"])]

out = {"run_timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
       "model": "facebook/bart-large-mnli", "transformers": transformers.__version__, "torch": torch.__version__,
       "method": "zero-shot, multi_label=False, default hypothesis template", "results": {}}
for k, m in MESSAGES.items():
    t0 = time.time()
    cat, urg = run(m, CATEGORY), run(m, URGENCY)
    out["results"][k] = {"message": m, "category_top": cat[0], "category_all": cat,
                         "urgency_top": urg[0], "urgency_all": urg, "seconds": round(time.time() - t0, 2)}
    print(k, "|", cat[0]["label"], cat[0]["score"], "|", urg[0]["label"], urg[0]["score"])
json.dump(out, open("hf_zero_shot_output.json", "w"), indent=2)
print(json.dumps(out, indent=2))
