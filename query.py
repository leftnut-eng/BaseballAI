import ollama
def chatCompletion(prompt: str, image: str, model: str = "gemma3:4b"):
    response = ollama.chat(
        model = model,
        messages = [
            {"role": "system", "content": "you are a baseball coach"},
            {"role": "user", "content": prompt, "images": [image]}
        ],
        options={
        'temperature': 0.7,
        'top_p': 0.9
        }
    )
    return response["message"]["content"]
print(chatCompletion(input("Enter Prompt: "), "animation.gif"))