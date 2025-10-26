import argparse
from model_loader import ModelLoader
from chat_memory import ChatMemory

def main():
    parser = argparse.ArgumentParser(description="A local command-line chatbot.")
    parser.add_argument(
        "--model",
        type=str,
        default="facebook/blenderbot-400M-distill",
        help="The Hugging Face text-generation model to use."
    )
    parser.add_argument(
        "--window",
        type=int,
        default=3,
        help="The sliding window size for conversation memory."
    )
    args = parser.parse_args()

    print("--- Initializing Chatbot ---")
    model_loader = ModelLoader(model_name=args.model)
    chatbot = model_loader.get_pipeline()
    memory = ChatMemory(window_size=args.window)

    print("\n--- Chatbot is now running ---")
    print("Type your message and press Enter. Type '/exit' to quit.")

    while True:
        try:
            user_input = input("User: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting chatbot. Goodbye!")
            break

        if user_input.lower() == '/exit':
            print("Exiting chatbot. Goodbye!")
            break

        # Build context for prompt
        context = memory.get_context()
        prompt = f"{context}User: {user_input}\nBot:"

        try:
            response = chatbot(prompt, max_new_tokens=100)
            if not response or "generated_text" not in response[0]:
                bot_reply = "Sorry, no response generated."
            else:
        # Extract only bot reply (after the prompt)
                full_generated = response[0]['generated_text'].strip()
                bot_reply = full_generated[len(prompt):].strip()
        # Fallback if bot_reply is empty
            if not bot_reply:
                bot_reply = full_generated
        except Exception as e:
            bot_reply = f"Sorry, an error occurred: {e}"

        print(f"Bot: {bot_reply}")
        memory.add_exchange(user_input, bot_reply)

if __name__ == "__main__":
    main()
