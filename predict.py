from cog import BasePredictor, Input
import os
import torch
import shutil
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda"

class Predictor(BasePredictor):
    def setup(self):
        name = 'mosaicml/mpt-30b-chat'
        MODEL_CACHE = "diffusers-cache"

        if os.path.exists(MODEL_CACHE):
            shutil.rmtree(MODEL_CACHE)
        os.makedirs(MODEL_CACHE, exist_ok=True)

        self.tokenizer = AutoTokenizer.from_pretrained(
            name,
            cache_dir=MODEL_CACHE
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            name, 
            load_in_8bit=True,
            cache_dir=MODEL_CACHE
        )

    def predict(self,
        prompt: str = Input(description="Instruction for the model"),
        max_new_tokens: int = Input(description="max tokens to generate", default=64)
    ) -> str:    
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(device)
        outputs = self.model.generate(
            inputs, 
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id)
        output = self.tokenizer.decode(outputs[0])
        return output
    