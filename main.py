import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Countdown Timer")
window.resize(400, 300)

label = QLabel("05:00", window)

label.move(150, 100)

button = QPushButton("Start", window)
button.move(160, 160)


window.show()

sys.exit(app.exec())