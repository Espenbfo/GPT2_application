USE_GPU = True
# Bare nødvendig i visse versjoner av tensorflow
if USE_GPU:
    import tensorflow as tf
    physical_devices = tf.config.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

from transformers import pipeline, set_seed, GPT2Tokenizer
generator = pipeline('text-generation', model='gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#set_seed(42)

def generate_text(text, tokens_pr_generation=20):
    encoded_input = tokenizer(text, return_tensors='tf')
    length = len(encoded_input["input_ids"][0])
    return generator(text, max_length=length+tokens_pr_generation, num_return_sequences=1)[0]["generated_text"]
