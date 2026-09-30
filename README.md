# Flappy Bird - Python Project

## 1. Project Title

**Flappy Bird - Python Project**

## 2. Overview of the Project

This project is a simple Flappy Bird-style game made using Python. The player controls a yellow bird and uses the **Space** key to make it jump. The bird is affected by gravity and has to pass through the gap between green pipes.

The game keeps track of the player's score. The score increases when the bird successfully passes a pipe. The game ends when the bird collides with a pipe, the ground, or the ceiling.

The game window is created with a size of **800 × 600 pixels** and has a sky-blue background.

## 3. Features

- Simple Flappy Bird-style gameplay.
- Yellow circular bird controlled using the **Space** key.
- Gravity effect that continuously pulls the bird downward.
- Green pipes with a randomly positioned gap.
- Pipes move from right to left.
- Score increases when the bird passes the pipe.
- Random pipe gap position makes each round slightly different.
- Collision detection with:
  - Top pipe
  - Bottom pipe
  - Ground
  - Ceiling
- Displays **GAME OVER** when the game ends.
- Simple graphical interface using Python Turtle.

## 4. Technologies / Tools Used

### Programming Language
- **Python**

### Python Libraries
- **Turtle** - Used to create the game window, bird, pipes, score, and game graphics.
- **Random** - Used to generate a random vertical position for the pipe gap.

### Tools
- Any Python-compatible IDE or code editor, such as:
  - Visual Studio Code
  - PyCharm
  - IDLE

## 5. Steps to Install and Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

You can check the installation by opening a terminal or command prompt and running:

```bash
python --version
```

### Step 2: Download or copy the project

Save the Python code in a file named:

```text
Project_Game.py
```

### Step 3: Open the project

Open `Project_Game.py` in your preferred Python IDE or code editor.

### Step 4: Run the program

Run the Python file using your IDE or from the terminal:

```bash
python Project_Game.py
```

### Step 5: Start playing

A game window will open. Press the **Spacebar** to make the bird jump.

Try to keep the bird between the pipes and avoid hitting the pipes, ground, or ceiling.

## 6. Instructions for Testing

The following tests can be performed to check whether the game is working correctly.

### Test 1: Game Window

**Action:** Run the program.

**Expected Result:**  
An 800 × 600 game window opens with a sky-blue background, a yellow bird, green pipes, and a score display.

### Test 2: Bird Jump

**Action:** Press the **Spacebar**.

**Expected Result:**  
The bird moves upward when the Spacebar is pressed.

### Test 3: Gravity

**Action:** Do not press any key for some time.

**Expected Result:**  
The bird gradually moves downward because of gravity.

### Test 4: Pipe Movement

**Action:** Start the game and observe the pipes.

**Expected Result:**  
The pipes move from right to left across the screen.

### Test 5: Score

**Action:** Successfully guide the bird past the pipe.

**Expected Result:**  
The score increases by 1.

### Test 6: Pipe Collision

**Action:** Allow the bird to hit the top or bottom pipe.

**Expected Result:**  
The game stops and **GAME OVER** appears.

### Test 7: Ground Collision

**Action:** Do not press the Spacebar and allow the bird to fall.

**Expected Result:**  
When the bird reaches the ground area, the game ends and **GAME OVER** appears.

### Test 8: Ceiling Collision

**Action:** Press the Spacebar repeatedly so that the bird reaches the top of the game window.

**Expected Result:**  
The game ends when the bird reaches the ceiling area and **GAME OVER** appears.

## Project Structure

```text
Project/
│
├── Project_Game.py
└── README.md
```

## Conclusion

This project demonstrates basic Python programming concepts such as variables, functions, loops, conditional statements, keyboard input, random values, collision detection, and graphical programming using the Turtle library.
