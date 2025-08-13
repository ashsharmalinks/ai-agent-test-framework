# 🤖 AI Agent Test Framework
---

## 📌 Overview

This project is a **full-stack AI Agent testing framework** featuring:

- 🚀 **FastAPI** backend to interact with the AI Agent.
- 🧪 **Pytest** & **Behave (BDD)** automated tests.
- 🛠 **Custom tools** for search, math, and retrieval.
- 📊 **Cost tracking** and latency monitoring.
- 🎨 **Minimal UI** for quick manual testing.
- 📜 **Allure Reports** for rich test results.

---

## 🛠 Tech Stack

| Category        | Tools |
|-----------------|-------|
| Backend         | FastAPI, Uvicorn |
| Testing         | Pytest, Behave, Allure |
| Agent           | DeterministicMockLLM, SearchTool, MathTool, RetrievalTool |
| Language        | Python 3.12+ |
| Packaging       | pip + virtualenv |
| Reporting       | Allure |

---

## 📦 Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-agent-test-framework.git
cd ai-agent-test-framework

# 2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3️⃣ Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶ Running the Server

```bash
uvicorn src.server.main:app --reload
```

**Check health:**
```bash
curl http://127.0.0.1:8000/health
```

---

## 💻 Open the UI

After starting the server, open in your browser:
```
http://127.0.0.1:8000/
```
Example queries:
- `What is 2+2?`
- `capital of France`
- `Tell me about the sun`
- `tool:retrieval: safety checks in agents`

---

## 🧪 Running Tests

### Run Pytest
```bash
pytest -v
```

### Run Behave BDD
```bash
behave
```

### Run All Tests + Generate Allure Report
```bash
./run_all_tests.ps1    # Windows PowerShell
# OR
bash run_all_tests.sh  # Mac/Linux
```

---

## 📊 Viewing Allure Report

After running `run_all_tests`, the Allure report will be generated.

To view:
```bash
allure serve allure-results
```

---

## 📂 Project Structure

```
ai-agent-test-framework/
│── src/
│   ├── agent/              # Core agent logic & tools
│   ├── common/             # Utilities & factories
│   ├── server/             # FastAPI app
│── tests/                  # Pytest tests
│── features/               # Behave BDD features
│── run_all_tests.ps1       # Full test runner (Windows)
│── run_all_tests.sh        # Full test runner (Mac/Linux)
│── requirements.txt        # Python dependencies
│── README.md               # This file
```

---

## 🏆 Key Features

- **🔍 SearchTool** – Answers using predefined search routes.
- **➗ MathTool** – Solves basic math queries.
- **📚 RetrievalTool** – Retrieves knowledge from stored docs.
- **⏱ Cost & Latency Tracking** – Ensures performance visibility.
- **🖥 Simple UI** – Test from browser instantly.
- **✅ Automated Testing** – Pytest + Behave + Allure.



> ⚡ Developed for robust AI agent testing with **speed**, **clarity**, and **automation** in mind.
