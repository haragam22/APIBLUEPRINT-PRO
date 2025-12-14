
# 🚀 APIBlueprint Pro

**Turn messy API documentation into production-ready Python SDKs using autonomous AI agents.**

---

## 📌 Overview

**APIBlueprint Pro** is an agentic system that converts incomplete, inconsistent, or ambiguous API documentation into **clean, usable Python SDKs** with tests, retry logic, and validation reports.

In the real world, API documentation is often messy — missing types, unclear schemas, undocumented error handling. Existing tools like OpenAPI generators fail unless the spec is perfect.

APIBlueprint Pro fixes this by **inferring, repairing, and validating API schemas automatically**.

---

## 🎯 Problem Statement

Developers waste hours understanding and fixing broken API docs before writing usable code.

Common issues:

* Missing field types
* Incomplete request/response schemas
* No error handling guidance
* Inconsistent formats (Markdown, README, cURL, Swagger)

**APIBlueprint Pro solves this end-to-end.**

---

## ✨ Key Features (Magic Layers)

### 🔥 Robust Schema Inference & Repair

* Infers missing types, timestamps, IDs
* Detects inconsistencies
* Auto-repairs broken schemas
* Flags ambiguities with confidence scores

### ⚠️ Error Intelligence Layer

* Detects 4xx / 5xx / 429 patterns
* Generates Python exception classes
* Adds retry & exponential backoff logic
* Produces workflow templates

### 🧠 Agent Mode (End-to-End)

A single command runs:

```
Summarize → Extract → Repair → Generate → Validate
```

Outputs:

* Python SDK
* Tests
* Validation report (`report.json`)

### 🌐 Multi-Format Input (60%+ Real-World Coverage)

Supports:

* Raw text docs
* Markdown
* OpenAPI / Swagger
* cURL examples
* README-style APIs
* URLs (fetched by local agent)

---

## 🏗️ Architecture

**Hybrid Runtime Model**

* **Local Python Agent**

  * Secure execution
  * SDK generation
  * Schema inference
  * Testing & validation

* **Vercel-Deployed Dashboard (Next.js)**

  * Input control (Text / URL)
  * Trigger agent execution
  * Visualize results (repairs, confidence, SDK preview)

This separation avoids cloud execution limits while delivering a polished UX.

---

## 🛠️ Tech Stack

* **Python** — Core agent pipeline
* **FastAPI** — Local agent API wrapper
* **Next.js (Vercel)** — Frontend dashboard
* **Cline CLI** — Autonomous execution
* **Kestra AI Agent** — API doc summarization
* **Oumi** — RLHF fine-tuning for schema extraction
* **CodeRabbit** — Automated PR reviews
* **Pytest** — Generated test validation

---

## 🧪 Demo Flow

1. Paste API docs (text or URL) in dashboard
2. Click **Generate Python SDK**
3. Agent runs locally
4. Dashboard updates with:

   * Repairs applied
   * Error intelligence
   * Confidence scores
   * Generated Python functions
5. Tests validate output

---

## 🎥 Demo Video

👉 **YouTube Demo:**
*https://youtu.be/Fy4M7q29VxI

---

## 🧩 Sponsor Integrations

### ✅ Cline

* Used to run the full agent pipeline autonomously via CLI
* Execution logs committed for verification

### ✅ Kestra

* AI Agent used to summarize large API documents before extraction
* Workflow YAML included

### ✅ Oumi

* Reinforcement Learning (RLHF) used to improve schema inference accuracy
* Tiny checkpoint included for demonstration

### ✅ CodeRabbit

* Enabled for automated PR reviews
* Demonstrates clean open-source workflow

---

## 📂 Project Structure

```
api-blueprint-pro/
├── cli.py
├── api_server.py
├── generator/
│   ├── parser.py
│   ├── inference.py
│   ├── repair.py
│   └── codegen.py
├── generated/
│   └── vehicle_alert/
│       ├── api_client.py
│       ├── errors.py
│       ├── retry_policy.py
│       ├── tests/
│       └── report.json
├── integrations/
│   ├── cline_task.yaml
│   ├── kestra_summarize.yaml
│   └── oumi_checkpoint/
├── vercel-ui/
└── README.md
```

---

## 📈 Learning & Growth

This project pushed boundaries in:

* Agent orchestration
* Schema inference under uncertainty
* Hybrid runtime architecture
* Practical use of RLHF in developer tooling
* Building production-ready outputs under hackathon constraints

---

## 🏁 Conclusion

**APIBlueprint Pro** is built for real developers, real APIs, and real pain points.

It doesn’t just generate code —
it **understands, repairs, and validates APIs like an experienced engineer**.

