import asyncio
import os
from google import genai
from google.genai import types

api_key = os.environ["GEMINI_API_KEY"]

async def test_model():
    client = genai.Client(api_key=api_key)
    
    try:
        print("Testing gemini-2.5-flash model...")
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello, this is a test",
            config=types.GenerateContentConfig(
                system_instruction="You are a test assistant",
                temperature=0.1,
            ),
        )
        print(f"✓ Success: {response.text[:100]}")
    except Exception as e:
        print(f"✗ Error: {e}")
        print(f"Error type: {type(e).__name__}")

asyncio.run(test_model())
