from src.agent import build_agent

agent = build_agent(max_iterations=10, verbose=True)

if __name__ == "__main__":
    
    chat_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        agent_response = agent.chat(user_input)
        print("Agent:", agent_response.response)
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": agent_response.response})