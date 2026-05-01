print("AI Chatbot 🤖")
print("Type 'exit' to stop the chat\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye! Keep learning AI 🚀")
        break

    elif "name" in user.lower():
        print("Bot: My name is AI Assistant.")

    elif "hello" in user.lower():
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user.lower():
        print("Bot: I am just code, but I'm doing great 🤖")

    else:
        print("Bot: I am still learning... 🤖")
