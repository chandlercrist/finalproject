from PyQt6.QtWidgets import *
from gui import *
import sys


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(self.submit_vote)
        self.voted_ids_file = 'voted_ids.txt'
        self.already_voted_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.already_voted_label.setGeometry(QtCore.QRect(320, 250, 151, 16))
        self.already_voted_label.setObjectName("already_voted_label")
        self.already_voted_label.setStyleSheet("color: red")
        self.already_voted_label.setText("Already Voted")
        self.already_voted_label.hide()

    def submit_vote(self):

        voter_id = self.id_input.text().strip()

        if not self.is_valid_voter_id(voter_id):
            QMessageBox.warning(self, 'Invalid ID', 'Voter ID must be a 6-digit numberic value.')
            return

        if self.has_already_voted(voter_id):
            self.already_voted_label.show()
            return
        else:
            self.already_voted_label.hide()

        candidate = None
        if self.candidate_one.isChecked():
            candidate = 'Jane'
        elif self.candidate_two.isChecked():
            candidate = 'John'

        if candidate is None:
            QMessageBox.warning(self, "No Candidate Selected.", "Please select candidate.")
            return

        self.record_vote(voter_id, candidate)
        QMessageBox.information(self, "Vote Submitted", f"You voted for {candidate}.")
        self.clear_inputs()

    def is_valid_voter_id(self, voter_id):
        return voter_id.isdigit() and len(voter_id) == 6

    def has_already_voted(self, voter_id):
        try:
            with open(self.voted_ids_file, 'r') as file:
                voted_ids = file.readlines()
            voted_ids = [id.strip() for id in voted_ids]
            return voter_id in voted_ids
        except FileNotFoundError:
            return False

    def record_vote(self, voter_id, candidate):
        with open(self.voted_ids_file, 'a') as file:
            file.write(f"{voter_id}, {candidate}\n")

    def clear_inputs(self):
        self.id_input.clear()
        self.candidate_one.setAutoExclusive(False)
        self.candidate_two.setAutoExclusive(False)
        self.candidate_one.setChecked(False)
        self.candidate_two.setChecked(False)
        self.candidate_one.setAutoExclusive(True)
        self.candidate_two.setAutoExclusive(True)
