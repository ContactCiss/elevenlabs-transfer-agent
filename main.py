import os
import requests
import json

# Je bestaande agent-ID
agent_id = "L2LOeYbvx1U1S71X8JWZ"
api_key = os.getenv("ELEVEN_API_KEY")

# ✅ Juiste endpoint om bestaande agent te updaten
url = f"https://api.elevenlabs.io/v1/agents/{agent_id}"

headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

# Payload met transfer_to_number tool
payload = {
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

# PATCH-aanroep om de agent bij te werken
response = requests.patch(url, headers=headers, data=json.dumps(payload))

# Log resultaat
if response.status_code == 200:
    print("✅ Agent succesvol geüpdatet met doorverbind-functionaliteit!")
else:
    print("❌ Fout bij updaten agent:")
    print("Status:", response.status_code)
    print("Antwoord:", response.text)
