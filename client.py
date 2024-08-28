"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""


import os
import google.generativeai as genai

# Configure the API key using an environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configuration for the model generation
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

# Create the model with the specified configuration
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(
  history=[]  # Initial chat history (empty)
)

# Send a message to the model
response = chat_session.send_message("What is java?")

# Print only the content of the response
print(response.text)