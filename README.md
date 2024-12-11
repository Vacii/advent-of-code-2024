# Advent of Code

This repository contains my solutions for the [Advent of Code](https://adventofcode.com/) challenges.

## About

Advent of Code is an annual coding challenge that takes place in December, offering a new two-part puzzle every day from December 1st to 25th. It's a great way to improve problem-solving skills and learn new programming techniques.

## Repository Structure

The project is organized as follows:

```
.
├── day01/
│   ├── input.txt
│   ├── solution.py
│   └── README.md
├── day02/
│   ├── input.txt
│   ├── solution.py
│   └── README.md
├── ...
├── utils/
│   ├── helpers.py
│   └── README.md
├── requirements.txt
└── README.md
```

### Folder Descriptions

- `dayXX/`: Contains the input file (`input.txt`) and solution script (`solution.py`) for each day.
- `utils/`: Utility scripts and helper functions used across multiple days.
- `requirements.txt`: Python dependencies for the project.
- `README.md`: This file, describing the project.

## How to Run

### Prerequisites

- Python 3.8 or later
- Recommended: a virtual environment tool such as `venv` or `conda`

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/advent-of-code.git
   cd advent-of-code
   ```

2. Set up a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Solutions

1. Navigate to the folder for the day you want to run:

   ```bash
   cd day01
   ```

2. Run the solution script:
   ```bash
   python solution.py
   ```

## Contributing

Feel free to fork this repository, solve puzzles, and submit pull requests. Contributions that improve the clarity, efficiency, or readability of solutions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Coding! 🎄
