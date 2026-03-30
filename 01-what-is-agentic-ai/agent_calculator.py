"""
Agentic AI — Beginner Calculator Agent
=======================================
A simple agent that decides whether your input needs a calculation,
and if it does, uses a tool (calculator function) to get it done.

Article: What is Agentic AI? — Beginner Friendly Introduction & Quick Start
Author: Daniel D'souza
"""

from google import genai

# Get your API key from Google AI Studio: https://aistudio.google.com/apikey
client = genai.Client(api_key="YOUR_API_KEY_HERE")


# --- TOOL: Calculator ---
def calculator_tool(expression):
    """A simple calculator tool the agent can use."""
    try:
        return eval(expression)
    except:
        return "Error in calculation"


# --- AGENT ---
def agent(user_input):
    print(f"User: {user_input}")

    # Step 1: Ask the LLM what to do (REASONING)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You are an AI agent.

        Decide if this task requires calculation.

        User input: {user_input}

        If calculation is needed, respond with:
        ACTION: CALCULATE <expression>

        Otherwise respond normally.
        """
    )

    decision = response.text.strip()
    print(f"Agent thinking: {decision}")

    # Step 2: Use the tool if needed (ACTION)
    if "ACTION: CALCULATE" in decision:
        expression = decision.split("CALCULATE")[-1].strip()
        result = calculator_tool(expression)
        return f"Result: {result}"
    else:
        return f"{decision} \n I am an agent designed for Mathematical Calculations, I can help you better with a Math Calculation."


# --- RUN ---
if __name__ == "__main__":
    # Try a math question:
    # print(agent("What is 25 * 4 + 10?"))

    # Try a general question:
    print(agent("How are you?"))
