import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# langchain支持deepseek以model identifier string方式声明（需要在.env中配置DEEPSEEK_API_KEY），考虑到调用成本，改用免费的model
# agent = create_agent(
#     model = "deepseek-chat",
#     tools = [get_weather],
#     system_prompt = "You are a helpful assistant",
# )

model = ChatOpenAI(
    model="qwen-max",
    temperature=0.1,
    max_tokens=1000,
    timeout=30,
    api_key=os.getenv('API_KEY'),
    base_url=os.getenv('BASE_URL')
)
agent = create_agent(
    model,
    tools = [get_weather],
    system_prompt = "You are a helpful assistant",
)

if __name__ == "__main__":
    # Run the agent
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
        )
    print(result)