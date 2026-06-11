# test_openai.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if API key exists
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY not found in .env file")
    print("Please create a .env file with: OPENAI_API_KEY=your-key-here")
else:
    print(f"✅ OPENAI_API_KEY found (starts with: {api_key[:10]}...)")
    
    # Test the API
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input="Test message"
        )
        print("✅ OpenAI API connection successful!")
        print(f"Embedding dimension: {len(response.data[0].embedding)}")
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")