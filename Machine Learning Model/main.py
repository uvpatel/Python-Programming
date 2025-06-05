from phi.agent import Agent
from phi.model.groq import Groq
# If Groq is not available, use a supported model import or install the required package.
# Example fallback (update as needed):
# from phi.model.openai import OpenAI as Groq

# Create the agent
agent = Agent(
    description="You are a helpful AI assistant.",
    instructions=["Answer questions clearly and helpfully."],
    model=Groq(id="llama3-8b-8192"),  # Or use llama3-70b-8192 if you have access
    markdown=True,
    debug_mode=True
)

# Input prompt
user_input = "What is the capital of Japan?"

# Print agent's response
while True:
    prompt = input("You: ")
    agent.print_response(prompt, stream=True)

