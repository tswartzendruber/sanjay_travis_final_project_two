from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from view import Ui_MainWindow
from module import *


class Controller(QWidget, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())

        self.insert_players()
        self.players_list = []
        self.current_guess_data = ''

        self.height_of_table = 21
        self.random_player_info = randomizer()

        self.guess_count = 1

    def insert_players(self):
        self.players_list = get_players()
        self.players_list.pop(0)
        for i in self.players_list:
            self.dropdown_players.addItem(i[0])

        return self.players_list

    def submit(self):
        if self.guess_count > 8:
            self.button_submit.setEnabled(False)
            self.label_enter_first_guess.setText(f"You LOSE! The player was {self.random_player_info[0]}.")
            return

        self.height_of_table += 100
        self.table_player_info.setMinimumHeight(self.height_of_table)
        self.table_player_info.setMaximumHeight(self.height_of_table)

        row_position = self.table_player_info.rowCount()
        self.table_player_info.insertRow(row_position)
        player_name = self.dropdown_players.currentText()

        list_of_players = self.insert_players()

        if player_name != self.random_player_info[0]:
            # Finding the information of guessed player
            for line in self.players_list:
                if line[0] == player_name:
                    self.current_guess_data = line

                    self.label_enter_first_guess.setText("Enter your next guess!")

                    self.picture = QtGui.QPixmap(f'icons/{self.current_guess_data[8]}.png').scaled(136,100)
                    self.label = QLabel()
                    self.label.setPixmap(self.picture)

                    self.table_player_info.setCellWidget(row_position, 0, self.label)
                    self.table_player_info.setItem(row_position, 1, QTableWidgetItem(self.current_guess_data[0]))
                    self.table_player_info.setItem(row_position, 2, QTableWidgetItem(self.current_guess_data[1]))
                    self.table_player_info.setItem(row_position, 3, QTableWidgetItem(self.current_guess_data[2]))
                    self.table_player_info.setItem(row_position, 4, QTableWidgetItem(self.current_guess_data[3]))
                    self.table_player_info.setItem(row_position, 5, QTableWidgetItem(self.current_guess_data[4]))
                    self.table_player_info.setItem(row_position, 6, QTableWidgetItem(self.current_guess_data[5]))
                    self.table_player_info.setItem(row_position, 7, QTableWidgetItem(self.current_guess_data[6]))
                    self.table_player_info.setItem(row_position, 8, QTableWidgetItem(self.current_guess_data[7]))

                    # Name
                    self.table_player_info.item(row_position, 1).setBackground(QtGui.QColor('red'))

                    # Conference
                    if self.current_guess_data[1] == self.random_player_info[1]:
                        self.table_player_info.item(row_position, 2).setBackground(QtGui.QColor('lime'))
                    else:
                        self.table_player_info.item(row_position, 2).setBackground(QtGui.QColor('red'))

                    # Division
                    if self.current_guess_data[2] == self.random_player_info[2]:
                        self.table_player_info.item(row_position, 3).setBackground(QtGui.QColor('lime'))
                    else:
                        self.table_player_info.item(row_position, 3).setBackground(QtGui.QColor('red'))

                    # Team
                    if self.current_guess_data[3] == self.random_player_info[3]:
                        self.table_player_info.item(row_position, 4).setBackground(QtGui.QColor('lime'))
                    else:
                        self.table_player_info.item(row_position, 4).setBackground(QtGui.QColor('red'))

                    # Height
                    current_guess_height = self.current_guess_data[4].split('-')
                    random_player_height = self.random_player_info[4].split('-')

                    current_guess_feet = int(current_guess_height[0])
                    current_guess_inches = int(current_guess_height[1])

                    random_player_feet = int(random_player_height[0])
                    random_player_inches = int(random_player_height[1])

                    if current_guess_height == random_player_height:
                        self.table_player_info.item(row_position, 5).setBackground(QtGui.QColor('lime'))
                    elif ((random_player_feet == current_guess_feet) and (
                            random_player_inches > current_guess_inches)) or (random_player_feet > current_guess_feet):
                        self.table_player_info.setItem(row_position, 5, QTableWidgetItem(f'{self.current_guess_data[4]} ^'))
                        self.table_player_info.item(row_position, 5).setBackground(QtGui.QColor('red'))
                    elif ((random_player_feet == current_guess_feet) and (
                            random_player_inches < current_guess_inches)) or (random_player_feet < current_guess_feet):
                        self.table_player_info.setItem(row_position, 5, QTableWidgetItem(f'{self.current_guess_data[4]} v'))
                        self.table_player_info.item(row_position, 5).setBackground(QtGui.QColor('red'))

                    # Age
                    current_guess_age = int(self.current_guess_data[5])
                    random_player_age = int(self.random_player_info[5])

                    if random_player_age == current_guess_age:
                        self.table_player_info.item(row_position, 6).setBackground(QtGui.QColor('lime'))
                    elif random_player_age > current_guess_age:
                        self.table_player_info.setItem(row_position, 6, QTableWidgetItem(f'{current_guess_age} ^'))
                        self.table_player_info.item(row_position, 6).setBackground(QtGui.QColor('red'))
                    elif random_player_age < current_guess_age:
                        self.table_player_info.setItem(row_position, 6, QTableWidgetItem(f'{current_guess_age} v'))
                        self.table_player_info.item(row_position, 6).setBackground(QtGui.QColor('red'))

                    # Jersey No.
                    current_guess_jersey = int(self.current_guess_data[6])
                    random_player_jersey = int(self.random_player_info[6])

                    if random_player_jersey == current_guess_jersey:
                        self.table_player_info.item(row_position, 7).setBackground(QtGui.QColor('lime'))
                    elif random_player_jersey > current_guess_jersey:
                        self.table_player_info.setItem(row_position, 7, QTableWidgetItem(f'{current_guess_jersey} ^'))
                        self.table_player_info.item(row_position, 7).setBackground(QtGui.QColor('red'))
                    elif random_player_jersey < current_guess_jersey:
                        self.table_player_info.setItem(row_position, 7, QTableWidgetItem(f'{current_guess_jersey} v'))
                        self.table_player_info.item(row_position, 7).setBackground(QtGui.QColor('red'))

                    # Position
                    if self.current_guess_data[7] == self.random_player_info[7]:
                        self.table_player_info.item(row_position, 8).setBackground(QtGui.QColor('lime'))
                    else:
                        self.table_player_info.item(row_position, 8).setBackground(QtGui.QColor('red'))

                    break
        else:
            for line in self.players_list:
                if line[0] == player_name:
                    self.current_guess_data = line

                    self.label_enter_first_guess.setText("You got it right!")

                    self.picture = QtGui.QPixmap(f'icons/{self.current_guess_data[8]}.png').scaled(136, 100)
                    self.label = QLabel()
                    self.label.setPixmap(self.picture)


                    self.table_player_info.setCellWidget(row_position, 0, self.label)
                    self.table_player_info.setItem(row_position, 1, QTableWidgetItem(self.current_guess_data[0]))
                    self.table_player_info.item(row_position, 1).setBackground(QtGui.QColor('lime'))
                    self.table_player_info.setItem(row_position, 2, QTableWidgetItem(self.current_guess_data[1]))
                    self.table_player_info.item(row_position, 2).setBackground(QtGui.QColor('lime'))
                    self.table_player_info.setItem(row_position, 3, QTableWidgetItem(self.current_guess_data[2]))
                    self.table_player_info.item(row_position, 3).setBackground(QtGui.QColor('lime'))
                    self.table_player_info.setItem(row_position, 4, QTableWidgetItem(self.current_guess_data[3]))
                    self.table_player_info.item(row_position, 4).setBackground(QtGui.QColor('lime'))
                    self.table_player_info.setItem(row_position, 5, QTableWidgetItem(self.current_guess_data[4]))
                    self.table_player_info.item(row_position, 5).setBackground(QtGui.QColor('lime'))
                    self.table_player_info.setItem(row_position, 6, QTableWidgetItem(self.current_guess_data[5]))
                    self.table_player_info.item(row_position, 6).setBackground(QtGui.QColor('lime'))
                    self.table_player_info.setItem(row_position, 7, QTableWidgetItem(self.current_guess_data[6]))
                    self.table_player_info.item(row_position, 7).setBackground(QtGui.QColor('lime'))
                    self.table_player_info.setItem(row_position, 8, QTableWidgetItem(self.current_guess_data[7]))
                    self.table_player_info.item(row_position, 8).setBackground(QtGui.QColor('lime'))

                    self.button_submit.setEnabled(False)

                    break

        header = self.table_player_info.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_player_info.resizeRowsToContents()

        self.guess_count += 1
