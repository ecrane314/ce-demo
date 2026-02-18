
import asyncio

from google.genai import types
from google.adk.agents import Agent
from vertexai.agent_engines import AdkApp
 

async def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "EUR",
    currency_date: str = "latest",
):
    """Retrieves the exchange rate between two currencies on a specified date.

    Uses the Frankfurter API (https://api.frankfurter.app/) to obtain
    exchange rate data.

    Args:
        currency_from: The base currency (3-letter currency code).
            Defaults to "USD" (US Dollar).
        currency_to: The target currency (3-letter currency code).
            Defaults to "EUR" (Euro).
        currency_date: The date for which to retrieve the exchange rate.
            Defaults to "latest" for the most recent exchange rate data.
            Can be specified in YYYY-MM-DD format for historical rates.

    Returns:
        dict: A dictionary containing the exchange rate information.
            Example: {"amount": 1.0, "base": "USD", "date": "2023-11-24",
                "rates": {"EUR": 0.95534}}
    """
    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()



"""Develop an agent for Vertex agent engine"""
model = "gemini-2.5-flash"


async def main():
    ''' DEPLOY TO AGENT ENGINE https://docs.cloud.google.com/agent-builder/agent-engine/deploy
        or deploy to local environment
    '''

    generate_content_config = types.GenerateContentConfig(
    # safety_settings=safety_settings,
    temperature=0.25,
    max_output_tokens=1000,
    top_p=0.95,
    )
  
    # Construct the agent
    # from google.adk.agents import Agent
    agent = Agent(
        model=model,                                      # Required.
        name='currency_exchange_agent',                   # Required.
        tools=[get_exchange_rate],                        # Optional.
        generate_content_config=generate_content_config,  # Optional.
        # requirements = "./requirements.txt",
        # min_instances=1,
    )

    # Construct the LOCAL ADK App
    # from vertexai.agent_engines import AdkApp
    app = AdkApp(agent=agent)

    # Construct REMOTE ADK Agent Engine app
    # from vertexai.agent_engines import AdkApp
    # https://docs.cloud.google.com/agent-builder/agent-engine/deploy#create-agent-engine
    client = app.agent_engines.client()
    remote_agent = client.agent_engines.create(
    agent=agent,
    config={
        "min_instances": 1,
        "max_instances": 10,
        "resource_limits": {"cpu": "4", "memory": "8Gi"},
        "container_concurrency": 9,
        }
    )

    async for event in app.async_stream_query(
        user_id="eac-user",  # Required
        message="What is the exchange rate from US dollars to Swedish currency?",
        ):
        print(event)

if __name__ == "__main__":
    asyncio.run(main())