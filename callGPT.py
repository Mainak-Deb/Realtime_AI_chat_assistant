import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def call_gpt4o_mini(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[{"role": "user", "content": prompt}],
        text={"format": {"type": "text"}},
        reasoning={},
        tools=[],
        temperature=0.7,
        max_output_tokens=2048,
        top_p=1,
        store=False  # Change to True if you want to store responses
    )
    if response.output and response.output[0].content:
        return response.output[0].content[0].text  # Extract text content
    
    return "No response received."

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    output = call_gpt4o_mini(user_prompt)
    print("\nGPT-4o-mini Response:\n", output)
