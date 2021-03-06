import librosa as lr
import numpy as np
import pyqtgraph as pg
import sounddevice as sd
from scipy import signal
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Equalizer(object):
    fileName = None
    nyquist = 0

    def setupUi(self, Equalizer):
        Equalizer.setObjectName("Equalizer")
        Equalizer.resize(796, 724)
        Equalizer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Equalizer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 271, 61))
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
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 390, 371, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 330, 88, 34))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(100, 330, 90, 34))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(200, 330, 93, 34))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(310, 330, 93, 34))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(30, 300, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setRange(0, 1)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setSingleStep(1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(110, 300, 62, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setRange(0.0, 1)
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setSingleStep(1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(230, 290, 62, 22))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_4.setRange(0.0, 1)
        self.doubleSpinBox_4.setDecimals(0)
        self.doubleSpinBox_4.setSingleStep(1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(350, 290, 62, 22))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.doubleSpinBox_6.setRange(0.0, 1)
        self.doubleSpinBox_6.setDecimals(0)
        self.doubleSpinBox_6.setSingleStep(1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(160, 620, 81, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
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
        self.pushButton_6 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
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
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(
            QtCore.QRect(190, 130, 31, 191))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.C3 = QtWidgets.QSlider(self.verticalLayoutWidget_6)
        self.C3.setOrientation(QtCore.Qt.Vertical)
        self.C3.setObjectName("C3")
        self.verticalLayout_6.addWidget(self.C3)
        self.C3.setRange(0, 1)
        self.C3.valueChanged[int].connect(
            self.update_spinbox_C3)
        self.C4 = QtWidgets.QSlider(self.verticalLayoutWidget_6)
        self.C4.setOrientation(QtCore.Qt.Vertical)
        self.C4.setObjectName("C4")
        self.verticalLayout_6.addWidget(self.C4)
        self.C4.setRange(0, 1)
        self.C4.valueChanged[int].connect(
            self.update_spinbox_C4)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(
            QtCore.QRect(310, 130, 31, 191))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.C5 = QtWidgets.QSlider(self.verticalLayoutWidget_7)
        self.C5.setOrientation(QtCore.Qt.Vertical)
        self.C5.setObjectName("C5")
        self.verticalLayout_7.addWidget(self.C5)
        self.C5.setRange(0, 1)
        self.C5.valueChanged[int].connect(
            self.update_spinbox_C5)
        self.C6 = QtWidgets.QSlider(self.verticalLayoutWidget_7)
        self.C6.setOrientation(QtCore.Qt.Vertical)
        self.C6.setObjectName("C6")
        self.verticalLayout_7.addWidget(self.C6)
        self.C6.setRange(0, 1)
        self.C6.valueChanged[int].connect(
            self.update_spinbox_C6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 170, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 270, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 170, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 270, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(40, 120, 31, 171))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.C1 = QtWidgets.QSlider(self.verticalLayoutWidget_8)
        self.C1.setOrientation(QtCore.Qt.Vertical)
        self.C1.setObjectName("C1")
        self.verticalLayout_8.addWidget(self.C1)
        self.C1.setRange(0, 1)
        self.C1.valueChanged[int].connect(
            self.update_spinbox_C1)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(
            QtCore.QRect(130, 120, 31, 171))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.C2 = QtWidgets.QSlider(self.verticalLayoutWidget_9)
        self.C2.setOrientation(QtCore.Qt.Vertical)
        self.C2.setObjectName("C2")
        self.verticalLayout_9.addWidget(self.C2)
        self.C2.setRange(0, 1)
        self.C2.valueChanged[int].connect(
            self.update_spinbox_C2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 100, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 100, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(230, 190, 62, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setRange(0.0, 1)
        self.doubleSpinBox_3.setDecimals(0)
        self.doubleSpinBox_3.setSingleStep(1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(350, 190, 62, 22))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_5.setRange(0.0, 1)
        self.doubleSpinBox_5.setDecimals(0)
        self.doubleSpinBox_5.setSingleStep(1)
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(420, 390, 351, 231))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(550, 80, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.graphicsView_3 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(450, 100, 331, 241))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(560, 620, 81, 16))
        self.label_16.setObjectName("label_16")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(170, 370, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 370, 101, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(610, 350, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(430, 200, 47, 13))
        self.label_17.setObjectName("label_17")
        Equalizer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Equalizer)
        self.statusbar.setObjectName("statusbar")
        Equalizer.setStatusBar(self.statusbar)

        self.retranslateUi(Equalizer)
        QtCore.QMetaObject.connectSlotsByName(Equalizer)

    def update_spinbox_C1(self, value):  # function update value spinbox C1
        self.doubleSpinBox.setValue(int(value))

    def update_spinbox_C2(self, value):  # function update value spinbox C2
        self.doubleSpinBox_2.setValue(int(value))

    def update_spinbox_C3(self, value):  # function update value spinbox C3
        self.doubleSpinBox_3.setValue(int(value))

    def update_spinbox_C4(self, value):  # function update value spinbox C4
        self.doubleSpinBox_4.setValue(int(value))

    def update_spinbox_C5(self, value):  # function update value spinbox C5
        self.doubleSpinBox_5.setValue(int(value))

    def update_spinbox_C6(self, value):  # function update value spinbox C6
        self.doubleSpinBox_6.setValue(int(value))

    # function update position slider C1
    def update_slider_position_C1(self):
        self.UpdateFromSpinbox = True
        self.C1.setSliderPosition(self.doubleSpinBox.value())
        self.UpdateFromSpinbox = False

    # function update position slider C2
    def update_slider_position_C2(self):
        self.UpdateFromSpinbox = True
        self.C2.setSliderPosition(self.doubleSpinBox_2.value())
        self.UpdateFromSpinbox = False

    # function update position slider C3
    def update_slider_position_C3(self):
        self.UpdateFromSpinbox = True
        self.C3.setSliderPosition(self.doubleSpinBox_3.value())
        self.UpdateFromSpinbox = False

    # function update position slider C4
    def update_slider_position_C4(self):
        self.UpdateFromSpinbox = True
        self.C4.setSliderPosition(self.doubleSpinBox_4.value())
        self.UpdateFromSpinbox = False

    # function update position slider C5
    def update_slider_position_C5(self):
        self.UpdateFromSpinbox = True
        self.C5.setSliderPosition(self.doubleSpinBox_5.value())
        self.UpdateFromSpinbox = False

    # function update position slider C4
    def update_slider_position_C6(self):
        self.UpdateFromSpinbox = True
        self.C6.setSliderPosition(self.doubleSpinBox_6.value())
        self.UpdateFromSpinbox = False

    def retranslateUi(self, Equalizer):
        _translate = QtCore.QCoreApplication.translate
        Equalizer.setWindowTitle(_translate("Equalizer", "MainWindow"))
        self.Judul.setText(_translate("Equalizer", "EQUALIZER"))
        self.label.setText(_translate("Equalizer", "Low Pass Filter"))
        self.label_3.setText(_translate("Equalizer", "High Pass Filter"))
        self.label_5.setText(_translate("Equalizer", "Band Pass Filter"))
        self.label_7.setText(_translate("Equalizer", "Band Stop Filter"))
        self.label_12.setText(_translate("Equalizer", "Time (s)"))
        self.pushButton.setText(_translate("Equalizer", "Load"))
        self.pushButton_6.setText(_translate("Equalizer", "Reset"))
        self.pushButton_2.setText(_translate("Equalizer", "Plot"))
        self.pushButton_3.setText(_translate("Equalizer", "Clear"))
        self.pushButton_4.setText(_translate("Equalizer", "Play"))
        self.pushButton_5.setText(_translate("Equalizer", "Stop"))
        self.label_2.setText(_translate("Equalizer", "High Cut (Hz)"))
        self.label_4.setText(_translate("Equalizer", "Low Cut (Hz)"))
        self.label_6.setText(_translate("Equalizer", "High Cut (Hz)"))
        self.label_8.setText(_translate("Equalizer", "Low Cut (Hz)"))
        self.label_9.setText(_translate("Equalizer", "Cut Off (Hz)"))
        self.label_10.setText(_translate("Equalizer", "Cut Off (Hz)"))
        self.label_15.setText(_translate("Equalizer", "Chevy 1 filter(A)"))
        self.label_16.setText(_translate("Equalizer", "Time (s)"))
        self.label_11.setText(_translate("Equalizer", "Butter Filter(A)"))
        self.label_13.setText(_translate(
            "Equalizer", "Raw Audio(A) Base"))
        self.label_14.setText(_translate("Equalizer", "Time (s)"))
        self.label_17.setText(_translate("Equalizer", ""))

        self.pushButton.clicked.connect(
            self.inputSound)    # action clicked for load
        self.pushButton_2.clicked.connect(
            self.plotSound)   # action clicked for plot
        self.pushButton_3.clicked.connect(
            self.clearSound)  # action clicked for reset
        self.pushButton_4.clicked.connect(
            self.playSound)   # action clicked for play
        self.pushButton_5.clicked.connect(
            self.stopSound)   # action clicked for stop
        self.pushButton_6.clicked.connect(
            self.resetSound)

    def resetSound(self):
        if self.fileName:
            self.audio = self.audio_temp
            self.graphicsView.clear()
            self.graphicsView_3.clear()
            self.graphicsView_3.plot(self.time, self.audio)
            self.graphicsView.plot(self.time, self.audio)

        else:
            pass

    def inputSound(self):   # function for input sound
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Select Sound', r"\.", 'Sound Files(*.wav)')
        if self.fileName != '':
            self.audio, self.sfreq = lr.load(self.fileName)
            self.nyquist = (0.5 * self.sfreq)
            self.audio_temp = self.audio
            self.C1.setRange(0, self.nyquist)
            self.C2.setRange(0, self.nyquist)
            self.C3.setRange(0, self.nyquist)
            self.C4.setRange(0, self.nyquist)
            self.C5.setRange(0, self.nyquist)
            self.C6.setRange(0, self.nyquist)
            self.doubleSpinBox.setRange(0.0, self.nyquist)
            self.doubleSpinBox_2.setRange(0.0, self.nyquist)
            self.doubleSpinBox_3.setRange(0.0, self.nyquist)
            self.doubleSpinBox_4.setRange(0.0, self.nyquist)
            self.doubleSpinBox_5.setRange(0.0, self.nyquist)
            self.doubleSpinBox_6.setRange(0.0, self.nyquist)
            self.time = np.arange(0, len(self.audio)) / self.sfreq
            self.graphicsView.plot(self.time, self.audio)
            self.graphicsView_2.plot(self.time, self.audio)
            self.graphicsView_3.plot(self.time, self.audio)
        else:
            return

    def plotSound(self):    # function for plot visual audio
        if self.fileName:
            if self.doubleSpinBox.value() == 0 or self.doubleSpinBox.value() > self.nyquist:
                pass
            else:
                sos = signal.butter(100, int(self.doubleSpinBox.value()),
                                    'lowpass', fs=self.sfreq, output='sos')
                sos_chevy = signal.cheby1(100, 1, int(self.doubleSpinBox.value()),
                                          'lowpass', fs=self.sfreq, output='sos')
                self.audio = signal.sosfilt(sos, self.audio)
                self.audio_chevy = signal.sosfilt(sos_chevy, self.audio)
                self.graphicsView.clear()
                self.graphicsView_3.clear()
                self.graphicsView.plot(self.time, self.audio)
                self.graphicsView_3.plot(self.time, self.audio_chevy)

            if self.doubleSpinBox_2.value() == 0 or self.doubleSpinBox_2.value() > self.nyquist:
                pass
            else:
                sos1 = signal.butter(100, int(self.doubleSpinBox_2.value()),
                                     'highpass', fs=self.sfreq, output='sos')
                sos_chevy1 = signal.cheby1(100, 1, int(self.doubleSpinBox_2.value()),
                                           'highpass', fs=self.sfreq, output='sos')
                self.audio = signal.sosfilt(sos1, self.audio)
                self.audio_chevy = signal.sosfilt(sos_chevy1, self.audio)
                self.graphicsView.clear()
                self.graphicsView_3.clear()
                self.graphicsView.plot(self.time, self.audio)
                self.graphicsView_3.plot(self.time, self.audio_chevy)

            if self.doubleSpinBox_3.value() == 0 or self.doubleSpinBox_3.value() > self.nyquist\
                    and self.doubleSpinBox_4.value() == 0 or self.doubleSpinBox_4.value() > self.nyquist:
                pass
            else:
                sos2 = signal.butter(
                    100, [int(self.doubleSpinBox_4.value()), int(self.doubleSpinBox_3.value())], 'bandpass', fs=self.sfreq, output='sos')
                sos_chevy2 = signal.cheby1(100, 1, [int(self.doubleSpinBox_4.value()), int(self.doubleSpinBox_3.value())],
                                           'bandpass', fs=self.sfreq, output='sos')
                self.audio = signal.sosfilt(sos2, self.audio)
                self.audio_chevy = signal.sosfilt(sos_chevy2, self.audio)
                self.graphicsView.clear()
                self.graphicsView_3.clear()
                self.graphicsView.plot(self.time, self.audio)
                self.graphicsView_3.plot(self.time, self.audio_chevy)

            if self.doubleSpinBox_5.value() == 0 or self.doubleSpinBox_5.value() > self.nyquist\
                    and self.doubleSpinBox_4.value() == 0 or self.doubleSpinBox_4.value() > self.nyquist:
                pass
            else:
                sos3 = signal.butter(
                    100, [int(self.doubleSpinBox_6.value()), int(self.doubleSpinBox_5.value())], 'bandstop', fs=self.sfreq, output='sos')
                sos_chevy3 = signal.cheby1(100, 1, [int(self.doubleSpinBox_6.value()), int(self.doubleSpinBox_5.value())],
                                           'bandstop', fs=self.sfreq, output='sos')
                self.audio = signal.sosfilt(sos3, self.audio)
                self.audio_chevy = signal.sosfilt(sos_chevy3, self.audio)
                self.graphicsView.clear()
                self.graphicsView_3.clear()
                self.graphicsView.plot(self.time, self.audio)

        else:
            pass

    def clearSound(self):   # function for clear audio
        if self.fileName:
            self.fileName = ''
            self.audio = None
            self.time = None
            self.graphicsView.clear()
            self.graphicsView_2.clear()
        else:
            pass

    def playSound(self):    # function for play audio
        if self.fileName:
            sd.play(self.audio, self.sfreq)
        else:
            pass

    def stopSound(self):    # function for stop audio
        if self.fileName:
            sd.stop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Equalizer = QtWidgets.QMainWindow()
    ui = Ui_Equalizer()
    ui.setupUi(Equalizer)
    Equalizer.show()
    sys.exit(app.exec_())
