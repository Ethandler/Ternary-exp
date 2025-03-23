from rodrick_ai import RodrickAI
import time

rodrick = RodrickAI()

print("\n--- Interactive Chat with RODRICK (type 'exit' to quit) ---")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = rodrick.think(user_input)
    print("RODRICK:", response)
    print("Memory recall:", rodrick.recall(user_input))
    print("Mood:", rodrick.mood)
    print("Emotion:", rodrick.emotional_response(user_input))

    # Logical analysis
    logic_analysis = rodrick.analyze_logic(user_input)
    print("Logical Analysis:", logic_analysis)

    # Training correction
    feedback = input("Type 'up' or 'down' to adjust memory, or press enter to skip: ")
    if feedback.lower() in ["up", "down"]:
        print(rodrick.user_feedback(user_input, feedback))

    print("-----")

print("oh fuck....RODRICK shutting down...")
