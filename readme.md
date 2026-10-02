# Build Local Instagram Profile Roasting Using Llama 3.1 (8b) (Ollama)

This tutorial guides you through setting up and running a local Instagram Profile Roasting web application powered by **FastAPI** on the backend, **Ollama** running **Llama 3.1:8b** as the LLM engine, and a standard HTML/CSS/JS frontend.

---

## Why Llama 3.1?

> For this release, Meta has evaluation the performance on over 150 benchmark datasets that span a wide range of languages. In addition, Meta performed extensive human evaluations that compare Llama 3.1 with competing models in real-world scenarios. Meta’s experimental evaluation suggests that our flagship model is competitive with leading foundation models across a range of tasks, including GPT-4, GPT-4o, and Claude 3.5 Sonnet. Additionally, Meta’s smaller models are competitive with closed and open models that have a similar number of parameters.

![Ollama benchmark](https://ollama.com/assets/mchiang0610/mikey3.1/2d582df5-ce45-4326-85c5-254c917554b2)


## Project Directory Structure

Ensure your project folder is structured as follows:

```text
project/
├── backend/
│   └── main.py
└── frontend/
    ├── index.html
    ├── style.css
    └── app.js
```

---

## Prerequisites & Model Information

* **AI Model:** Llama 3.1 (8b)
* **Model URL:** [Ollama Llama 3.1 Library](https://ollama.com/library/llama3.1:8b)

---

## Step 1: Environment Setup & Python Dependencies

Open your terminal in the root project directory and run the following commands to create a virtual environment and install the required dependencies (`fastapi`, `uvicorn`, and the `ollama` python package):


```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn ollama
```

---

## Step 2: Running the Services (Terminal Breakdown)

> ⚠️ **Important Note:** You must run **`ollama serve`**, the **Backend**, and the **Frontend** in **three (3) different terminal tabs** simultaneously.

### Terminal Tab 1: Initialize & Run Ollama Server
1. *(Make sure you have already pulled the model by running `ollama pull llama3.1:8b` beforehand if you haven't already).*
```bash
ollama pull llama3.1:8b
```

2. Start your local Ollama instance to serve the model:
```bash
ollama serve
```
   or more specific model:
```bash
ollama run llama3.1:8b
```

3. To see specific model currently running:
```bash
ollama list
```
### Terminal Tab 2: Run the FastAPI Backend
Activate your virtual environment and start the FastAPI development server:

```bash
source venv/bin/activate
uvicorn backend.main:app --reload
```
* **Backend URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000) or localhost:8000

### Terminal Tab 3: Run the Frontend Server
Navigate to the frontend directory and spin up a lightweight static HTTP server:

```bash
cd frontend
python -m http.server 5500
```
* **Frontend URL:** [http://127.0.0.1:5500](http://127.0.0.1:5500) or localhost:5500

---

## Step 3: Verify and Test

1. Open your browser and navigate to `http://127.0.0.1:5500`.
2. Interact with your frontend UI to send requests to your FastAPI backend, which will communicate locally with your Llama 3.1 instance!

Source: [Ollama Llama 3.1 Library](https://ollama.com/library/llama3.1:8b)