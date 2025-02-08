
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Kategori(object):
    def setupUi(self, Kategori):
        Kategori.setObjectName("Kategori")
        Kategori.resize(478, 249)

        # Horizontal Layout for Buttons
        self.horizontalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButtonInsert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonInsert.setFont(font)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.horizontalLayout.addWidget(self.pushButtonInsert)

        # Vertical Layout for Input Fields
        self.verticalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 10, 281, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEditId = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditId.setFont(font)
        self.lineEditId.setObjectName("lineEditId")
        self.verticalLayout.addWidget(self.lineEditId)

        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout.addWidget(self.lineEditName)

        # Vertical Layout for Labels
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 151, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.labelId = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelId.setFont(font)
        self.labelId.setObjectName("labelId")
        self.verticalLayout_2.addWidget(self.labelId)

        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.verticalLayout_2.addWidget(self.labelName)

        # Result Label
        self.labelResult = QtWidgets.QLabel(Kategori)
        self.labelResult.setGeometry(QtCore.QRect(10, 220, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")

        # Connect Insert Button to Function
        self.pushButtonInsert.clicked.connect(self.insertkategori)

        self.retranslateUi(Kategori)
        QtCore.QMetaObject.connectSlotsByName(Kategori)

    def insertkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()
            sql = "INSERT INTO kategori (id, nama) VALUES (%s, %s)"
            val = (idkat, namekat)
            cursor.execute(sql, val)
            mydb.commit()
            self.labelResult.setText("Data Kategori Berhasil Disimpan")
            self.lineEditId.setText("")
            self.lineEditName.setText("")
        except mc.Error as e:
            self.labelResult.setText("Data Kategori Gagal Disimpan")

    def retranslateUi(self, Kategori):
        _translate = QtCore.QCoreApplication.translate
        Kategori.setWindowTitle(_translate("Kategori", "Form Kategori"))
        self.pushButtonInsert.setText(_translate("Kategori", "INSERT DATA"))
        self.labelId.setText(_translate("Kategori", "ID Kategori"))
        self.labelName.setText(_translate("Kategori", "Nama Kategori"))
        self.labelResult.setText(_translate("Kategori", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kategori = QtWidgets.QWidget()
    ui = Ui_Kategori()
    ui.setupUi(Kategori)
    Kategori.show()
    sys.exit(app.exec_())
