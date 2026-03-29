from agent.agent import Agent

agent = Agent()

while True:

    task = input("User: ")

    result = agent.run(task)

    print("Agent:", result)