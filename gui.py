from tkinter import *
import csv


class VotingApp:
    """Class for the Voting App"""

    def __init__(self, window: Tk):
        """
        Initializes the VotingApp class.

        Parameters:
        - window: Tkinter window object
        """
        self.window = window
        self.window.configure(background='black')
        self.window.geometry('300x400')
        self.window.resizable(False, False)  # Making the window non-resizable
        self.id_label = Label(self.window, text='Enter ID:', font='Arial 15', bg='black', fg='purple')
        self.id_input = Entry(self.window, width=15, bg='purple', fg='white')

        # Adding validation to allow 5-digit numbers only
        self.id_input.config(validate="key")
        self.id_input.config(validatecommand=(self.window.register(self.validate_id), '%P'))

        self.candidates_label = Label(self.window, text='Candidates:', font='Arial 15 bold', bg='black', fg='white')

        self.candidate1_button = Button(self.window, text='Faith', font='Arial 15 underline', bg='black', fg='purple',
                                        command=lambda: self.vote('Faith'))
        self.candidate1_votes = 0
        self.candidate2_button = Button(self.window, text='Jayla', font='Arial 15 underline', bg='black', fg='purple',
                                        command=lambda: self.vote('Jayla'))
        self.candidate2_votes = 0
        self.submit_button = Button(self.window, text='Submit Vote', font='Arial 15', bg='black', fg='purple',
                                    command=self.submit_vote)
        self.result_label = Label(self.window, text='', font='Arial 15 bold', bg='black', fg='white')
        self.id_label.pack()
        self.id_input.pack()
        self.candidates_label.pack()
        self.candidate1_button.pack()
        self.candidate2_button.pack()
        self.submit_button.pack()
        self.result_label.pack()
        self.votes_file = 'votes.csv'
        self.load_votes()

    def load_votes(self) -> None:
        """
        Loads votes from a csv file.
        """
        try:
            with open(self.votes_file, 'r', newline='') as file:
                reader = csv.reader(file)
                self.votes = {row[0]: row[1] for row in reader}
        except FileNotFoundError:
            self.votes = {}

    def save_votes(self) -> None:
        """
        Saves votes to a csv file.
        """
        with open(self.votes_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for voter_id, candidate in self.votes.items():
                writer.writerow([voter_id, candidate])

    def validate_id(self, input_str: str) -> bool:
        """
        Validates the ID input to allow 5-digit numbers only.

        Parameters:
        - input_str: The input string from the Entry widget.

        Returns:
        - if True the input is a 5-digit number,
        -if False, will not take the vote.
        """
        return input_str.isdigit() and len(input_str) <= 5

    def vote(self, candidate: str) -> None:
        """
        Records the vote for a candidate.

        Parameters:
        - candidate: The name of the candidate.
        """
        voter_id = self.id_input.get()
        if len(voter_id) != 5:
            self.result_label.config(text="Please enter a 5-digit ID.", fg='purple')
            return

        if voter_id in self.votes:
            self.result_label.config(text="You have already voted.", fg='red')
            return

        if candidate == 'Faith':
            self.votes[voter_id] = 'Faith'
            self.candidate1_votes += 1
        elif candidate == 'Jayla':
            self.votes[voter_id] = 'Jayla'
            self.candidate2_votes += 1

        self.result_label.config(text=f"ID: {voter_id}\nFaith: {self.candidate1_votes}\nJayla: {self.candidate2_votes}",
                                 fg='white')

    def submit_vote(self) -> None:
        """
        Submits the vote and displays a confirmation message.
        """
        voter_id = self.id_input.get()

        # Data validation for the identifier
        if len(voter_id) != 5:
            self.result_label.config(text="Please enter a 5-digit ID.", fg='red')
            return

        if voter_id not in self.votes:
            self.result_label.config(text="Vote before submitting.", fg='red')
            return

        self.save_votes()
        self.result_label.config(text=f"Vote submitted for ID: {voter_id}!", fg='pink')
