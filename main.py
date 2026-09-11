import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable is not set")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ],
)

usage = response.usage
if usage is None:
    raise RuntimeError("Response did not contain token usage information")

print(f"Completion tokens: {usage.completion_tokens}")
print(f"Prompt tokens: {usage.prompt_tokens}")
print(f"Response tokens: {usage.completion_tokens}")
print(f"Total tokens: {usage.total_tokens}")

print(response.choices[0].message.content)
