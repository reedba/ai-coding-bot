import openai
import os
import subprocess

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code():
    """Generates Python code using OpenAI's API and writes it to a file."""
    prompt = "Generate a Python script that prints 'Hello, World!'"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    code = response["choices"][0]["text"]
    
    # Save the generated code to a fixed file
    output_file = "generated_script.py"
    with open(output_file, "w") as file:
        file.write(code)

    return output_file

def commit_and_push(filename):
    """Commits and pushes the generated file to GitHub."""
    subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"])
    subprocess.run(["git", "config", "--global", "user.email", "github-actions@github.com"])
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", "Updated generated script"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    file = generate_code()
    commit_and_push(file)