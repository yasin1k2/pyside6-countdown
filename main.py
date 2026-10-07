
# imports and global valuables
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtCore import QTimer

remaining_seconds = 300

# UI
app = QApplication(sys.argv)


## window
window = QWidget()
window.setWindowTitle(f"Countdown Timer")
window.resize(400, 300)


## label
label = QLabel("05:00", window)
label.move(185, 100)


## enter timer number


## button
start_button = QPushButton("Start", window)
start_button.move(160, 160)
reset_button = QPushButton("Reset",window)
reset_button.move(160, 240)
pause_button = QPushButton("Pause",window)
pause_button.move(160, 200)


def start_timer():
    print("Timer started!")
    timer.start(1000)

def reset_timer():
    global remaining_seconds
    print("Timer got reset!")
    remaining_seconds =300
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    label.setText(f"{minutes:02d}:{seconds:02d}")
    timer.stop()

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
    remaining_seconds -= 1
    if remaining_seconds <= 0:
        timer.stop()
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    label.setText(f"{minutes:02d}:{seconds:02d}")


timer.timeout.connect(timer_tick)


## show window
window.show()
sys.exit(app.exec())