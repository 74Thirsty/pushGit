# 🚀 Push to GitHub (Force Push Script)


[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Ethereum](https://img.shields.io/badge/network-Ethereum-%236C71C4)](https://ethereum.org/)
[![Security](https://img.shields.io/badge/encryption-AES--256-orange.svg)]()
[![Issues](https://img.shields.io/github/issues/74Thirsty/wallet.svg)](https://github.com/74Thirsty/wallet/issues)

A robust Python utility that **automatically creates or updates a Git repository** in any folder and **force pushes** its contents to a GitHub repository via SSH.

Perfect for quick one-off pushes, repo migrations, or syncing local projects to GitHub with a single command.

---

## ✨ Features

- 🆕 Initializes a Git repo if none exists  
- 🛠 Sets Git user.name and user.email if missing  
- 📦 Creates an **initial commit** (empty commit if no files staged)  
- 🔀 Switches or creates a `main` branch automatically  
- 🔗 Adds/updates the remote origin  
- 🚀 **Force pushes** all files to GitHub via SSH  
- 💯 Works on Linux, macOS, and Windows (with Git installed)

---

## 📦 Installation

1. Clone or download this repository
2. Install Python 3.8+ and ensure Git is installed
3. Place `push_to_github.py` anywhere in your PATH (optional)

---

## 🚀 Usage

```bash
python push_to_github.py <folder_path> <github_repo_ssh_url>
````

### Example

```bash
python push_to_github.py . git@github.com:74Thirsty/pushGit.git
```

### Parameters

* `<folder_path>` — Path to the local folder you want to push
* `<github_repo_ssh_url>` — SSH URL of your GitHub repo (e.g., `git@github.com:user/repo.git`)

---

## 🔧 How It Works

1. Checks if `.git` exists in the target folder; if not, runs `git init`
2. Ensures `git config user.name` and `git config user.email` are set
3. Stages all files (`git add -A`)
4. Commits changes (or makes an empty commit if nothing to commit)
5. Creates/switches to `main` branch (`git checkout -B main`)
6. Adds remote origin (replacing existing one if needed)
7. Force pushes to `origin main`

---

## 🛡 Requirements

* **Git** installed and in PATH
* **Python 3.8+** installed
* **SSH key** configured with GitHub ([Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh))

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## ⚠️ Warning

This script uses **`git push --force`** which will **overwrite** the remote repository’s history on the target branch.
Use with caution.

---

## ⭐ Show Support

If this saved you time, consider giving it a ⭐ on GitHub!

ETH wallet

```bash
0x749BFb765F22D851DE809fc1892c0919fAb40cef
```
