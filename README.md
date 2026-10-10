# Countdown Timer

A simple countdown timer desktop application built with Python and PySide6.

## Features

- Set a countdown duration in minutes.
- Start the countdown timer.
- Pause the timer and resume from the remaining time.
- Reset the timer to the specified duration.
- Display the remaining time in `MM:SS` format.
- Dark-themed user interface.
- Input validation for invalid or non-positive durations.

## Technologies Used

- **Python** — Programming language
- **PySide6** — GUI framework
- **QTimer** — Timer functionality

## Requirements

- Python 3.9 or later
- PySide6

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR_PROJECT_DIRECTORY
   ```

3. Install PySide6:

   ```bash
   pip install PySide6
   ```

## Usage

Run the application using Python:

```bash
python main.py
```

Replace `main.py` with your Python file's name if it is different.

1. Enter the countdown duration in minutes.
2. Click **Start** to begin the countdown.
3. Click **Pause** to pause the timer.
4. Click **Start** again to resume the countdown.
5. Click **Reset** to restore the timer to the duration entered in the input field.

When the countdown reaches zero, the timer stops.

## Project Structure

```text
countdown-timer/
├── main.py
└── README.md
```

## Learning Goals

This project is part of my journey to improve my Python programming skills and learn GUI development.

Through this project, I am practicing:

- Building graphical user interfaces with PySide6
- Working with signals and slots
- Using `QTimer` for periodic events
- Managing application state
- Handling user input and validation
- Organizing widgets with layouts
- Styling widgets with Qt Style Sheets

## Future Improvements

- Display a notification when the countdown finishes.
- Improve timer state management.
- Add hours and seconds input options.
- Add custom themes and UI improvements.
- Allow users to start a new countdown more easily.

## License

This project is open source. A license can be added when the project is ready for distribution.
