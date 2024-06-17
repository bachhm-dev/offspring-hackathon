# Description: This file contains the code to perform face swap using InsightFace library.
# Live Coding 3D Face Analysis with InsightFace

# pip install insightface==0.7.3

# pip install onnxruntime

# pip install gdown

import torch
import transformers

from transformers import LlamaForCausalLM, LlamaTokenizer
from dotenv import load_dotenv
import os
import os.path as osp

load_dotenv()

# model_dir = "./models/final/"
model_dir = os.environ.get('MODEL_LOCAL_PATH')
print(model_dir)
model = LlamaForCausalLM.from_pretrained(model_dir)

tokenizer = LlamaTokenizer.from_pretrained(model_dir)
def generate_text(prompt):

  pipeline = transformers.pipeline(
  "text-generation",
  model=model,
  tokenizer=tokenizer,
  torch_dtype=torch.float16,
  device_map="auto",
  )
  sequences = pipeline(
  prompt,
  do_sample=True,
  top_k=10,
  num_return_sequences=1,
  eos_token_id=tokenizer.eos_token_id,
  max_length=400,
  truncation=True
  )

  # Convert generated text to a string array
  generated_text_array = [seq['generated_text'] for seq in sequences]
  print(generated_text_array)

  for seq in sequences:
    print(f"{seq['generated_text']}")

  # Convert generated text to a string array
  generated_text_array = [seq['generated_text'] for seq in sequences]
  print(generated_text_array)

  return generated_text_array

  

