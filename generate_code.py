import openai
import os
import subprocess
from datetime import datetime

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code():
    """Generates Python code using OpenAI's API."""
    prompt = "Generate a Python script that prints 'Hello, World!'"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    code = response["choices"][0]["message"]["content"]
    
    # Save the generated code
    filename = f"generated_code_{datetime.now().strftime('%Y-%m-%d')}.py"
    with open(filename, "w") as file:
        file.write(code)

    return filename

def commit_and_push(filename):
    """Commits and pushes the generated code to GitHub."""
    subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"])
    subprocess.run(["git", "config", "--global", "user.email", "github-actions@github.com"])
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"Auto-generated code {filename}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    file = generate_code()
    commit_and_push(file)
