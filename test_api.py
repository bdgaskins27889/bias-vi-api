"""
BIAS-VI API - Endpoint Test Suite
Validates all three core endpoints against real-world scenarios.
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"x-api-key": "biasvi-demo-key-etv-institute-2026", "Content-Type": "application/json"}

def print_result(title, result):
    print(f"\n{'='*60}")
    print(f"  TEST: {title}")
    print(f"{'='*60}")
    print(json.dumps(result, indent=2))

# --- TEST 1: Status Check ---
print("\n[1/4] Testing API Status...")
r = requests.get(f"{BASE_URL}/")
print_result("API Status", r.json())

# --- TEST 2: Translator Classifier (False Positive Scenario) ---
print("\n[2/4] Testing /v1/analyze - False Positive Scenario...")
payload = {
    "text": "On sight, I'm sliding tonight. They took my brother and I'm crashing out fr."
}
r = requests.post(f"{BASE_URL}/v1/analyze", headers=HEADERS, json=payload)
print_result("Translator Classifier (False Positive Test)", r.json())

# --- TEST 3: De-escalation Router ---
print("\n[3/4] Testing /v1/respond - De-escalation Scenario...")
payload = {
    "user_message": "I just found out who did it. I'm about to handle this myself tonight."
}
r = requests.post(f"{BASE_URL}/v1/respond", headers=HEADERS, json=payload)
print_result("De-escalation Router", r.json())

# --- TEST 4: CWI Data Extraction ---
print("\n[4/4] Testing /v1/extract - CWI Data Extraction...")
payload = {
    "field_notes": (
        "Responded to a call on the south side. The individual was extremely agitated "
        "after seeing a post on social media that he believed was directed at him. "
        "He kept mentioning his daughter and not wanting to go back to prison. "
        "After 45 minutes of conversation, he agreed to go home and sleep on it. "
        "Situation was de-escalated successfully."
    )
}
r = requests.post(f"{BASE_URL}/v1/extract", headers=HEADERS, json=payload)
print_result("CWI Data Extraction", r.json())

print("\n\n✅ All tests complete.")
