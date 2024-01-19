from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Main chat loop
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit' or 'bye'
    if user_input.lower() in ['exit', 'bye']:
        print("SimpleBot: Goodbye!")
        break

    # Get the chatbot's response
    response = chatbot.get_response(user_input)
    
    print(f"SimpleBot: {response}")
