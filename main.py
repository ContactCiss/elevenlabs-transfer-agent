import os
import requests
import json

# Haal je ElevenLabs API-sleutel op uit de environment
api_key = os.getenv("ELEVEN_API_KEY")

# Endpoint voor agent aanmaken
url = "https://api.elevenlabs.io/v1/agents"

# Headers voor authenticatie
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

# Payload met doorverbind-tool
payload = {
    "agent": {
        "prompt": {
            "prompt": "Je bent een behulpzame Nederlandse klantenservice-assistent. Als de klant vraagt om doorverbonden te worden, gebruik je de transfer_to_number tool.",
            "first_message": "Welkom bij Contactons! Waarmee kan ik je helpen?",
            "tools": [
                {
                    "type": "system",
                    "name": "transfer_to_number",
                    "description": "Verbind de gebruiker door naar een medewerker wanneer daarom wordt gevraagd.",
                    "params": {
                        "transfers": [
                            {
                                "phone_number": "+31884114114",
                                "condition": "Als de beller vraagt om doorverbonden te worden."
                            }
                        ]
                    }
                }
            ]
        }
    }
}

# Verstuur POST-verzoek
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Resultaat tonen
if response.status_code == 200:
    agent_data = response.json()
    print("✅ Agent succesvol aangemaakt!")
    print("Agent-ID:", agent_data.get("agent_id"))
else:
    print("❌ Fout bij aanmaken agent:")
    print("Status:", response.status_code)
    print("Antwoord:", response.text)
