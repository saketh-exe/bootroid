# Asteroid Game

A classic Asteroids arcade game built with Python and Pygame.

## Project Description

This is a recreation of the classic Asteroids arcade game where you pilot a spaceship and destroy incoming asteroids. The game features:

- **Player Ship**: Control a spaceship in the center of the screen
- **Asteroids**: Dodge and destroy randomly spawning asteroids of varying sizes
- **Shooting Mechanic**: Shoot asteroids to destroy them and earn points
- **Split System**: When hit, larger asteroids split into smaller ones
- **Game Logging**: Event and state logging for game analysis
- **Collision Detection**: Realistic collision detection for asteroids and shots

## Requirements

- Python 3.13 or higher
- pygame 2.6.1

## Installation

1. Clone or navigate to the project directory:
```bash
cd bootGame
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

Or install pygame directly:
```bash
pip install pygame==2.6.1
```

## How to Run

1. Ensure your virtual environment is activated (if using one):
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Run the game:
```bash
python main.py
```

3. The game window will open. Close the window to exit the game.

## Game Controls

- **Arrow Keys**: Rotate and move your ship
- **Space**: Shoot
- **Close Window**: Exit game

## Game Mechanics

- Destroy asteroids by shooting them
- Larger asteroids split into smaller ones when destroyed
- Avoid colliding with asteroids
- The game ends if an asteroid hits your ship
- Game state and events are logged for analysis

## Project Structure

- `main.py` - Main game loop and entry point
- `player.py` - Player ship class
- `asteroid.py` - Asteroid class
- `asteroidfield.py` - Asteroid spawner
- `shot.py` - Projectile class
- `circleshape.py` - Base collision detection class
- `constants.py` - Game configuration (screen size, speeds, etc.)
- `logger.py` - Event and state logging
- `pyproject.toml` - Project metadata and dependencies
