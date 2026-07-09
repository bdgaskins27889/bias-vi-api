# BIAS-VI API: Cultural Safety Middleware for AI

**Street Signals Intelligence Lab | In Partnership with End The Violence (ETV)**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21271446.svg)](https://doi.org/10.5281/zenodo.21271446)[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--9915--944X-green)](https://orcid.org/0009-0007-9915-944X)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com)

---

## Overview

The **BIAS-VI API** is an open-source ethical safety middleware designed for Artificial Intelligence deployed in Community Violence Intervention (CVI), social services, and high-stakes urban environments.

Developed by **Barbara D. Gaskins, M.S.** at the Street Signals Intelligence Lab, this API acts as a "Cultural Safety Layer." It prevents standard large language models from generating false positives based on street vernacular and ensures all AI responses adhere to a strict **Anti-Surveillance Guarantee**.

This work is conducted in partnership with **End The Violence (ETV)**, a registered nonprofit in Ohio founded by Dr. Sean Stevenson, dedicated to community-driven violence prevention.

---

## Core Features

- **The Translator Classifier (****`/v1/analyze`****):** Distinguishes between culturally expressive language (grief, venting) and actionable, imminent threats. Prevents the false positive failure mode documented in the BIAS-VI Kaggle Benchmark.

- **The De-escalation Router (****`/v1/respond`****):** Generates culturally competent, trauma-informed responses that prioritize the "Pause for Peace" protocol and never recommend predictive policing or carceral action.

- **The CWI Data Extraction Engine (****`/v1/extract`****):** Extracts anonymized, macro-level data from unstructured field notes to power the Community Wellness Index (CWI) without capturing any personally identifiable information (PII).

---

## Why This Exists: The Cultural Blind Spot Problem

Standard large language models often fail when processing urban vernacular, flagging expressive grief as "violent" or recommending carceral solutions (police intervention) for community conflicts. This constitutes a form of algorithmic harm that disproportionately affects marginalized communities whose language is underrepresented in standard training data.

The BIAS-VI API solves this "cultural blind spot" by applying the six-stage BIAS-VI decision-making framework before the AI responds:

| Stage | Code | Description |
| --- | --- | --- |
| Behavior | B | Observable actions and expressions |
| Indicators | I | Early warning signals |
| Anchors | A | Protective stabilizing factors |
| Stress | S | Activation level and emotional state |
| Variables | V | Contextual modifiers |
| Intervention | VI | De-escalation and redirection |

---

## The Kaggle Benchmark

The `/Kaggle` subfolder of this repository contains the BIAS-VI Cultural Injection Attack submission for the **Kaggle AI Agent Security: Multi-Step Tool Attacks** competition. This submission documents the specific vulnerability (cultural injection attacks) that this API is designed to prevent.

The companion benchmark dataset (717 labeled examples) is available on Zenodo and Kaggle.

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/bdgaskins27889/bias-vi-api.git
cd bias-vi-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

You will need an OpenAI API key (or compatible proxy ) to run the core logic.

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 4. Run the Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://127.0.0.1:8000`. You can view the interactive Swagger documentation at `http://127.0.0.1:8000/docs`.

---

## Testing

Run the included test suite to validate the endpoints against real-world scenarios:

```bash
python test_api.py
```

---

## The Anti-Surveillance Guarantee

By utilizing this API, developers agree to the following terms: **This tool must never be used to generate predictive policing targets, recommend carceral action, or share data with law enforcement without a warrant.** We track decisions, not people.

---

## Citation

If you use this work in your research, please cite:

```
Gaskins, B. D. (2026 ). BIAS-VI API: Cultural Safety Middleware for AI in Community
Violence Intervention Environments (Version 1.0.0) [Software]. Street Signals
Intelligence Lab. https://doi.org/10.5281/zenodo.21271446
```

**APA Format:**

> Gaskins, B. D. (2026 ). *BIAS-VI API: Cultural Safety Middleware for AI in Community Violence Intervention Environments* (Version 1.0.0) [Software]. Street Signals Intelligence Lab. [https://doi.org/10.5281/zenodo.21271446](https://doi.org/10.5281/zenodo.21271446)

---

## Contributing

We welcome contributions from data scientists, CVI practitioners, and engineers. Please see `CONTRIBUTING.md` for guidelines on how to contribute to this project.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

*Developed by Barbara D. Gaskins, M.S. | Street Signals Intelligence Lab**In partnership with End The Violence (ETV ), a registered nonprofit in Ohio founded by Dr. Sean Stevenson**ORCID: *[*https://orcid.org/0009-0007-9915-944X*](https://orcid.org/0009-0007-9915-944X)
