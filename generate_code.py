import openai
import os
from dotenv import load_dotenv

# Load API key from .env file or environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code():
    """Generates Python code using OpenAI's API and writes it to a file."""
    prompt = "I am currently working on learning DSA and need you to act as my tutor. I need you to create a new DSA problem with explanation and solution within python. Lets start wit strings and arrays"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    code = response["choices"][0]["message"]["content"]
    
    # Debugging: Print the response to ensure it's correct
    print("Generated code:", code)
    
    # Save the generated code to a fixed file with UTF-8 encoding
    output_file = "generated_script.py"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(code)

    # Debugging: Confirm the file was written
    with open(output_file, "r", encoding="utf-8") as file:
        print("File content:", file.read())

    return output_file

if __name__ == "__main__":
    generate_code()