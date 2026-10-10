
# imports and global valuables
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QTimer, Qt


# UI
app = QApplication(sys.argv)


## window
window = QWidget()
window.setWindowTitle(f"Countdown Timer")
window.setStyleSheet("""
    QWidget {
        background-color: #1e1e2e;
        color: #cdd6f4;
        font-family: Arial;
    }
""")
window.resize(400, 300)
main_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()

main_layout.setSpacing(15)
main_layout.setContentsMargins(25, 25, 25, 25)



## label

label = QLabel("05:00", window)
label.setStyleSheet("""
    font-size: 48px;
    font-weight: bold;
    color: #89b4fa;
""")
label_name = QLabel("Countdown Timer", window)
label_name.setStyleSheet("""
    font-size: 22px;
    font-weight: bold;
""")


## enter timer number
time_input = QLineEdit("5", window)
time_input.setPlaceholderText("Minutes")
time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
time_input.setStyleSheet("""
    QLineEdit {
        background-color: #313244;
        border: 1px solid #585b70;
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
    }
""")

remaining_seconds = 300


## update timer display
def update_time():
    global remaining_seconds
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    label.setText(f"{minutes:02d}:{seconds:02d}")


## button
start_button = QPushButton("Start", window)
reset_button = QPushButton("Reset",window)
pause_button = QPushButton("Pause",window)
button_style = """
    QPushButton {
        background-color: #45475a;
        color: #cdd6f4;
        border: none;
        border-radius: 8px;
        padding: 10px 16px;
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #585b70;
    }

    QPushButton:pressed {
        background-color: #313244;
    }
"""

start_button.setStyleSheet(button_style)
pause_button.setStyleSheet(button_style)
reset_button.setStyleSheet(button_style)


def start_timer():
    global remaining_seconds

    if not timer.isActive():
        if remaining_seconds <= 0:
            try:
                input_minutes = int(time_input.text())

                if input_minutes <= 0:
                    print("Enter a number greater than zero!")
                    return

                remaining_seconds = input_minutes * 60
                update_time()

            except ValueError:
                print("Please enter a valid integer!")
                return

        print("Timer started!")
        timer.start(1000)

def reset_timer():
    global remaining_seconds

    timer.stop()

    try:
        input_minutes = int(time_input.text())

        if input_minutes <= 0:
            print("Enter a number greater than zero!")
            return

        remaining_seconds = input_minutes * 60
        update_time()
        print("Timer got reset!")

    except ValueError:
        print("Please enter a valid integer!")

def pause_timer():
    print("Timer paused!")
    timer.stop()

start_button.clicked.connect(start_timer)
reset_button.clicked.connect(reset_timer)
pause_button.clicked.connect(pause_timer)


## Timer
timer = QTimer()

def timer_tick():
    global remaining_seconds

    if remaining_seconds > 0:
        remaining_seconds -= 1

    update_time()

    if remaining_seconds == 0:
        timer.stop()
        print("Time is up!")


timer.timeout.connect(timer_tick)


## layout
main_layout.addWidget(label_name)
main_layout.addWidget(label)
main_layout.addWidget(time_input)
buttons_layout.addWidget(start_button)
buttons_layout.addWidget(reset_button)
buttons_layout.addWidget(pause_button)
main_layout.addLayout(buttons_layout)
window.setLayout(main_layout)

label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

## show window
window.show()
sys.exit(app.exec())