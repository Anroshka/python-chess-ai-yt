# Python Chess Game with Stockfish AI

A chess game implementation in Python using Pygame, featuring both basic AI and Stockfish engine integration.

## Features
- Full chess game implementation with all standard rules
- Multiple themes (green, brown, blue, gray)
- Two AI modes:
  - Basic AI (original implementation)
  - Stockfish AI (professional chess engine)
- Visual move suggestions
- Move sound effects
- Drag and drop interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/python-chess-ai-yt.git
cd python-chess-ai-yt
```

2. Install required packages:
```bash
pip install pygame python-chess stockfish
```

3. Download Stockfish:
- Download the latest version from https://stockfishchess.org/download/
- Create a 'stockfish' folder in the project root
- Extract the Stockfish executable to the 'stockfish' folder
- Make sure the executable is named 'stockfish-windows-x86-64-avx2.exe' (Windows) or 'stockfish' (Linux/Mac)

## How to Play

1. Run the game:
```bash
python src/main.py
```

2. Controls:
- Click and drag pieces to move them
- Press 't' to change theme (green, brown, blue, gray)
- Press 'r' to restart the game

3. AI Modes:
- Basic AI: Original implementation (easier)
- Stockfish AI: Professional chess engine (stronger)
  - Configurable skill level (0-20) in stockfish_ai.py

## Game Snapshots

### Snapshot 1 - Start (green)
![snapshot1](snapshots/snapshot1.png)

### Snapshot 2 - Start (brown)
![snapshot2](snapshots/snapshot2.png)

### Snapshot 3 - Start (blue)
![snapshot3](snapshots/snapshot3.png)

### Snapshot 4 - Start (gray)
![snapshot4](snapshots/snapshot4.png)

## Technical Details

- Built with Python and Pygame
- Chess logic implementation from scratch
- Stockfish integration using python-chess library
- Multiple AI difficulty levels
- FEN position conversion for Stockfish integration
- Visual feedback during AI calculations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

- Original implementation based on YouTube tutorial
- Stockfish chess engine integration added by community
- Chess piece images and sound effects included in assets folder

## License

This project is open source and available under the MIT License.
