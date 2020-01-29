from PyQt5 import QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _from_utf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName(_from_utf8("MainWindow"))
        MainWindow.resize(852, 671)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_from_utf8("centralwidget"))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        font = QtGui.QFont()
        font.setPointSize(12)



        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 811, 51))
        self.groupBox_2.setTitle(_from_utf8(""))
        self.groupBox_2.setObjectName(_from_utf8("groupBox_2"))
        self.display = QtWidgets.QPushButton(self.groupBox_2)
        self.display.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.display.setObjectName(_from_utf8("display"))
        self.first = QtWidgets.QPushButton(self.groupBox_2)
        self.first.setGeometry(QtCore.QRect(170, 10, 111, 31))
        self.first.setObjectName(_from_utf8("first"))
        self.lr1 = QtWidgets.QPushButton(self.groupBox_2)
        self.lr1.setGeometry(QtCore.QRect(340, 10, 111, 31))
        self.lr1.setObjectName(_from_utf8("lr1"))
        self.lalr = QtWidgets.QPushButton(self.groupBox_2)
        self.lalr.setGeometry(QtCore.QRect(510, 10, 111, 31))
        self.lalr.setObjectName(_from_utf8("lalr"))
        self.parse_table = QtWidgets.QPushButton(self.groupBox_2)
        self.parse_table.setGeometry(QtCore.QRect(680, 10, 111, 31))
        self.parse_table.setObjectName(_from_utf8("parse_table"))
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 330, 811, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser.setObjectName(_from_utf8("textBrowser"))
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(23, 80, 381, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_from_utf8("plainTextEdit"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_from_utf8("label_2"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_from_utf8("Gungsuh"))
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_from_utf8("label"))
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(730, 60, 101, 31))
        self.groupBox_3.setTitle(_from_utf8(""))
        self.groupBox_3.setObjectName(_from_utf8("groupBox_3"))
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_from_utf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName(_from_utf8("menubar"))
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName(_from_utf8("menu_File"))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_from_utf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName(_from_utf8("action_Open"))
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName(_from_utf8("action_Exit"))
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName(_from_utf8("actionAuthor"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)


        self.re_translate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        MainWindow.setTabOrder(self.display, self.first)
        MainWindow.setTabOrder(self.first, self.lr1)
        MainWindow.setTabOrder(self.lr1, self.lalr)
        MainWindow.setTabOrder(self.lalr, self.parse_table)
        MainWindow.setTabOrder(self.parse_table, self.textBrowser)

    def re_translate_ui(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

        self.display.setText(_translate("MainWindow", "Display", None))
        self.first.setText(_translate("MainWindow", "First", None))
        self.lr1.setText(_translate("MainWindow", "LR(1) items", None))
        self.lalr.setText(_translate("MainWindow", "LALR items", None))
        self.parse_table.setText(_translate("MainWindow", "Parsing Table", None))
        self.label_2.setText(_translate("MainWindow", "Enter grammar :", None))
        self.label.setText(_translate("MainWindow", "LALR Parser", None))
        self.label_4.setText(_translate("MainWindow", "\'e\' : epsilon", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))

        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_Exit.setText(_translate("MainWindow", "&Exit", None))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

