from controller import *


def main() -> None:
    """
    Function to run all the code from the module
    :return: Nothing
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
