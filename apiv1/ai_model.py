from transformers import LlamaForCausalLM, LlamaTokenizer

tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Llama-2-7b")
model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b", device_map="auto")


def generate_resume(data):
    
    prompt = f"""
    Create an ATS-friendly resume for the following details:

    Name: {data['name']}
    Role: {data['role']}
    Experience: {', '.join(data['experience'])}
    Education: {data['education']}
    Skills: {', '.join(data['skills'])}

    Format the resume with proper headings, bullet points, and concise details.
    """
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=512, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
