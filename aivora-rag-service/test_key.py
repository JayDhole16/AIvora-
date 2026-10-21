import os
from google import genai

# Set the API key
api_key = os.environ["GEMINI_API_KEY"]

print(f"Testing API key: {api_key[:20]}...")

try:
    client = genai.Client(api_key=api_key)
    print("✓ Client initialized successfully")
    
    # Try a simple API call
    response = client.models.list()
    print("✓ API call successful")
    print(f"Available models: {response}")
except Exception as e:
    print(f"✗ Error: {e}")
    print(f"Error type: {type(e).__name__}")
