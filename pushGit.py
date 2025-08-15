#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def run(cmd, cwd, allow_fail=False):
    p = subprocess.run(cmd, cwd=cwd, shell=True, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0 and not allow_fail:
        print(f"❌ {cmd}\n{p.stderr.strip()}")
        sys.exit(1)
    return p.stdout.strip()

def git_config_get(cwd, key):
    out = run(f"git config --get {key}", cwd, allow_fail=True)
    return out if out else None

def ensure_git_identity(cwd):
    name = git_config_get(cwd, "user.name")
    email = git_config_get(cwd, "user.email")
    if not name:
        name = input("Git user.name not set. Enter a name: ").strip()
        if not name:
            print("❌ user.name is required"); sys.exit(1)
        run(f'git config user.name "{name}"', cwd)
    if not email:
        email = input("Git user.email not set. Enter an email: ").strip()
        if not email:
            print("❌ user.email is required"); sys.exit(1)
        run(f'git config user.email "{email}"', cwd)

def ensure_repo(cwd):
    if not (Path(cwd) / ".git").is_dir():
        print("📂 Initializing git repository…")
        run("git init", cwd)

def ensure_initial_commit(cwd):
    # Stage everything
    run("git add -A", cwd)
    # If nothing is staged, make an empty commit; else try a normal commit.
    changes = subprocess.run("git diff --cached --quiet", cwd=cwd, shell=True)
    if changes.returncode == 0:
        # no staged changes -> create empty commit if no commits exist
        has_commit = subprocess.run("git rev-parse --verify HEAD", cwd=cwd, shell=True)
        if has_commit.returncode != 0:
            run('git commit --allow-empty -m "Initial commit"', cwd)
    else:
        # staged changes exist
        run('git commit -m "Initial commit"', cwd, allow_fail=True)
        # If commit failed (e.g., nothing to commit due to race), try empty if no HEAD
        has_commit = subprocess.run("git rev-parse --verify HEAD", cwd=cwd, shell=True)
        if has_commit.returncode != 0:
            run('git commit --allow-empty -m "Initial commit"', cwd)

def ensure_main_branch(cwd):
    # Create/switch to main regardless of current state
    run("git checkout -B main", cwd)

def set_remote(cwd, repo_ssh):
    print("🔗 Setting remote origin…")
    run("git remote remove origin", cwd, allow_fail=True)
    run(f"git remote add origin {repo_ssh}", cwd)

def force_push(cwd):
    print("🚀 Force pushing to GitHub…")
    # Set upstream and force push
    run("git push -u --force origin main", cwd)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {Path(sys.argv[0]).name} <folder_path> <github_repo_ssh_url>")
        print(f"Example:\n  {Path(sys.argv[0]).name} . git@github.com:74Thirsty/pushGit.git")
        sys.exit(1)

    folder = os.path.abspath(sys.argv[1])
    repo_url = sys.argv[2]

    if not os.path.isdir(folder):
        print("❌ Provided path is not a directory.")
        sys.exit(1)

    if not repo_url.startswith("git@github.com:"):
        print("⚠️  Expected an SSH URL like git@github.com:USER/REPO.git")
        print("    If you intend to use SSH, fix the URL. Continuing anyway…")

    ensure_repo(folder)
    ensure_git_identity(folder)
    ensure_initial_commit(folder)
    ensure_main_branch(folder)
    set_remote(folder, repo_url)
    force_push(folder)
    print("✅ Done! Repository pushed to origin:main")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Aborted by user.")
        sys.exit(130)

