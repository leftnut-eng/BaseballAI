import ollama
def chatCompletion(prompt: str):
    response = ollama.chat(
        model = "gemma3:4b",
        messages = [
            {"role": "system", "content": "you are a baseball coach"},
            {"role": "user", "content": prompt}
        ],
        options={
        'temperature': 0.7,
        'top_p': 0.9
        }
    )
    return response["message"]["content"]
print(chatCompletion(input("Enter Prompt: ")))