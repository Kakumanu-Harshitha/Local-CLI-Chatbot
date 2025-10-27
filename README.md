# 🗨️ Local Command-Line Chatbot

A simple and lightweight command-line chatbot built using **Hugging Face’s `facebook/blenderbot-400M-distill`** model.  
It maintains short-term conversational memory and generates context-aware responses directly from your local system — no internet API calls needed!

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Kakumanu-Harshitha/local-chatbot.git
   cd local-chatbot
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv local_chatbot
   ```

3. **Activate the environment**  
   - **Windows:**  
     ```bash
     local_chatbot\Scripts\activate
     ```
   - **macOS/Linux:**  
     ```bash
     source local_chatbot/bin/activate
     ```

4. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run

Run the chatbot from your terminal:

```bash
python chatbot.py
```

Optional arguments:
- `--model` → change the model (default: `facebook/blenderbot-400M-distill`)
- `--window` → adjust memory window size (default: 3)

Example:
```bash
python chatbot.py --model facebook/blenderbot-400M-distill --window 5
```

When running, type your message and press **Enter**.  
To stop chatting, type `/exit`.

---

## 💬 Sample Interaction

```
--- Chatbot is now running ---
Type your message and press Enter. Type '/exit' to quit.

User: Hi there!
Bot: Hello! How are you doing today?

User: I’m learning about AI chatbots.
Bot: That’s awesome! Chatbots are a great way to explore conversational AI.

User: /exit
Exiting chatbot. Goodbye!
```

---

## 📘 Project Overview

This chatbot project includes three main modules:

- **model_loader.py** → Loads the Hugging Face model and tokenizer.  
- **chat_memory.py** → Manages short-term conversation memory using a deque.  
- **interface.py** → Handles user interaction and message flow.

---

## 🙌 Conclusion

This project demonstrates how a small conversational AI model can run locally, maintaining short-term context and producing natural responses.  
I’m excited to share this as part of my internship application and would love the opportunity to contribute to your global AI initiatives!
