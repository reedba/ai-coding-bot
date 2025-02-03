import openai
import os
import subprocess

# Load API key from environment variables
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
    
    # Save the generated code to a fixed file
    output_file = "generated_script.py"
    with open(output_file, "w") as file:
        file.write(code)

    # Debugging: Confirm the file was written
    with open(output_file, "r") as file:
        print("File content:", file.read())

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