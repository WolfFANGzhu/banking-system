from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QPushButton, QMessageBox, QInputDialog, QApplication, QVBoxLayout, QHBoxLayout, QFrame, QGridLayout,QLineEdit
from PyQt5.QtCore import pyqtSignal, Qt ,QTimer
from PyQt5.QtGui import QFont
import sys
import os
import APP_UI
import NetClient
import ATM_UI
import sqlite3
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.bank import reset_database
from Controller import Controller
import unittest
from PyQt5.QtTest import QTest
import time

class TestSingleUserATM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize the test environment and set class-level variables"""
        reset_database()
        time.sleep(5)  # Wait for the database to reset
        cls.identity = "Team15"
        cls.zmqThread = NetClient.ZmqClientThread(identity=cls.identity)
        cls.app = QApplication(sys.argv)
        cls.mainWindow = Controller(cls.zmqThread)
        cls.mainWindow.show()
        pass
    def setUp(self):
        """Initialization of each test case"""
        self.identity = TestSingleUserATM.identity
        self.zmqThread = TestSingleUserATM.zmqThread
        self.mainWindow = TestSingleUserATM.mainWindow
        self.msgBoxText = ""
        pass
    def tearDown(self):
        """Cleanup after each test case"""
        pass
        

    @classmethod
    def tearDownClass(cls):
        """Cleanup work after all test cases are executed"""
        # Ensure the event loop runs long enough to display the window
        QTest.qWait(1000)  # Delay 1 second to ensure the window is displayed
        print("[Test finished]")

    def test_create_account_common(self):
        # Click create account button
        print("test_create_account_common")
        QTest.mouseClick(self.mainWindow.atm.test_dict["b_create"], Qt.LeftButton)
        print("mouse_clicked")
        QTest.qWait(1000)
        QTest.keyClicks(self.mainWindow.atm.test_dict["i_id"], "1234567890")
        QTest.qWait(1000)
        QTest.keyClicks(self.mainWindow.atm.test_dict["i_password"], "Jsk123_456")
        QTest.qWait(1000)
        # Wait for 2s for the message box to appear
        QTimer.singleShot(2000, lambda: self.simulateClickMessage(self.mainWindow.atm))
        QTest.mouseClick(self.mainWindow.atm.test_dict["b_confirm"], Qt.LeftButton)
        self.assertEqual(self.msgBoxText, "Account created successfully")
        print("test_create_account_common finished")
    def test_deposit_common(self):
        # get start balance:
        start_balance = self.getDispayBalance()
        # Click deposit button
        # Wait for 2s for the message box to appear
        QTimer.singleShot(2000, lambda: self.simulateInputDialog(self.mainWindow.atm.test_dict["d_dialog"], "1000"))
        # Wait for 3s for the message box to appear
        QTimer.singleShot(3000, lambda: self.simulateClickMessage(self.mainWindow.atm))
        QTest.mouseClick(self.mainWindow.atm.test_dict["b_deposit"], Qt.LeftButton)
        QTest.qWait(1000)
        self.assertTrue(self.msgBoxText.startswith("$1000.00 deposited successfully"))
        # get end balance:
        end_balance = self.getDispayBalance()
        self.assertEqual(start_balance + 1000.00, end_balance)
    def simulateClickMessage(self,ui_window:QWidget):
        # Find the active message box and click the "OK" button
        active_message_box = ui_window.findChild(QMessageBox)
        if active_message_box:
            ok_button = active_message_box.button(QMessageBox.Ok)
            self.msgBoxText = active_message_box.text()
            print("[msgBoxText]: ", self.msgBoxText)
            if ok_button:
                QTest.mouseClick(ok_button, Qt.LeftButton)
    def simulateInputDialog(self,dialog:QInputDialog, text:str):
        input_field = dialog.findChild(QLineEdit)
        QTest.keyClicks(input_field, text)
        QTest.keyClick(input_field, Qt.Key_Enter)  # Simulate pressing Enter
    def getDispayBalance(self)->float:
        "Account ID: {self.current_account_id}\nBalance: ${balance:.2f}"
        return float(self.mainWindow.atm.test_dict["l_account"].text().split("$")[1])
if __name__ == "__main__":
    unittest.main()
