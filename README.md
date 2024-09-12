# Boggle Game Simulator and Solver

This Python project simulates and solves Boggle games, while analyzing word frequency across multiple boards. The code can generate random Boggle boards, solve them to find the highest-scoring words, and keep track of the most common words across simulations. It also allows sorting and filtering word data based on various criteria.

## Features
- **Boggle Solver**: Input a Boggle board to solve and display the highest scoring words.
- **Board Simulation**: Simulate random Boggle boards for a specified time and track the best-performing boards.
- **Word Frequency Analysis**: Sort and analyze the frequency of words found in simulations based on length, alphabetical order, or frequency. You can also filter based on word characteristics like starting/ending letters.
- **Real Board Input**: Manually input real Boggle boards to store and analyze them.

## Installation
1. Clone the repository.
2. Ensure you have the `boggle.py` file in the project directory, which contains utility functions for generating grids, finding neighboring letters, and checking for valid words.
3. Install any required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How It Works
### Core Components:
1. **Simulating Boards**: 
   - The code can generate random boards of 16 letters using weighted random choices based on letter frequency stored in `letters.pk`.
   - Boards are solved to find all possible words using a recursive depth-first search.
   - The word frequency and board performance are tracked across multiple simulations.

2. **Solving Boggle**:
   - For a given board (input as a 16-letter string), the code will find valid words using the provided dictionary (`bogwords.txt`).
   - Scores are assigned based on word length, and the total points for the board are calculated.

3. **Word Frequency Analysis**:
   - After simulating boards, the user can view word statistics. Words can be sorted by length, frequency, or alphabetical order.
   - The filtering options include searching for words starting/ending with specific letters or containing specific sequences.

4. **Data Persistence**:
   - Data like letter frequencies, boards, and word frequencies are stored in `pickle` files to retain data across sessions.

### Files:
- `letters.pk`: Stores the frequency of letters from simulated boards.
- `boards.pk`: Stores the list of generated boards.
- `allwords.pk`: Stores the frequency of words found in all simulations.
- `count.pk`: Tracks the total number of boards simulated.

## Usage
1. **Running the Program**:
   - On running the script, you'll be prompted with several options:
     - `S`: Solve a specific Boggle board.
     - `R`: Simulate random boards for a set time and track the best-performing board.
     - `D`: Display word frequency data sorted by length, alphabetical order, or frequency.
     - `I`: Input and analyze real Boggle boards.
     - `B`: Show the best-performing board from simulations.

2. **Board Simulation**:
   - When simulating boards, the program generates random 4x4 grids, solves them, and tracks the highest score. The results are stored in the `allwords.pk` file for future analysis.

3. **Solving Boards**:
   - Input a 16-letter string representing a 4x4 Boggle board and see the possible words found, along with the total points for the board.

4. **Analyzing Word Frequencies**:
   - Sort words found during simulations by length, frequency, or alphabetically, and apply filters based on word structure.

## Example:
To solve a specific Boggle board, run the script and select `S`:
```
Input board to Solve: ABCDEFGHIJKLMNOP
```
The program will find and display all valid words on the board and show the total score.

To simulate random boards for 10 seconds, run the script and select `R`:
```
How many seconds to run this for: 10
```

## Dependencies
- `boggle.py`: This external module contains essential functions for generating grids, identifying neighbors, and solving Boggle boards.
- Python 3.x

## Future Enhancements
- Add a graphical interface for inputting boards and viewing results.
- Implement more advanced word filtering options, such as excluding specific letters.
- Allow variable-sized boards beyond the standard 4x4.

