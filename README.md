# 🧹 GitHub Repo Cleaner

A Flask web app to help you clean up your GitHub account by listing your personal and forked repositories separately. Select the ones you want to delete and hit the button. Useful for managing long-forgotten forks.

## ⚙️ Features

- Lists both personal and forked repositories
- Checkboxes for selecting which to delete
- Uses GitHub API securely with your token

## 🔐 Security

Your GitHub token is stored in the script for now. For production, use environment variables or `.env`.


## 🔐 To generate a secure secret_key for your Flask application, you can use Python’s built-in libraries to create a random string.
Open a terminal or Python shell and run:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Example output:
4a1f3c5a1b913f66e5cfbf8a1e4bfb4e1a03e8760e3f271aebc3f77d8e5fc22b

## 🔐 GitHub Token Setup
Generate a [Personal Access Token](https://github.com/settings/tokens) with the following scopes:
- repo (Full control of private repositories)
- delete_repo (Permission to delete repositories)

## 🚀 Getting Started
```bash
pip install -r requirements.txt
```
🧪 Run the App
```bash
python app.py
```
Open in your browser:
http://127.0.0.1:5000/


![2025-07-06_000030](https://github.com/user-attachments/assets/f2f1cba5-2761-48ad-97d9-1eee52b99855)
