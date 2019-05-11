import sys
from PyQt4 import QtGui,QtCore


gradeDict = {
  "O":10,
  "A+":9,
  "A":8.5,
  "B+":8,
  "B":7,
  "C":6,
  "P":5,
  "F":0
}


class Window(QtGui.QWidget):
    
  def __init__(self):
    super(Window,self).__init__()
    self.initUI()
    
  
  def initUI(self):
    self.header=QtGui.QLabel("CGPA Calculator")
    self.semtext=QtGui.QLabel("Select Semester")
    self.branchtext=QtGui.QLabel("Select Branch")
    self.subject=QtGui.QLabel("Subject")
    self.grade=QtGui.QLabel("Grade")
    self.subject1=QtGui.QLabel("Subject1")
    self.subject2=QtGui.QLabel("Subject2")
    self.subject3=QtGui.QLabel("Subject3")
    self.subject4=QtGui.QLabel("Subject4")
    self.subject5=QtGui.QLabel("Subject5")
    self.subject6=QtGui.QLabel("Subject6")
    self.lab1=QtGui.QLabel("Lab1       ")
    self.lab2=QtGui.QLabel("Lab2       ")
    self.submit=QtGui.QPushButton("Calculate",self)
    self.submit.clicked.connect(self.calc_gpa)

    self.credDict = {
      self.subject1:4,
      self.subject2:4,
      self.subject3:4,
      self.subject4:4,
      self.subject5:3,
      self.subject6:3,
      self.lab1:1,
      self.lab2:1
    }

    self.semBox=QtGui.QComboBox(self)
    self.semBox.addItem("S1")
    self.semBox.addItem("S2")
    self.semBox.addItem("S3")
    self.semBox.addItem("S4")
    self.semBox.addItem("S5")
    self.semBox.addItem("S6")
    self.semBox.addItem("S7")
    self.semBox.addItem("S8")

    self.brBox=QtGui.QComboBox(self)
    self.brBox.addItem("CSE")
    self.brBox.addItem("ECE")
    self.brBox.addItem("EEE") 
    self.brBox.addItem("ME")
    self.brBox.addItem("CE")
    self.brBox.addItem("IE")
    self.brBox.addItem("AE")
    

    self.gr1=QtGui.QComboBox()
    self.gr1.addItem("O")       
    self.gr1.addItem("A+")
    self.gr1.addItem("A")
    self.gr1.addItem("B+")
    self.gr1.addItem("B")
    self.gr1.addItem("C")
    self.gr1.addItem("P")
    self.gr1.addItem("F")

    self.gr2=QtGui.QComboBox()
    self.gr2.addItem("O")       
    self.gr2.addItem("A+")
    self.gr2.addItem("A")
    self.gr2.addItem("B+")
    self.gr2.addItem("B")
    self.gr2.addItem("C")
    self.gr2.addItem("P")
    self.gr2.addItem("F")

    self.gr3=QtGui.QComboBox()
    self.gr3.addItem("O")       
    self.gr3.addItem("A+")
    self.gr3.addItem("A")
    self.gr3.addItem("B+")
    self.gr3.addItem("B")
    self.gr3.addItem("C")
    self.gr3.addItem("P")
    self.gr3.addItem("F")

    self.gr4=QtGui.QComboBox()
    self.gr4.addItem("O")       
    self.gr4.addItem("A+")
    self.gr4.addItem("A")
    self.gr4.addItem("B+")
    self.gr4.addItem("B")
    self.gr4.addItem("C")
    self.gr4.addItem("P")
    self.gr4.addItem("F")

    self.gr5=QtGui.QComboBox()
    self.gr5.addItem("O")       
    self.gr5.addItem("A+")
    self.gr5.addItem("A")
    self.gr5.addItem("B+")
    self.gr5.addItem("B")
    self.gr5.addItem("C")
    self.gr5.addItem("P")
    self.gr5.addItem("F")

    self.gr6=QtGui.QComboBox()
    self.gr6.addItem("O")       
    self.gr6.addItem("A+")
    self.gr6.addItem("A")
    self.gr6.addItem("B+")
    self.gr6.addItem("B")
    self.gr6.addItem("C")
    self.gr6.addItem("P")
    self.gr6.addItem("F")

    self.gr7=QtGui.QComboBox()
    self.gr7.addItem("O")       
    self.gr7.addItem("A+")
    self.gr7.addItem("A")
    self.gr7.addItem("B+")
    self.gr7.addItem("B")
    self.gr7.addItem("C")
    self.gr7.addItem("P")
    self.gr7.addItem("F")

    self.gr8=QtGui.QComboBox()
    self.gr8.addItem("O")       
    self.gr8.addItem("A+")
    self.gr8.addItem("A")
    self.gr8.addItem("B+")
    self.gr8.addItem("B")
    self.gr8.addItem("C")
    self.gr8.addItem("P")
    self.gr8.addItem("F")

    self.hbox=QtGui.QHBoxLayout()
    self.hbox.addStretch()
    self.hbox.addWidget(self.header)
    self.hbox.addStretch()
    self.vbox=QtGui.QVBoxLayout()
    self.vbox.addLayout(self.hbox)
    self.hbox=QtGui.QHBoxLayout()
    self.hbox.addStretch()
    self.hbox.addWidget(self.semtext)
    self.hbox.addWidget(self.semBox)
    self.hbox.addStretch()
    self.hbox.addWidget(self.branchtext)
    self.hbox.addWidget(self.brBox)
    self.hbox.addStretch()
    self.vbox.addLayout(self.hbox)
    
    # hbox=QtGui.QHBoxLayout()
    # hbox.addStretch() 
    # hbox.addWidget(subject)
    # hbox.addStretch()
    # hbox.addStretch()
    # hbox.addWidget(grade)
    # hbox.addStretch()
    # hbox.addStretch() 
    # vbox.addLayout(hbox)

    
    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.subject1,self.gr1)
    self.vbox.addLayout(self.fbox)

    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.subject2,self.gr2)
    self.vbox.addLayout(self.fbox)

    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.subject3,self.gr3)
    self.vbox.addLayout(self.fbox)

    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.subject4,self.gr4)
    self.vbox.addLayout(self.fbox)

    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.subject5,self.gr5)
    self.vbox.addLayout(self.fbox)

    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.subject6,self.gr6)
    self.vbox.addLayout(self.fbox)

    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.lab1,self.gr7)
    self.vbox.addLayout(self.fbox)

    self.fbox=QtGui.QFormLayout()
    self.fbox.addRow(self.lab2,self.gr8)
    self.vbox.addLayout(self.fbox)

    self.hbox=QtGui.QHBoxLayout()
    self.hbox.addStretch()
    self.hbox.addWidget(self.submit)
    self.hbox.addStretch()
    self.vbox.addLayout(self.hbox)

    self.vbox.addStretch()
    
    self.setLayout(self.vbox)
    self.setWindowTitle("CGPA Calculator")
    self.setGeometry(50,50,700,400)
    self.show()


  def calc_gpa(self):
    sum=0.0
    sum+=gradeDict[str(self.gr1.currentText())]*self.credDict[self.subject1] 
    sum+=gradeDict[str(self.gr2.currentText())]*self.credDict[self.subject2]  
    sum+=gradeDict[str(self.gr3.currentText())]*self.credDict[self.subject3]  
    sum+=gradeDict[str(self.gr4.currentText())]*self.credDict[self.subject4]  
    sum+=gradeDict[str(self.gr5.currentText())]*self.credDict[self.subject5]  
    sum+=gradeDict[str(self.gr6.currentText())]*self.credDict[self.subject6]  
    sum+=gradeDict[str(self.gr7.currentText())]*self.credDict[self.lab1]  
    sum+=gradeDict[str(self.gr8.currentText())]*self.credDict[self.lab2]  
    
    credSum=0
    for i in self.credDict.values():
      credSum+=i
    sum/=credSum
    # msg=QtGui.QMessageBox.information(self,"GPA","Your GPA is "+str(sum))
    msg=QtGui.QMessageBox()
    msg.setWindowTitle("GPA")
    msg.setText("Your GPA is "+str(sum))
    msg.resize(100,100)
    msg.exec_()


def run():
  app=QtGui.QApplication(sys.argv)
  GUI=Window()
  sys.exit(app.exec_())      

run()