# Snake---Game-
# 🐍 Snake Game – Linked List Implementation

This project was developed for  
**AII201 – Data Structures and Algorithms**  
Near East University, Faculty of AI & Informatics.

The classic Snake game is implemented by modeling the snake’s body as a
**Linked List** data structure.  
The project focuses on movement logic, collision detection algorithms,
grid representation, food generation, and a GUI-based game loop.

---

## 🎯 Project Objective
- Apply the Linked List data structure in a real-world game scenario
- Implement movement and collision detection algorithms on a 2D grid
- Strengthen algorithmic thinking through practical application
- Reinforce data structures concepts with a complete project

---

## 🛠 Technologies Used
- Python
- Pygame (for GUI)

---

## 📐 Game Rules
- The game is played on a 2D grid (e.g., 20×20)
- The snake starts with a small length
- The snake moves step by step based on user input
- Food appears at random empty locations
- When the snake eats food, it grows
- The game ends if the snake hits a wall or itself
- Each food item increases the score

---

## 🧩 Core Data Structures

### 🟢 Snake as a Linked List
The snake is represented as a linked list where each node stores
a `(row, col)` coordinate.

**Supported operations:**
- Add new head
- Remove tail (unless the snake is growing)
- Traverse the list for collision detection

---

### 🟢 Grid Representation
The board is conceptually represented using 2D coordinates.

Each cell can be:
- Empty
- Snake body
- Food

---

### 🟢 Direction Handling
The snake’s movement direction is represented using:
- UP
- DOWN
- LEFT
- RIGHT

---

## ⚙️ Core Algorithms

### 🔁 Movement Algorithm
1. Compute the new head position  
2. Check for wall collisions  
3. Check for body collisions  
4. Check if food is eaten  
5. Update the linked list accordingly (grow or normal move)

---

### 💥 Collision Detection
The linked list is traversed to ensure that the new head position does not
overlap with any part of the snake’s body.

---

### 🍎 Food Placement
Food is placed randomly on an empty cell that is not occupied by the snake.

---

## ▶️ How to Run
```bash
python main.py
