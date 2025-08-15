# 🚀 Push to GitHub (Force Push Script)

[![Copilot-20250601-124946.png](https://i.postimg.cc/P5TQq2RL/Copilot-20250601-124946.png)](https://postimg.cc/QHYT4kss)

## 🔧 Technologies & Tools

[![Cyfrin](https://img.shields.io/badge/Cyfrin-Audit%20Ready-005030?logo=shield&labelColor=F47321)](https://www.cyfrin.io/)
[![FlashBots](https://img.shields.io/pypi/v/finta?label=Finta&logo=python&logoColor=2774AE&labelColor=FFD100)](https://www.flashbots.net/)
[![Python](https://img.shields.io/badge/Python-3.11-003057?logo=python&labelColor=B3A369)](https://www.python.org/)
[![Solidity](https://img.shields.io/badge/Solidity-0.8.20-7BAFD4?logo=ethereum&labelColor=4B9CD3)](https://docs.soliditylang.org)
[![pYcHARM](https://img.shields.io/badge/Built%20with-PyCharm-782F40?logo=pycharm&logoColor=CEB888)](https://www.jetbrains.com/pycharm/)
[![Issues](https://img.shields.io/github/issues/74Thirsty/getBytecode.svg?color=hotpink&labelColor=brightgreen)](https://github.com/74Thirsty/getBytecode/issues)
[![Lead Dev](https://img.shields.io/badge/C.Hirschauer-Lead%20Developer-041E42?logo=parrotsecurity&labelColor=C5B783)](https://christopherhirschauer.bio)
[![Security](https://img.shields.io/badge/encryption-AES--256-orange.svg?color=13B5EA&labelColor=9EA2A2)]()

> <p><strong>Christopher Hirschauer</strong><br>
> Builder @ the bleeding edge of MEV, automation, and high-speed arbitrage.<br>
<em>June 13, 2025</em></p>
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
