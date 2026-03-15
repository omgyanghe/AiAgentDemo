from agent import Agent

agent = Agent()

while True:

    task = input("\nUser: ")

    result = agent.run(task)

    print("\nResult:", result)