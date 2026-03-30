# 01 — What is Agentic AI?

**Beginner Friendly Introduction & Quick Start**

📖 [Read the full article on Substack](https://learningagenticai.substack.com/p/what-is-agentic-ai)

## What You'll Learn

- The difference between Traditional AI and Agentic AI
- The 4 building blocks of any AI Agent: LLM, Tools, Memory, Loop
- How to build a simple agent from scratch using Python and Google Gemini

## How to Run

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey)

2. Install the dependency:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your API key in `agent_calculator.py` (replace the placeholder)

4. Run it:
   ```bash
   python agent_calculator.py
   ```

## What the Code Does

This is a bare-bones AI agent that:
- Takes your input
- Uses an LLM (Gemini) to **decide** if a calculation is needed (that's the reasoning)
- If yes, calls a calculator **tool** to get the answer (that's the tool use)
- If no, responds normally and nudges you toward what it's good at

That decision-making + tool use loop is the foundation of every agentic system.

## Try It Out

```bash
# Math question — agent uses the calculator tool
python agent_calculator.py
# Change the last line to: print(agent("What is 25 * 4 + 10?"))

# General question — agent responds and redirects
python agent_calculator.py
# Default: print(agent("How are you?"))
```
