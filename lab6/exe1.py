import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt

class TicTacToeGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Крестики-нолики (Адаптивные)")
        self.setMinimumSize(300, 400)
        self.buttons = []
        self.current_player = "X"
        self.move_count = 0        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(5)
        self.main_layout.addLayout(self.grid_layout, stretch=5)
        self.create_buttons()       
        self.status_label = QLabel()
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px; margin: 10px;")
        self.status_label.setText(f"Ход игрока: {self.current_player}")
        self.main_layout.addWidget(self.status_label, stretch=1)
        self.reset_button = QPushButton("Начать заново")
        self.reset_button.setMinimumHeight(40)
        self.reset_button.setStyleSheet("font-size: 14px;")
        self.reset_button.clicked.connect(self.reset_game)
        self.main_layout.addWidget(self.reset_button, stretch=1)

    def create_buttons(self):
        self.buttons = []
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = QPushButton("")
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setStyleSheet("font-size: 32px; font-weight: bold;")
                button.clicked.connect(self.on_click)
                self.grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_click(self):
        button = self.sender()
        if button.text() == "" and button.isEnabled():
            button.setText(self.current_player)
            self.move_count += 1            
            if self.check_winner():
                self.end_game(f"Игрок {self.current_player} победил!")
            elif self.move_count == 9:
                self.end_game("Ничья!")
            else:
                self.switch_player()
                self.status_label.setText(f"Ход игрока: {self.current_player}")

    def check_winner(self):
        for row in self.buttons:
            if row[0].text() == row[1].text() == row[2].text() != "":
                return True
        for col in range(3):
            if self.buttons[0][col].text() == self.buttons[1][col].text() == self.buttons[2][col].text() != "":
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            return True 
        return False

    def end_game(self, message):
        self.status_label.setText(message)
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)
        QMessageBox.information(self, "Игра окончена", message)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.current_player = "X"
        self.move_count = 0
        self.status_label.setText(f"Ход игрока: {self.current_player}")
        for row in self.buttons:
            for button in row:
                button.setText("")
                button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeGame()
    window.show()
    sys.exit(app.exec_())