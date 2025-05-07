import os
import requests

agent_id = "L2LOeYbvx1U1S71X8JWZ"
api_key = os.getenv("ELEVEN_API_KEY")

url = f"https://api.elevenlabs.io/v1/conversational/agents/{agent_id}"

headers = {
    "xi-api-key": api_key
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.text)
