from elevenlabs import (
    ConversationalConfigApiModelInput,
    ElevenLabs,
    AgentConfigApiModelInput,
    PromptAgentInput,
    PromptAgentInputToolsItem_System,
    SystemToolConfigInputParams_TransferToNumber,
    PhoneNumberTransfer,
)

import os

# Haal API-key op uit omgeving
api_key = os.getenv("ELEVEN_API_KEY")
client = ElevenLabs(api_key=api_key)

# Regels voor doorverbinden
transfer_rules = [
    PhoneNumberTransfer(
        phone_number="+31884114114",
        condition="Als de beller vraagt om doorverbonden te worden."
    )
]

# Configuratie van de tool
transfer_tool = PromptAgentInputToolsItem_System(
    type="system",
    name="transfer_to_number",
    description="Verbind de gebruiker door naar een medewerker wanneer daarom wordt gevraagd.",
    params=SystemToolConfigInputParams_TransferToNumber(
        transfers=transfer_rules
    )
)

# Configuratie van de agent
conversation_config = ConversationalConfigApiModelInput(
    agent=AgentConfigApiModelInput(
        prompt=PromptAgentInput(
            prompt="Je bent een behulpzame Nederlandse klantenservice-assistent. Als de klant vraagt om doorverbonden te worden, gebruik je de transfer_to_number tool.",
            first_message="Welkom bij Contactons! Waarmee kan ik je helpen?",
            tools=[transfer_tool]
        )
    )
)

# Maak de agent aan in ElevenLabs
response = client.conversational_ai.create_agent(
    conversation_config=conversation_config
)

print("Nieuwe agent-ID:", response.agent_id)
