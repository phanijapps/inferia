import gc
from logging import warn
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import llamacpp
from langchain.prompts import PromptTemplate



class LLMService:

    def __init__(self, model_path, model_desc, prompt_template):
        """Constuctor for initialization"""
        self._load_model(self,model_path)

        self.model_desc = model_desc:warn()
        self.prompt_template = prompt_template

    def _load_model(self, model_path):
        """Load Selected Model"""
        self.llm = Llama(model_path = model_path,
                         use_mlock=True,
                         n_threads=8,
                         use_gpu=True,
                         n_gpu_layers=50,
                         n_ctx=512)

    def query(self,query):
        """Question the model"""
        response = self.llm(prompt=query)
        return response['choices'][0]['text']



    def unload(self):
        """Unload model"""
        del self.llm
        gc.collect()

