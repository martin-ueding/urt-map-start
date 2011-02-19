#!/usr/bin/python
import glob
import re
import os
import random
from PyQt4 import QtCore, QtGui
from listui import Ui_Dialog
import sys

mapnames = []
	
def printRandomMapName ():
	print random.choice(mapnames)

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
	QtGui.QWidget.__init__(self, parent)
	self.ui = Ui_Dialog()
	self.ui.setupUi(self)
	QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.printSelectedMap)
	maps = glob.glob('/home/mu/.q3a/q3ut4/*.pk3')
	for map in maps:
		m = re.search('(?:.*/)+([^/]+)\\.pk3', map)
		mapnames.append(m.group(1))
	
	mapnames.sort()

	for map in mapnames:
		self.ui.mapList.addItem(map)

  def printSelectedMap (self):
	row = self.ui.mapList.currentRow()
	print mapnames[row]

	os.system('/opt/UrbanTerror/ioUrbanTerror.i386 +map '+mapnames[row])


if __name__ == "__main__":	
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())

