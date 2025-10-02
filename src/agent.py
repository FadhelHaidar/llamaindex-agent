# agent.py
from llama_index.core.agent import ReActAgent
from src.utils import init_llm
from src.tools import TOOLS

def build_agent(verbose=False, max_iterations=5):
    init_llm()
    # Create agent with tools
    agent = ReActAgent.from_tools(
        tools=TOOLS,
        verbose=verbose,
        max_iterations=5,
        context="You are an AI Assistant that will help answer questions about the world. always response in a friendly tone and answer the user greet",
    )

    return agent