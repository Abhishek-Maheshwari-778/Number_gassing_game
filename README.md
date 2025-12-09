# Number Guessing Game (CLI + GUI Version)

A fun and interactive **Number Guessing Game** made using **Python**, featuring:

- ✔️ **Command-Line Version**
- ✔️ **Graphical User Interface (GUI)** using Tkinter  
- ✔️ **Sound Effects & Background Music** using Pygame  
- ✔️ **User Profiles & Leaderboard** (CSV-based)
- ✔️ **Multiple Game Modes**  
- ✔️ **Colorful UI (CLI) using Colorama**

---

## 📂 Project Structure
📁 number-guessing-game
│── _pycache/
│── sounds/
│ ├── click.wav
│ ├── win.wav
│ ├── lose.wav
│ └── background.mp3
│── number_gassing.py
│── number_gassing_with_gui.py
│── README.md

---

## 🚀 Features

### 🖥️ **CLI Version (number_gassing.py)**
- 🎮 **3 Game Modes**
  - Single Player  
  - 2-Player Mode  
  - Time Attack (with countdown)  
- 🧠 Difficulty Levels:
  - Easy (1–50)
  - Medium (1–100)
  - Hard (1–200)
- 🏆 Auto saved **Leaderboard**
- 👤 **User Profiles stored in CSV**
- 💡 Smart Hints  
- 🎨 Colorful terminal UI using **colorama**

---

### 🖼️ **GUI Version (number_gassing_with_gui.py)**
- 🎧 Background music + sound effects
- 🟩 Beautiful and simple Tkinter UI  
- 🖱️ Hover effects on buttons  
- 🎮 Play mode with:
  - Username input  
  - Attempts tracking  
  - Smart hints  

---

## 🔧 Installation

### 1️⃣ Install Python (3.8+ recommended)

Download from: https://www.python.org/downloads/

### 2️⃣ Install required libraries

Run:

```bash
pip install colorama pygame
```

Tkinter comes pre-installed with Python.
No extra installation needed.

▶️ Run the Game
Run CLI Version:
python number_gassing.py

Run GUI Version:
python number_gassing_with_gui.py

🕹️ Controls & Gameplay
🎯 CLI Gameplay
Enter your username
Select game mode
Select difficulty
Guess the number before attempts run out
See your score & leaderboard rank

🎯 GUI Gameplay
Enter your username
Guess the hidden number
Get instant hints
Hear sound effects
Play again from menu

🔊 Sounds Folder
Place all sound files in the sounds/ folder:
sounds/click.wav  
sounds/win.wav  
sounds/lose.wav  
sounds/background.mp3

💾 User Profiles (CSV)
A file user_profiles.csv is auto-created to store:
Username	Attempts	Games Played	Wins

🌟 Future Improvements (Optional Ideas)
Add themes (dark/light mode)
Add more game modes
Multiplayer GUI mode
Animated GUI elements
Store profiles using SQLite

🧑‍💻 Author
Developer: Abhishek Maheshwari
Project: Number Guessing Game – CLI + GUI
Language: Python

📜 License
This project is free to use for learning & personal projects.

🎉 Enjoy the Game!


