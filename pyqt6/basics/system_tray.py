from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QSystemTrayIcon, QMenu

)


def main() -> None:
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)    # Set application doesn't end even after the main window closed

    icon = QIcon("../data/abacus.png")

    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QMenu()
    action = QAction("A menu item")
    menu.addAction(action)

    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    tray.setContextMenu(menu)
    app.exec()


if __name__=="__main__":
    main()


