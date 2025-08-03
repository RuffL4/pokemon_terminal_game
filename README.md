# 🐍 Pokémon Terminal Game

A text-based Pokémon adventure in your terminal, written in Python! Choose your starter, fight wild Pokémon, catch new ones, heal at the Pokémon Center – all through the command line.

---

## 📦 Features

- 🧑‍🎮 Create your player (name and age)
- 🔥 Choose a starter Pokémon: Bulbasaur, Charmander, or Squirtle
- ⚔️ Battle wild Pokémon
- 🤖 Simple AI behavior for wild Pokémon attacks
- 🏥 Heal your team at the Pokémon Center
- 🎒 Party system: only one Pokémon per species allowed
- 🌈 Color-coded outputs using `colorama`

---

## 🚀 Quickstart

### 🔧 Requirements

- Python **3.10+**
- Install dependencies:
  ```bash
  pip install colorama
  ```

### ▶️ Start the Game

```bash
python project.py
```

---

## 📁 Project Structure

```
pokemon_terminal_game/
├── battle.py          # Battle logic with wild Pokémon
├── player.py          # Player class with attributes and party
├── pokemons.py        # Pokémon classes (Bulbasaur, Charmander, Squirtle)
└── project.py         # Main script (game entry point)
```

---

## 🎮 Gameplay Overview

### 1. Create a Player  
→ Enter your name and age.

### 2. Choose Your Starter  
→ Pick one of the three available Pokémon.

### 3. Main Menu Options:
- `1` – Battle a wild Pokémon  
- `2` – Visit the Pokémon Center (heal all)  
- `3` – Show info about your Pokémon

### 4. Battle System
- Type `attack` to damage the wild Pokémon  
- Type `switch` to change your active Pokémon  
- You can only catch a wild Pokémon if you don’t already have the same species in your party

---

## 📌 Notes

- The game does **not** save progress between sessions.
- Only living Pokémon can fight or be healed.
- A simple turn-based mechanic handles wild and player attacks.

---

## 🛠️ To-Do / Ideas

- 💾 Add save/load functionality
- 📈 Add experience points and leveling
- 🌍 Create a world map or navigation system
- ✨ Implement special abilities or types
- ✅ Add testing and error handling improvements

---
