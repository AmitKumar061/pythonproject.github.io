# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from calculate_points import player_points
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from open import Ui_Dialog as Open   # importing open window dialogbox
from new import Ui_Dialog as New     # importing new window dialogbox
from evaluate import Ui_Dialog as Eva  # importing evaluate window dialogbox

import sqlite3
fant=sqlite3.connect('cricket_db.db')  # connecting to database file(fandatabase.db)
fantcurs=fant.cursor()

class Ui_MainWindow(object):
    def __init__(self):
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Eva()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)

      # FILE OPENING MENU
    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.openbtn.clicked.connect(self.openteam)

    # EVALUATE TEAM MENU
    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()
    
    def setupUi(self, MainWindow):

        # INITIALISING POINTS AND COUNTS
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        # INITIALIZING LISTS
        self.a = []  # bowler names list
        self.b = []  #  batsman nameslist
        self.c = []   # allrounder names list
        self.d = []  #wicketer names list
        self.list1 = []    # selectedplayer's list

        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 40, 731, 80))
        self.frame.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.BAT = QtWidgets.QLabel(self.frame)
        self.BAT.setGeometry(QtCore.QRect(130, 50, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BAT.setFont(font)
        self.BAT.setStyleSheet("color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.BAT.setObjectName("BAT")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(180, 50, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.BOWL = QtWidgets.QLabel(self.frame)
        self.BOWL.setGeometry(QtCore.QRect(300, 50, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BOWL.setFont(font)
        self.BOWL.setStyleSheet("color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.BOWL.setObjectName("BOWL")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 50, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ARL = QtWidgets.QLabel(self.frame)
        self.ARL.setGeometry(QtCore.QRect(500, 50, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ARL.setFont(font)
        self.ARL.setStyleSheet("color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.ARL.setObjectName("ARL")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(540, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.WK = QtWidgets.QLabel(self.frame)
        self.WK.setGeometry(QtCore.QRect(690, 50, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.WK.setFont(font)
        self.WK.setStyleSheet("color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.WK.setObjectName("WK")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 220, 731, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.av_player = QtWidgets.QListWidget(self.frame_2)
        self.av_player.setGeometry(QtCore.QRect(0, 50, 291, 261))
        self.av_player.setObjectName("av_player")
        self.sel_player = QtWidgets.QListWidget(self.frame_2)
        self.sel_player.setGeometry(QtCore.QRect(440, 50, 291, 261))
        self.sel_player.setObjectName("sel_player")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(340, 140, 55, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(-1, 0, 291, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bat_rb = QtWidgets.QRadioButton(self.frame_4)
        self.bat_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bat_rb.setFont(font)
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout.addWidget(self.bat_rb)
        self.bow_rb = QtWidgets.QRadioButton(self.frame_4)
        self.bow_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bow_rb.setFont(font)
        self.bow_rb.setObjectName("bow_rb")
        self.horizontalLayout.addWidget(self.bow_rb)
        self.ar_rb = QtWidgets.QRadioButton(self.frame_4)
        self.ar_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ar_rb.setFont(font)
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout.addWidget(self.ar_rb)
        self.wk_rb = QtWidgets.QRadioButton(self.frame_4)
        self.wk_rb.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.wk_rb.setFont(font)
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout.addWidget(self.wk_rb)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(440, 0, 291, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.team_name = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setStyleSheet("color: rgb(85, 170, 255);")
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_2.addWidget(self.team_name)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 150, 721, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.points_available = QtWidgets.QLabel(self.frame_3)
        self.points_available.setGeometry(QtCore.QRect(140, 20, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.points_available.setFont(font)
        self.points_available.setObjectName("points_available")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(430, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.points_used = QtWidgets.QLabel(self.frame_3)
        self.points_used.setGeometry(QtCore.QRect(530, 20, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.points_used.setFont(font)
        self.points_used.setObjectName("points_used")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_t = QtWidgets.QAction(MainWindow)
        self.new_t.setObjectName("new_t")
        self.open_t = QtWidgets.QAction(MainWindow)
        self.open_t.setObjectName("open_t")
        self.save_t = QtWidgets.QAction(MainWindow)
        self.save_t.setObjectName("save_t")
        self.evaluat_t = QtWidgets.QAction(MainWindow)
        self.evaluat_t.setObjectName("evaluat_t")
        self.menuFile.addAction(self.new_t)
        self.menuFile.addAction(self.open_t)
        self.menuFile.addAction(self.save_t)
        self.menuFile.addAction(self.evaluat_t)
        self.menubar.addAction(self.menuFile.menuAction())

        #Action teiggered
        self.new_t.triggered.connect(self.file_new)
        self.open_t.triggered.connect(self.file_open)
        self.save_t.triggered.connect(self.file_save)
        self.evaluat_t.triggered.connect(self.file_evaluate)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # DOUBLE CLICK
        self.av_player.itemDoubleClicked.connect(self.removelist1)
        self.sel_player.itemDoubleClicked.connect(self.removelist2)

        # -----stats of player
        self.stats = {}

        self.new_screen.savename.clicked.connect(self.namechange)

        # RADIOBUTTONS  CLICK
        self.bat_rb.clicked.connect(self.load_names)
        self.wk_rb.clicked.connect(self.load_names)
        self.bow_rb.clicked.connect(self.load_names)
        self.ar_rb.clicked.connect(self.load_names)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.BAT.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Your Selections"))
        self.label_5.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.BOWL.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "All Rounders(AR)"))
        self.ARL.setText(_translate("MainWindow", "##"))
        self.label_10.setText(_translate("MainWindow", "Wicket Keeper(WK)"))
        self.WK.setText(_translate("MainWindow", "##"))
        self.label_14.setText(_translate("MainWindow", "  >"))
        self.bat_rb.setText(_translate("MainWindow", "BAT"))
        self.bow_rb.setText(_translate("MainWindow", "BOW"))
        self.ar_rb.setText(_translate("MainWindow", "AR"))
        self.wk_rb.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team Name"))
        self.team_name.setText(_translate("MainWindow", "Displayed Here"))
        self.label_9.setText(_translate("MainWindow", "Points Available "))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.label_12.setText(_translate("MainWindow", "Points Used"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.menuFile.setTitle(_translate("MainWindow", "Manage Teams"))
        self.new_t.setText(_translate("MainWindow", "NEW Team"))
        self.open_t.setText(_translate("MainWindow", "OPEN Team"))
        self.save_t.setText(_translate("MainWindow", "SAVE Team"))
        self.evaluat_t.setText(_translate("MainWindow", "EVALUATE Team"))

        # NEW FILE MENU
    def file_new(self):
        self.newDialog.show()

    def namechange(self):
        teamname = self.new_screen.team_name.text()
        fantcurs.execute("SELECT DISTINCT name FROM teams")
        l = fantcurs.fetchall()
        for i in l:
            if i[0] == teamname:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.tname = self.new_screen.team_name.text()
            self.team_name.setText(str('    '+self.tname))
            self.newDialog.close()

    #TO RESET ALL COUNTS AND LITS
    def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))
        self.list1.clear()
        self.load_names()

        self.sel_player.clear()


        #SAVE TEAM MENU
    def file_save(self):
        if not self.error():  #IF THERE IS AN ERROR
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(' Inufficient Players OR Points !!')
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()
        elif self.error():  # IF NO ERROR
            try:
                fantcurs.execute("SELECT DISTINCT name FROM teams;")
                x = fantcurs.fetchall()
                for i in x:
                    if self.team_name.text() == i[0]:   # CHECKING IF THE TEAMNAME ALREADY EXISTS
                        print('Updating already there')
                        fantcurs.execute("DELETE  FROM teams WHERE name='" + self.team_name.text() + "';") #DELETING TO UPDATE TEAM
            except:
                print('error')
            for i in range(self.sel_player.count()):
                # print('----addding--')
                # print('teamnane: ',self.team_name.text())
                # print('playername: ',self.list1[i])
                # print('points: ', player_points[self.list1[i]])
                try:
                    fantcurs.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?)",
                                     (self.team_name.text(), self.list1[i], player_points[self.list1[i]]))

                    # self.file_evaluate()
                except:
                    print('error in operation!')
            fant.commit()
        else:
            print('---error in operation')


    
   #ON RADIOBUTTONS CLICKED
    def load_names(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT player,value from stats WHERE ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,value from stats WHERE ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,value from stats WHERE ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,value from stats WHERE ctg = '" + Bowler + "';"

        fantcurs.execute(sql1)
        x = fantcurs.fetchall()
        fantcurs.execute(sql4)
        y = fantcurs.fetchall()
        fantcurs.execute(sql3)
        z = fantcurs.fetchall()
        fantcurs.execute(sql2)
        w = fantcurs.fetchall()

        batsmen = []
        bowlers = []
        allrounders = []
        wcktkeepers = []

        for k in x:
            batsmen.append(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.append(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.append(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.append(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])
        for i in self.list1:
            if i in allrounders:
                allrounders.remove(i)
            elif i in batsmen:
                batsmen.remove(i)
            elif i in bowlers:
                bowlers.remove(i)
            elif i in wcktkeepers:
                wcktkeepers.remove(i)

        if self.bat_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(batsmen)):
                item = QtWidgets.QListWidgetItem(batsmen[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)
        elif self.bow_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(bowlers)):
                item = QtWidgets.QListWidgetItem(bowlers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)
        elif self.ar_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(allrounders)):
                item = QtWidgets.QListWidgetItem(allrounders[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)

        elif self.wk_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(wcktkeepers)):
                item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)

    def removelist1(self, item):   # REMOVE FROM AVAILABLE PLAYERS AND ADD TO SELECTED PLAYERS
        self.conditions_1(item.text())
        self.av_player.takeItem(self.av_player.row(item))
        self.sel_player.addItem(item.text())
        self.totalcount = self.sel_player.count()
        self.list1.append(item.text())
        self.error()

    def conditions_1(self, cat):   # Adding and Deducting respective points from points_calculator.py
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))

    def conditions_2(self, cat):   # Adding and Deducting respective poinrs from points_calculator.py
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))

    def removelist2(self, item):   # REMOVE FROM SELECTED PLAYERS AND ADD TO AVAIALBLE PLAYERS
        self.sel_player.takeItem(self.sel_player.row(item))
        self.av_player.addItem(item.text())
        self.list1.remove(item.text())
        # self.error()
        self.totalcount = self.sel_player.count()
        self.conditions_2(item.text())

    def openteam(self):  #upon open team selected
        self.reset()
        teamname = self.open_screen.open_cb.currentText()
        self.team_name.setText(teamname)
        self.enablebuttons()
        fantcurs.execute("SELECT players from teams WHERE name= '" + teamname + "';")
        x=fantcurs.fetchall()
        score=[]
        for i in x:
            fantcurs.execute("SELECT value from stats WHERE player='"+i[0]+"';")
            y=fantcurs.fetchone()
            score.append(y[0])
        # print(score)
        sum=0
        for i in score:
            sum+=i
        self.sel_player.clear()
        self.load_names()
        for i in x:
            self.sel_player.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.openDialog.close()

    def enablebuttons(self):
        self.bat_rb.setEnabled(True)
        self.bow_rb.setEnabled(True)
        self.ar_rb.setEnabled(True)
        self.wk_rb.setEnabled(True)
        
    def disablebuttons(self):
        self.bat_rb.setEnabled(False)
        self.bow_rb.setEnabled(False)
        self.ar_rb.setEnabled(False)
        self.wk_rb.setEnabled(False)
        

    def error(self):
        msg = QMessageBox()
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            # msg.setText("Error")
            msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        elif self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No more than 11 players allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            return 0
        elif self.totalcount < 11 :
            return 0
        elif self.wicketerscount < 1:
            return 0
        elif self.avail_points <= -1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough points!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0

        return 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
