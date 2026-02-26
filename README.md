# 🤖 Local AI Agentic Framework: Autonomous Software Dev Team

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-1.9.3-orange.svg)](https://www.crewai.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black.svg)](https://ollama.ai/)

An autonomous, 100% local, and privacy-first multi-agent framework powered by **CrewAI** and **Ollama (Qwen2.5-Coder:3b)**. This project demonstrates how to engineer small-parameter local LLMs into a highly disciplined, specialized software engineering team capable of writing, testing, and documenting complex code without relying on paid APIs.

## 🌟 Why This Project?
Running LLMs locally ensures complete data privacy and zero API costs. However, smaller models often struggle with cognitive load, formatting errors, and repetition collapse. This framework solves these issues by utilizing strict system prompts, `max_iter` safeguards, memory isolation, and structural boundaries to force the models into perfect compliance.

---

## 👥 The Agent Roster

The framework orchestrates three distinct AI agents working sequentially:

* **🏗️ Senior Python Architect:** Focuses purely on optimal algorithms, Big-O complexity, and Clean Code principles (e.g., Type Hinting).
* **🛡️ QA & Security Expert:** A highly strict defensive programming agent. It actively searches for edge cases (network timeouts, empty data, memory leaks) and wraps the architect's code in robust `try-except` blocks.
* **📝 Technical Documentation Robot:** Operates with zero creativity to strictly format the final, secure code into a professional Markdown template without hallucinations.

---

## 🚀 Installation & Setup

Ensure you have [Ollama](https://ollama.ai/) installed on your system. Then, run the following commands sequentially to clone the repo, install dependencies, start the model, and launch the AI team:

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
pip install -r requirements.txt
ollama run qwen2.5-coder:3b
python Agents.py

#🎯 Usage Example
Once the terminal interface starts, simply assign a task:

Prompt: > Write an advanced web scraper that extracts Premier League match statistics. It must include dynamic User-Agent rotation and robust error handling against timeouts and missing HTML tags.

Result: The agents collaborate (Architecture Design -> Security Testing -> Documentation) and output highly optimized, type-hinted Python code wrapped in strict try-except blocks, fully documented in Markdown.

#🗺️ Roadmap
[ ] v1.1: Integration of web search capabilities for agents to read up-to-date API documentations and library changes.

[ ] v2.0: Expanding the framework to support multiple programming languages (Java, C++, Go) with language-specific validation agents.

[ ] v2.1: A Graphical User Interface (GUI) using Streamlit for an easier code testing environment.

Developed by Gökmen — Exploring the intersection of Local LLMs, Autonomous Agents, and Software Engineering.
