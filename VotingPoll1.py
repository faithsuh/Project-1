from gui import *


def main():
    root = Tk()
    root.title("Voting App")
    root.resizable(False, False)
    VotingApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
