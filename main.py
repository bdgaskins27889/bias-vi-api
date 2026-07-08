"""
BIAS-VI API v1.0 - Working Prototype
The ETV Institute | Center for Decision Science
Author: Barbara D. Gaskins, Founder & Lead Researcher

This prototype implements three core endpoints:
  1. /v1/analyze  - The Translator Classifier
  2. /v1/respond  - The Anti-Surveillance De-escalation Router
  3. /v1/extract  - The CWI Data Extraction Engine
"""

import os
import json
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from typing import Optional

# --- App Initialization ---
app = FastAPI(
    title="BIAS-VI API",
    description=(
        "The ETV Institute's Cultural Safety Layer for AI deployed in "
        "Community Violence Intervention environments. Anti-surveillance. "
        "Trauma-informed. Community-first."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- OpenAI Client (uses sandbox pre-configured credentials) ---
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1"),
)

# --- API Key Auth (simple demo key for prototype) ---
DEMO_API_KEY = "biasvi-demo-key-etv-institute-2026"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != DEMO_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key. Contact the ETV Institute for access.")
    return x_api_key

# ============================================================
# CORE AI LOGIC: SYSTEM PROMPTS
# ============================================================

TRANSLATOR_SYSTEM_PROMPT = """
You are the BIAS-VI "Translator" AI, developed by the ETV Institute. Your primary function is to analyze text from urban communities and identify the difference between expressive language (grief, frustration, cultural vernacular) and actionable, imminent violence.

You operate under the "Translators" philosophy: You do not judge language by corporate or academic standards. You judge it by street context.

When analyzing the provided text, apply the following rules:
1. FALSE POSITIVE PREVENTION: Do not flag culturally specific vernacular (e.g., "crashing out," "standing on business," "sliding") as imminent violence unless it is attached to a specific, actionable plan (time, location, weapon, specific target).
2. GRIEF IDENTIFICATION: Recognize expressions of profound grief or mourning (e.g., "I can't believe they took my brother, I'm losing my mind") as emotional processing, not as immediate threats of retaliation.
3. BIAS-VI MAPPING: If a threat is present, identify which stage of the BIAS-VI cognitive sequence the author is in (Bias, Interpretation, Assumption, Strategy).

Output your analysis ONLY in strict JSON format with no extra text:
{
  "is_imminent_threat": boolean,
  "primary_emotion": "string (e.g., Grief, Anger, Humiliation, Unknown)",
  "cultural_context_note": "string (Explain the vernacular or emotional context)",
  "bias_vi_stage": "string (Bias, Interpretation, Assumption, Strategy, or None)"
}
"""

DESESCALATION_ROUTER_SYSTEM_PROMPT = """
You are the BIAS-VI "De-escalation Router," an ethical safety middleware developed by the ETV Institute. Your job is to generate a response to a user in conflict that complies with the strict Anti-Surveillance Guarantee.

CRITICAL RULES:
1. NO POLICING: You must NEVER recommend contacting law enforcement, utilizing predictive policing algorithms, or increasing surveillance as a primary solution to community conflict.
2. THE PAUSE: Your response must prioritize creating a "Pause for Peace." Ask the user: "What happens if you wait 24 hours?"
3. PAUSE ANCHORS: Guide the user to identify their Pause Anchor (e.g., family, freedom, future). Ask them: "Is this situation worth risking what matters most to you?"
4. R.I.P. PROTOCOL: Remind the user that Retaliation Is Permanent. Temporary emotions should not dictate permanent consequences.

Your response must be empathetic, direct, and street-credible. Do not sound like a therapist or a cop. Sound like a credible mentor who has been through it.
"""

CWI_EXTRACTION_SYSTEM_PROMPT = """
You are the BIAS-VI Data Extraction Engine. Your job is to read unstructured field notes from violence interrupters and extract the macro-level data required for the ETV Community Wellness Index.

STRICT ANTI-SURVEILLANCE RULE: You must completely ignore and redact any names, addresses, gang affiliations, or specific identifying details. You track patterns, not people.

Extract the following data points from the narrative:
1. TRIGGER: What started the conflict? (e.g., Social Media, Neighborhood Dispute, Financial Stress, Grief, Romantic Conflict, Unknown).
2. EMOTION: What was the primary emotion described? (e.g., Anger, Humiliation, Fear, Grief, Unknown).
3. PAUSE ANCHOR: Did the individual mention something they were trying to protect? (e.g., Child, Freedom, Job, Reputation, None).
4. OUTCOME: Was the situation Resolved, De-escalated, Delayed, or Escalated?

Output your analysis ONLY in strict JSON format with no extra text:
{
  "trigger_category": "string",
  "primary_emotion": "string",
  "pause_anchor_identified": boolean,
  "pause_anchor_type": "string or null",
  "intervention_outcome": "string"
}
"""

# ============================================================
# REQUEST / RESPONSE SCHEMAS
# ============================================================

class AnalyzeRequest(BaseModel):
    text: str
    class Config:
        json_schema_extra = {
            "example": {
                "text": "On sight, I'm sliding tonight. They took my brother and I'm crashing out."
            }
        }

class RespondRequest(BaseModel):
    user_message: str
    class Config:
        json_schema_extra = {
            "example": {
                "user_message": "I just found out who did it. I'm about to handle this myself."
            }
        }

class ExtractRequest(BaseModel):
    field_notes: str
    class Config:
        json_schema_extra = {
            "example": {
                "field_notes": (
                    "Responded to a call on the south side. Individual was extremely agitated "
                    "after seeing a post on social media that he believed was directed at him. "
                    "He kept mentioning his daughter and not wanting to go back to prison. "
                    "After 45 minutes of conversation, he agreed to go home and sleep on it."
                )
            }
        }

# ============================================================
# ENDPOINTS
# ============================================================

@app.get("/", tags=["Status"])
def root():
    return {
        "api": "BIAS-VI API",
        "version": "1.0.0",
        "institution": "The ETV Institute | Center for Decision Science",
        "status": "operational",
        "philosophy": "We track decisions, not people.",
    }


@app.post("/v1/analyze", tags=["Translator Classifier"])
def analyze_text(request: AnalyzeRequest, api_key: str = Depends(verify_api_key)):
    """
    **The Translator Classifier**

    Analyzes incoming text to distinguish between culturally expressive language
    and actionable, imminent threats. Prevents false positives caused by
    standard LLMs misreading street vernacular.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": TRANSLATOR_SYSTEM_PROMPT},
                {"role": "user", "content": request.text},
            ],
            temperature=0.1,
            response_format={"type": "json_object"},
        )
        result = json.loads(response.choices[0].message.content)
        return {
            "endpoint": "v1/analyze",
            "input_text": request.text,
            "bias_vi_analysis": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.post("/v1/respond", tags=["De-escalation Router"])
def generate_response(request: RespondRequest, api_key: str = Depends(verify_api_key)):
    """
    **The Anti-Surveillance De-escalation Router**

    Generates a culturally competent, trauma-informed response to a user in
    conflict. Strictly prohibits carceral or surveillance-based recommendations.
    Applies the ETV Pause for Peace, Pause Anchor, and R.I.P. protocols.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": DESESCALATION_ROUTER_SYSTEM_PROMPT},
                {"role": "user", "content": request.user_message},
            ],
            temperature=0.7,
        )
        result = response.choices[0].message.content
        return {
            "endpoint": "v1/respond",
            "user_message": request.user_message,
            "bias_vi_response": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Response generation failed: {str(e)}")


@app.post("/v1/extract", tags=["CWI Data Extraction"])
def extract_cwi_data(request: ExtractRequest, api_key: str = Depends(verify_api_key)):
    """
    **The CWI Data Extraction Engine**

    Processes unstructured field notes from ETV Practitioners and extracts
    anonymized, macro-level data for the ETV Community Wellness Index.
    Strictly anti-surveillance: no names, addresses, or identifiers are captured.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": CWI_EXTRACTION_SYSTEM_PROMPT},
                {"role": "user", "content": request.field_notes},
            ],
            temperature=0.1,
            response_format={"type": "json_object"},
        )
        result = json.loads(response.choices[0].message.content)
        return {
            "endpoint": "v1/extract",
            "cwi_data": result,
            "privacy_notice": "No PII captured. Data used exclusively for the ETV Community Wellness Index.",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {str(e)}")
