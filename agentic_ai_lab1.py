import ollama

try:
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": "Explain the CIA Triad in cybersecurity."}
        ],
    )
    print(response["message"]["content"])
except Exception as e:
    print(f"An error occured: {e}")
    print("Please ensure the Ollama application is running.")
