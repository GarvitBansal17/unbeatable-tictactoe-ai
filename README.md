# 🤖 Unbeatable Tic-Tac-Toe AI

## 📖 Overview
This project is an interactive, Command Line Interface (CLI) based application developed as the **Bring Your Own Project (BYOP)** for the **Fundamentals of AI and ML** course. 

It is an implementation of the classic game Tic-Tac-Toe, but with a twist: the computer opponent is powered by Artificial Intelligence, making it mathematically impossible for a human player to win. The best a human can achieve is a draw.

## 🧠 Core AI Concepts Applied
This project demonstrates fundamental Artificial Intelligence decision-making processes without relying on external ML libraries. It applies the following concepts:
* **The Minimax Algorithm:** A recursive algorithm used in decision-making and game theory.
* **Adversarial Search:** The AI evaluates the entire state-space tree of possible future moves, assuming the human is playing optimally to minimize the AI's score.
* **Terminal State Evaluation:** The AI assigns mathematical weights to end-game states (+1 for an AI win, -1 for a human win, 0 for a draw) and bubbles these scores up the decision tree to pick the perfect move.

## ✨ Features
* **Perfect Gameplay:** The AI evaluates all possible future board states instantly.
* **Clean CLI Interface:** Easy-to-read text-based grid rendering.
* **Robust Input Validation:** Gracefully handles invalid user inputs (e.g., typing letters, out-of-bounds numbers, or selecting already occupied spaces).
* **Zero External Dependencies:** Built using strictly fundamental Python core libraries.

## ⚙️ Prerequisites
To run this application, you must have Python installed on your system.
* Python 3.x (No external packages like `pip install` are required).

## 🚀 Installation & Setup
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/](https://github.com/)[YOUR-GITHUB-USERNAME]/[YOUR-REPOSITORY-NAME].git
