# -*- coding: utf-8 -*-
# by TynClause


from PyQt5 import QtCore, QtGui, QtWidgets
import librosa as lr
import numpy as np
import pyqtgraph as pg
import sounddevice as sd
from scipy.signal import butter, lfilter, freqz


class Ui_Equalizer(object):
    fileName = None

    def setupUi(self, Equalizer):
        self.UpdateFromSpinbox = False
        Equalizer.setObjectName("Equalizer")
        Equalizer.resize(796, 712)
        Equalizer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Equalizer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 9, 751, 72))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Judul = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(40)
        font.setItalic(True)
        self.Judul.setFont(font)
        self.Judul.setAlignment(QtCore.Qt.AlignCenter)
        self.Judul.setObjectName("Judul")
        self.verticalLayout.addWidget(self.Judul)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(20, 100, 751, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.C1 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.C1.setOrientation(QtCore.Qt.Vertical)
        self.C1.setObjectName("C1")
        self.horizontalLayout.addWidget(self.C1)
        # =======================================
        self.C1.setRange(0, 100)
        self.C1.valueChanged[int].connect(self.update_spinbox_C1)
        # =======================================
        self.C2 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.C2.setOrientation(QtCore.Qt.Vertical)
        self.C2.setObjectName("C2")
        self.horizontalLayout.addWidget(self.C2)
        # =======================================
        self.C2.setRange(0, 100)
        self.C2.valueChanged[int].connect(self.update_spinbox_C2)
        # =======================================
        self.C3 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.C3.setOrientation(QtCore.Qt.Vertical)
        self.C3.setObjectName("C3")
        self.horizontalLayout.addWidget(self.C3)
        # =======================================
        self.C3.setRange(0, 100)
        self.C3.valueChanged[int].connect(self.update_spinbox_C3)
        # =======================================
        self.C4 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.C4.setOrientation(QtCore.Qt.Vertical)
        self.C4.setObjectName("C4")
        self.horizontalLayout.addWidget(self.C4)
        # =======================================
        self.C4.setRange(0, 100)
        self.C4.valueChanged[int].connect(self.update_spinbox_C4)
        # =======================================
        self.C5 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.C5.setOrientation(QtCore.Qt.Vertical)
        self.C5.setObjectName("C5")
        self.horizontalLayout.addWidget(self.C5)
        # =======================================
        self.C5.setRange(0, 100)
        self.C5.valueChanged[int].connect(self.update_spinbox_C5)
        # =======================================
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(90, 390, 621, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 330, 51, 34))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(230, 330, 65, 34))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(360, 330, 71, 34))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(490, 330, 77, 34))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(620, 330, 75, 34))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 300, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        # ========================================
        self.doubleSpinBox.setRange(0.0, 100.0)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.editingFinished.connect(
            self.update_slider_position_C1)
        # ========================================
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(230, 300, 62, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        # ========================================
        self.doubleSpinBox_2.setRange(0.0, 100.0)
        self.doubleSpinBox_2.setDecimals(2)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.editingFinished.connect(
            self.update_slider_position_C2)
        # ========================================
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(370, 300, 62, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        # ========================================
        self.doubleSpinBox_3.setRange(0.0, 100.0)
        self.doubleSpinBox_3.setDecimals(2)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.editingFinished.connect(
            self.update_slider_position_C3)
        # ========================================
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(500, 300, 62, 22))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        # ========================================
        self.doubleSpinBox_4.setRange(0.0, 100.0)
        self.doubleSpinBox_4.setDecimals(2)
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_4.editingFinished.connect(
            self.update_slider_position_C4)
        # ========================================
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(630, 300, 62, 22))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        # ========================================
        self.doubleSpinBox_5.setRange(0.0, 100.0)
        self.doubleSpinBox_5.setDecimals(2)
        self.doubleSpinBox_5.setSingleStep(0.1)
        self.doubleSpinBox_5.editingFinished.connect(
            self.update_slider_position_C5)
        # ========================================
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 490, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 630, 81, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(330, 370, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(40, 650, 711, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        Equalizer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Equalizer)
        self.statusbar.setObjectName("statusbar")
        Equalizer.setStatusBar(self.statusbar)

        self.retranslateUi(Equalizer)
        QtCore.QMetaObject.connectSlotsByName(Equalizer)

    def update_spinbox_C1(self, value):
        self.doubleSpinBox.setValue(float(value)/100)

    def update_spinbox_C2(self, value):
        self.doubleSpinBox_2.setValue(float(value)/100)

    def update_spinbox_C3(self, value):
        self.doubleSpinBox_3.setValue(float(value)/100)

    def update_spinbox_C4(self, value):
        self.doubleSpinBox_4.setValue(float(value)/100)

    def update_spinbox_C5(self, value):
        self.doubleSpinBox_5.setValue(float(value)/100)

    def update_slider_position_C1(self):
        self.UpdateFromSpinbox = True
        self.C1.setSliderPosition(self.doubleSpinBox.value()*100)
        self.UpdateFromSpinbox = False

    def update_slider_position_C2(self):
        self.UpdateFromSpinbox = True
        self.C2.setSliderPosition(self.doubleSpinBox_2.value()*100)
        self.UpdateFromSpinbox = False

    def update_slider_position_C3(self):
        self.UpdateFromSpinbox = True
        self.C3.setSliderPosition(self.doubleSpinBox_3.value()*100)
        self.UpdateFromSpinbox = False

    def update_slider_position_C4(self):
        self.UpdateFromSpinbox = True
        self.C4.setSliderPosition(self.doubleSpinBox_4.value()*100)
        self.UpdateFromSpinbox = False

    def update_slider_position_C5(self):
        self.UpdateFromSpinbox = True
        self.C5.setSliderPosition(self.doubleSpinBox_5.value()*100)
        self.UpdateFromSpinbox = False

    def retranslateUi(self, Equalizer):
        _translate = QtCore.QCoreApplication.translate
        Equalizer.setWindowTitle(_translate("Equalizer", "MainWindow"))
        self.Judul.setText(_translate("Equalizer", "EQUALIZER"))
        self.label.setText(_translate("Equalizer", "C1"))
        self.label_2.setText(_translate("Equalizer", "Low"))
        self.label_3.setText(_translate("Equalizer", "C2"))
        self.label_4.setText(_translate("Equalizer", "Band 4-8 kHz"))
        self.label_5.setText(_translate("Equalizer", "C3"))
        self.label_6.setText(_translate("Equalizer", "Band 9-13 kHz"))
        self.label_7.setText(_translate("Equalizer", "C4"))
        self.label_8.setText(_translate("Equalizer", "Band 13-17 kHz"))
        self.label_9.setText(_translate("Equalizer", "C5"))
        self.label_10.setText(_translate("Equalizer", "High frequency"))
        self.label_11.setText(_translate("Equalizer", "Magnitude [dB]"))
        self.label_12.setText(_translate("Equalizer", "Time (s)"))
        self.label_13.setText(_translate(
            "Equalizer", "vizualize equalizer audio"))
        self.pushButton.setText(_translate("Equalizer", "Load"))
        self.pushButton_2.setText(_translate("Equalizer", "Plot"))
        self.pushButton_3.setText(_translate("Equalizer", "Reset"))
        self.pushButton_4.setText(_translate("Equalizer", "Play"))
        self.pushButton_5.setText(_translate("Equalizer", "Stop"))

        self.pushButton.clicked.connect(self.inputSound)
        self.pushButton_2.clicked.connect(self.plotSound)
        self.pushButton_3.clicked.connect(self.resetSound)
        self.pushButton_4.clicked.connect(self.playSound)
        self.pushButton_5.clicked.connect(self.stopSound)

    def inputSound(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Select Sound', r"\.", 'Sound Files(*.wav)')
        if self.fileName != '':
            self.audio, self.sfreq = lr.load(self.fileName)
            self.time = np.arange(0, len(self.audio)) / self.sfreq
            self.graphicsView.plot(self.time, self.audio)
        else:
            return

    def plotSound(self):
        if self.fileName:
            self.audio = np.zeros_like(self.audio)
            self.graphicsView.clear()
            self.graphicsView.plot(self.time, self.audio)
        else:
            pass

    def resetSound(self):
        if self.fileName:
            self.fileName = None
            self.audio = None
            self.time = None
            self.graphicsView.clear()
            self.graphicsView = pg.PlotWidget(self.centralwidget)
        else:
            pass

    def playSound(self):
        if self.fileName:
            sd.play(self.audio, self.sfreq)
        else:
            pass

    def stopSound(self):
        if self.fileName:
            sd.stop()

    def


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Equalizer = QtWidgets.QMainWindow()
    ui = Ui_Equalizer()
    ui.setupUi(Equalizer)
    Equalizer.show()
    sys.exit(app.exec_())
