# Snake Game

Classic snake game built in Python using the built‑in `turtle` graphics module.  
The project is structured into separate classes for the snake, food, and scoreboard to practice object‑oriented programming, movement logic, and collision detection. The game tracks your score and keeps your high score updated in the `data.txt` file.

---

## Features

- Snake movement with smooth step-based motion.
- Food that spawns at random positions within the play area.
- Collision detection with walls and the snake’s own tail.
- Score display with persistent high score stored in `data.txt`.
- Simple, readable code separated into multiple modules:
  - `main.py` – game loop and screen setup  
  - `snake.py` – snake segments and movement logic  
  - `Food.py` – food behavior and random placement  
  - `scoreboard.py` – score and high-score handling  

---

## Requirements

- Python 3.10 or higher
- Desktop environment that supports the built‑in `turtle` graphics window

No external libraries are required.

---

## How to Run

1. Clone or download this repository.
2. Make sure the following files are in the same folder:
   - `main.py`
   - `snake.py`
   - `Food.py`
   - `scoreboard.py`
   - `data.txt`
3. Open a terminal in that folder.
4. Run

## How to play
Use arrow keys(Up, Down, Right, Left) for snake movements

Notes
The data.txt file is used to store the high score.
If it is empty or missing, the game will create/update it automatically when you play.

This project is intended as a beginner‑friendly practice game for Python, OOP, and basic game logic. You are welcome to extend it with new features like levels, speed increase, or obstacles.

```bash
python main.py
