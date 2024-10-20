import gc
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate


# LLM Service to Load, Interact and Unload Local LLMs
class LLMService:
    """
    A service to interact with a GGUF model using Llama.cpp and Langchain.
    """

    def __init__(self, model_path: str, model_desc: str, prompt_template: PromptTemplate):
        """
        Initialize the LLMService class.

        Args:
            model_path (str): The path to the GGUF model file.
            model_desc (str): Description of the model.
            prompt_template (PromptTemplate): A prompt template for generating model queries.
        """
        self.model_desc = model_desc
        self.prompt_template = prompt_template
        self._load_model(model_path=model_path)

    def _load_model(self, model_path: str):
        """
        Load the GGUF model using LlamaCpp.

        Args:
            model_path (str): The path to the GGUF model file.
        
        Raises:
            Exception: If there is an error during model loading.
        """
        try:
            # Callback manager for streaming the output
            callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

            # Load the LlamaCpp model with the specified configurations
            self.llm = LlamaCpp(
                model_path=model_path,
                callback_manager=callback_manager,
                n_ctx=512,           # Context window size
                n_threads=8,         # Number of CPU threads to use
                use_mlock=True,      # Lock the model in memory (if supported)
                n_gpu_layers=50,     # Number of layers to offload to GPU
                verbose=True         # Enable verbose output
            )
        except Exception as e:
            print(f"Error loading the model: {e}")
            raise

    def query(self, query: str) -> str:
        """
        Query the model with a given input.

        Args:
            query (str): The input text for the model to process.

        Returns:
            str: The generated response from the model.
        
        Raises:
            Exception: If there is an error during querying.
        """
        try:
            # Use the LlamaCpp model to generate a response based on the input query
            response = self.llm(query)
            return response
        except Exception as e:
            print(f"Error querying the model: {e}")
            return f"Rookie at work {e}"

    def unload(self):
        """
        Unload the model to free up resources.
        """
        del self.llm
        gc.collect()

