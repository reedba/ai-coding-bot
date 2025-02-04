REM filepath: /C:/Users/brand/OneDrive/Desktop/AI_Projects/ai-coding-bot/run_job.bat
@echo off

REM Navigate to the project directory
cd C:\Users\brand\OneDrive\Desktop\AI_Projects\ai-coding-bot

REM Run the Python script
python generate_code.py

REM Commit and push changes
git config --global user.name "reedba"
git config --global user.email "rdsfence@gmail.com"
git add generated_script.py
git commit -m "Updated generated script with windows"
git push