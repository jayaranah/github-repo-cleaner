from flask import Flask, render_template, request, redirect, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Use secrets.token_hex(32) in production

# GitHub credentials
GITHUB_USERNAME = 'your_username'
GITHUB_TOKEN = 'your_personal_access_token'

HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {GITHUB_TOKEN}'
}

def get_repositories():
    repos = []
    page = 1
    while True:
        url = f'https://api.github.com/user/repos?per_page=100&page={page}'
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def delete_repository(full_name):
    url = f'https://api.github.com/repos/{full_name}'
    response = requests.delete(url, headers=HEADERS)
    return response.status_code == 204

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_repos = request.form.getlist('repos')
        deleted = []
        failed = []

        for repo in selected_repos:
            success = delete_repository(repo)
            if success:
                deleted.append(repo)
            else:
                failed.append(repo)

        flash(f"Deleted: {', '.join(deleted)}" if deleted else "No repositories deleted.", "success")
        if failed:
            flash(f"Failed to delete: {', '.join(failed)}", "danger")
        return redirect('/')

    all_repos = get_repositories()
    personal_repos = [r for r in all_repos if not r.get('fork')]
    forked_repos = [r for r in all_repos if r.get('fork')]

    return render_template('index.html', personal_repos=personal_repos, forked_repos=forked_repos)

if __name__ == '__main__':
    app.run(debug=True)
