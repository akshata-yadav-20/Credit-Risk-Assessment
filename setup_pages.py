#!/usr/bin/env python3
"""
This script creates a gh-pages branch with the demo site pre-built.
"""
import subprocess
import os
import shutil

os.chdir(r"C:\Users\Dhruv\credit-risk-assessment")

# Remove existing gh-pages branch if it exists locally
subprocess.run(["git", "branch", "-D", "gh-pages"], 
               stdout=subprocess.DEVNULL, 
               stderr=subprocess.DEVNULL)

# Create orphan branch
subprocess.run(["git", "checkout", "--orphan", "gh-pages"], check=True, 
               capture_output=True, text=True)

# Create docs folder with index.html
os.makedirs("docs", exist_ok=True)
shutil.copy("app/templates/index.html", "docs/index.html")
with open("docs/.nojekyll", "w") as f:
    f.write("")

# Remove everything except docs
files_to_remove = [
    ".github", "app", "ml", "data", "models",
    "LICENSE", "README.md", "demo.html", "deploy_demo.py",
    "index.md", "pyproject.toml", "requirements.txt", "run.py",
    "vercel.json", "repo-config.json"
]

for item in files_to_remove:
    if os.path.exists(item):
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.remove(item)

# Add everything and commit
subprocess.run(["git", "add", "-A"], check=True)
subprocess.run(["git", "commit", "-m", "Deploy to GitHub Pages"], 
               env={**os.environ, "GIT_AUTHOR_NAME": "Akshata Yadav", 
                    "GIT_AUTHOR_EMAIL": "akshata-yadav-20@example.com"}, check=True)

# Push to gh-pages branch
subprocess.run(["git", "push", "-u", "origin", "gh-pages", "-f"], check=True)

# Switch back to main
subprocess.run(["git", "checkout", "main"], check=True)

print("✓ gh-pages branch created and pushed successfully!")
print("URL: https://akshata-yadav-20.github.io/Credit-Risk-Assessment/")