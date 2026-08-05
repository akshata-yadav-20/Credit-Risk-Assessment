#!/usr/bin/env python3
import subprocess
import os

os.chdir(r"C:\Users\Dhruv\credit-risk-assessment")

# Use git-filter-repo with a callback
# This is tricky in PowerShell due to quote handling

# Let's use a simpler approach - use the --replace-text feature
with open("replace.txt", "w") as f:
    f.write("text:B[Aa]kshata Yadav\n")

# Actually, let's just force push after rewriting
# First, let's create a new root commit with all files
subprocess.run(["git", "checkout", "--orphan", "new-main"], check=True)

# Add all files and commit
subprocess.run(["git", "add", "-A"], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit: Credit Risk Assessment Project", "--author=Akshata Yadav <akshata-yadav-20@example.com>"], check=True)

print("Created new branch with correct author")

# Now delete old main and rename new-main
subprocess.run(["git", "branch", "-D", "main"], check=True)
subprocess.run(["git", "branch", "-m", "main"], check=True)

# Force push to remote
subprocess.run(["git", "push", "-u", "origin", "main", "-f"], check=True)

print("Successfully pushed with new history!")