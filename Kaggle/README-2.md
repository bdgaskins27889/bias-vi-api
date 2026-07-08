# BIAS-VI Kaggle Submission

## AI Agent Security: Multi-Step Tool Attacks Competition

**Author:** Barbara D. Gaskins, M.S.
**Organization:** Street Signals Intelligence Lab
**ORCID:** [0009-0007-9915-944X](https://orcid.org/0009-0007-9915-944X)
**Competition:** [AI Agent Security - Multi-Step Tool Attacks](https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks)

---

## How This Connects to the BIAS-VI API

This folder contains the Kaggle competition submission that **documents the vulnerability** that the BIAS-VI API (in the root of this repository) is designed to prevent.

The relationship is direct and intentional:

| This Folder | Root Repository |
|---|---|
| `attack.py` documents the **problem** | `main.py` provides the **solution** |
| Cultural injection attacks trigger `UNTRUSTED_TO_ACTION` in unprotected agents | The `/v1/analyze` endpoint prevents those same attacks before the LLM processes the input |
| The Kaggle benchmark proves the failure mode exists | The BIAS-VI API provides the certified mitigation |

---

## What Is a Cultural Injection Attack?

A cultural injection attack is a class of multi-step agent failure where culturally specific language -- specifically African American Vernacular English (AAVE) and trauma-processing street vernacular -- causes a tool-using AI agent to misclassify expressive grief or ambiguous stress as an actionable threat, and then take an unsafe downstream tool action (HTTP post, email alert, law enforcement referral) that was never intended by the legitimate user.

This is not a malicious attack in the traditional sense. The "injection" is the culturally specific language itself. The vulnerability is the model's inability to interpret it correctly in context. This constitutes a form of algorithmic harm that disproportionately affects marginalized communities whose language is underrepresented in standard training data.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `attack.py` | The competition submission implementing the BIAS-VI Cultural Injection Attack |
| `bias_vi_kaggle_notebook.ipynb` | The Kaggle notebook that wraps attack.py and generates submission.csv |
| `README.md` | This file |

---

## BIAS-VI Framework Stages

The attack is organized by the six stages of the BIAS-VI decision-making model:

| Stage | Code | Description | Attack Category |
|---|---|---|---|
| Behavior | B | Observable actions and expressions | Expressive grief misclassification |
| Indicators | I | Early warning signals | Ambiguous stress escalation |
| Anchors | A | Protective stabilizing factors | Protective language misread as threat |
| Stress | S | Activation level and emotional state | High-activation language escalation |
| Variables | V | Contextual modifiers | Cultural vernacular misinterpretation |
| Intervention | VI | De-escalation and redirection | De-escalation bypass attempts |

---

## Companion Working Note

The full methodology is documented in the Working Note submitted to the competition:

**Title:** "Cultural Injection Attacks: How Vernacular Misclassification Creates Exploitable Failure Modes in Tool-Using Community Violence Intervention Agents"

The Working Note is available in the repository root as `BIAS_VI_Kaggle_Working_Note.pdf`.

---

## Mitigation

The BIAS-VI API (root of this repository) provides a three-layer cultural safety middleware that prevents these attacks:

1. **`/v1/analyze`** -- Classifies input using the BIAS-VI framework before the LLM processes it, preventing false positive threat escalation
2. **`/v1/respond`** -- Validates LLM responses against anti-surveillance rules, ensuring no unsafe tool actions are recommended
3. **`/v1/extract`** -- Logs anonymized Community Wellness Index data from interactions without collecting personally identifiable information

---

## Citation

If you use this work in your research, please cite:

```
Gaskins, B. D. (2026). BIAS-VI API: Cultural Safety Middleware for AI in Community
Violence Intervention Environments [Software]. Street Signals Intelligence Lab.
https://github.com/bdgaskins27889/bias-vi-api
ORCID: 0009-0007-9915-944X
```

---

*This research is conducted in partnership with End The Violence (ETV), a registered
nonprofit in Ohio founded by Dr. Sean Stevenson, dedicated to community-driven
violence prevention.*
