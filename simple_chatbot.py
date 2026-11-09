def simple_chatbot():
    print("🤖 Chatbot: Hello! (Baat khatam karne ke liye 'bye' type karein)")
    
    while True:
        # User input lena aur extra spaces/uppercase ko handle karna
        user_input = input("You: ").strip().lower()
        
        # Rule-based replies using if-elif
        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
            break  # Loop ko rokne ke liye jab user 'bye' bole
        else:
            print("🤖 Chatbot: Mujhe samajh nahi aaya. Aap 'hello', 'how are you', ya 'bye' try karein.")

if __name__ == "__main__":
    simple_chatbot()