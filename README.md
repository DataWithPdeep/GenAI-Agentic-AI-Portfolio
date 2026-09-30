# 🤖 GenAI & Agentic AI Portfolio

Welcome to my **Generative AI & Agentic AI Portfolio**.

This repository contains practical AI projects built using **Python, LangChain, LangGraph, LLMs, APIs, Streamlit, and modern Generative AI techniques**.

The projects demonstrate how LLMs can be integrated with tools, APIs, databases, and external services to build practical AI applications.

---

## 🚀 Projects

| #  | Project                      | Description                                                                    |
| -- | ---------------------------- | ------------------------------------------------------------------------------ |
| 01 | 🤖 **AI Task Manager**       | AI-powered task management application using an intelligent agent and database |
| 02 | ✍️ **AI Blog Writer**        | Generative AI application for creating blog content using LLMs                 |
| 03 | 📧 **AI Email Agent**        | AI agent for assisting with email-related tasks and automation                 |
| 04 | 🌤️ **Search Weather Agent** | AI agent that searches and provides weather information using external APIs    |

---

## 📂 Repository Structure

```text
GenAI-Agentic-AI-Portfolio/
│
├── AiTaskManger/
│   ├── agent.py
│   ├── app.py
│   ├── tools.py
│   ├── databse.py
│   └── ...
│
├── Blog_Writter/
│   └── ...
│
├── Email_agent/
│   └── ...
│
├── Search_Weather_Agent/
│   └── ...
│
├── basic_langchain.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Technologies & Skills

### Generative AI

* Large Language Models (LLMs)
* Prompt Engineering
* Generative AI Applications
* AI Agents
* Tool Calling

### AI Frameworks

* LangChain
* LangGraph

### Programming

* Python

### Application Development

* Streamlit
* API Integration
* Database Integration

### Other Technologies

* SQLAlchemy
* SQLite
* REST APIs
* Environment Variables
* Git & GitHub

---

## 🔥 Key Concepts Demonstrated

* LLM-powered applications
* Agentic AI workflows
* Tool-based AI agents
* Function/tool calling
* API integration
* Database operations
* Prompt engineering
* State-based AI workflows
* AI automation
* Streamlit application development

---

## 🏗️ AI Agent Workflow

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    AI Agent     │
                    │   LangChain /   │
                    │    LangGraph    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   LLM / Model   │
                    └────────┬────────┘
                             │
                 ┌───────────┼───────────┐
                 ▼           ▼           ▼
             Database       Tools       APIs
                 │           │           │
                 └───────────┼───────────┘
                             ▼
                    ┌─────────────────┐
                    │     Result      │
                    └─────────────────┘
```

---

## 📌 Project Details

### 01. AI Task Manager

An AI-powered task management application where an AI agent can interact with tasks and perform operations through tools.

**Core Concepts:**

* AI Agent
* LangChain / LangGraph
* Tool Calling
* CRUD Operations
* SQLAlchemy
* SQLite
* Streamlit

---

### 02. AI Blog Writer

A Generative AI application designed to assist users in generating blog content using an LLM.

**Core Concepts:**

* Generative AI
* Prompt Engineering
* LLM
* Content Generation
* Python

---

### 03. AI Email Agent

An AI-powered application focused on assisting with email-related workflows and automation.

**Core Concepts:**

* AI Agent
* LLM
* Tool Calling
* Email Automation
* API Integration

---

### 04. Search Weather Agent

An AI agent that can interact with external weather/search services to retrieve useful information for the user.

**Core Concepts:**

* Agentic AI
* Tool Calling
* API Integration
* External Data Retrieval
* LLM

---

## 📓 Learning & Experiments

The repository also contains `basic_langchain.ipynb`, which includes experiments and learning examples related to LangChain and Generative AI concepts.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/DataWithPdeep/GenAI-Agentic-AI-Portfolio.git
```

Navigate into the project:

```bash
cd GenAI-Agentic-AI-Portfolio
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file and add the required API keys for the individual projects.

Example:

```env
GROQ_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```

**Never commit API keys or `.env` files to GitHub.**

---

## 🎯 Portfolio Objective

The goal of this repository is to demonstrate practical experience in building **Generative AI and Agentic AI applications** using modern AI frameworks and real-world integrations.

The projects focus on moving beyond simple LLM prompts toward applications that can **reason, use tools, interact with external systems, and perform useful tasks**.

---

## 👨‍💻 About Me

**Pradeep Singh**

AI/ML | Generative AI | Agentic AI | MLOps | Python

Interested in building practical AI applications and production-oriented machine learning systems.

---

## 📫 Connect

* GitHub: **DataWithPdeep**


---

## ⭐ Support

If you find these projects useful, consider giving this repository a ⭐.

Thanks for visiting! 🚀
