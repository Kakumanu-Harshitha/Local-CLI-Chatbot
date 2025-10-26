from transformers import pipeline
import torch

class ModelLoader:
    """
    Loads a Hugging Face text-generation pipeline.
    """
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.device = 0 if torch.cuda.is_available() else -1
        self.chatbot_pipeline = None
        print(f"Loading model '{self.model_name}' on device: {'GPU' if self.device == 0 else 'CPU'}")

    def load(self):
        """
        Loads the text-generation pipeline.
        """
        try:
            self.chatbot_pipeline = pipeline(
                "text-generation",
                model=self.model_name,
                tokenizer=self.model_name,
                device=self.device
            )
            print("Text-generation pipeline loaded successfully.")
        except Exception as e:
            print(f"Error loading pipeline: {e}")
            raise

    def get_pipeline(self):
        """
        Returns the loaded pipeline instance.
        """
        if self.chatbot_pipeline is None:
            self.load()
        return self.chatbot_pipeline
