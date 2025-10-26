from collections import deque

class ChatMemory:
    """
    Manages conversation history with a sliding window.
    """
    def __init__(self, window_size: int = 3):
        self.window_size = window_size
        self.history = deque(maxlen=window_size)

    def add_exchange(self, user_input: str, bot_response: str):
        """
        Adds a new user-bot exchange to the history.
        """
        self.history.append((user_input, bot_response))

    def get_context(self):
        """
        Builds the context string from history.
        """
        prompt = ""
        for user, bot in self.history:
            prompt += f"User: {user}\nBot: {bot}\n"
        return prompt
