"""Rule-based baseline for ESG message triage (BUS5001 A3 Q3).
Keyword rules only. No machine learning. Written for this assessment.
Run: python rule_based_baseline.py
"""
import json, re, datetime

MESSAGES = {
  "M1": "There is a water leak in Building C that has been running all morning.",
  "M2": "I want to report that one of our suppliers may not meet our sustainability policy.",
  "M3": "The accessible entrance near the main building has been blocked for two days.",
  "M4": "The recycling bins are contaminated again and no one seems to be checking them.",
  "M5": "The air conditioning is running overnight in an empty office.",
}

# Ordered rules: first match wins. (pattern, category, team)
RULES = [
  (r"\b(accessible|wheelchair|ramp|lift|disabled|accessibility)\b", "ACCESSIBILITY_INCLUSION", "ACCESSIBILITY_SERVICES"),
  (r"\b(supplier|procurement|vendor|purchas)\w*", "PROCUREMENT_SUPPLIER", "PROCUREMENT"),
  (r"\b(policy|misconduct|breach|compliance)\b", "GOVERNANCE_POLICY", "GOVERNANCE_COMPLIANCE"),
  (r"\b(leak|leaking|flood|burst|tap|pipe|water)\b", "ENVIRONMENTAL_WATER", "FACILITIES_MAINTENANCE"),
  (r"\b(recycl|bin|waste|contaminat|rubbish|disposal)\w*", "ENVIRONMENTAL_WASTE", "SUSTAINABILITY_TEAM"),
  (r"\b(air conditioning|aircon|heating|lights?|power|energy|electricity)\b", "ENVIRONMENTAL_ENERGY", "SUSTAINABILITY_TEAM"),
]
URGENT_WORDS = r"\b(all morning|for two days|overnight|again|running|blocked|burst|flood|danger|injur)\w*"

def classify(msg):
    text = msg.lower()
    for pat, cat, team in RULES:
        if re.search(pat, text):
            urgency = "HIGH" if re.search(URGENT_WORDS, text) else "MEDIUM"
            return {"issue_category": cat, "recommended_team": team, "urgency": urgency}
    return {"issue_category": "OTHER_UNCLEAR", "recommended_team": "HUMAN_TRIAGE", "urgency": "LOW"}

if __name__ == "__main__":
    out = {
      "run_timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
      "method": "keyword rules, first match wins (rule_based_baseline.py)",
      "results": {k: {"message": v, **classify(v)} for k, v in MESSAGES.items()},
    }
    with open("rule_based_baseline_output.json", "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))
