import sys
import glob
import vlc
#import threading

from PyQt5.QtGui import QPixmap
import eyed3
from PyQt5 import QtWidgets

import mainForm

currentSound = ""
songStatus = False

song = vlc.MediaPlayer()
index = 0
maxIndex = 0



def getIDv3(str):
    track = eyed3.load(str)
    for image in track.tag.images:
        image_file = open("temp.jpg", "wb")
        image_file.write(image.image_data)
        image_file.close()
      
    return [track.tag.title,track.tag.artist,track.tag.album, track.info.time_secs]

class MP3(QtWidgets.QMainWindow,mainForm.Ui_MainWindow):
    
    #sec = 0
    #tick = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.prev)
        self.pushButton_3.clicked.connect(self.play)
        self.pushButton.clicked.connect(self.next)
        
        self.actionAdd_File.triggered.connect(self.addFile)
        self.actionAdd_Folder.triggered.connect(self.addFolder)
        #self.tick = threading.Timer(1, self.ticker)


    def prev(self):
        global index
        
        temp = self.listWidget.item(index-1)
        
        if temp:
            text = getIDv3(temp.text())
            index-=1
            self.setLabel(text)
            self.playSong(self.listWidget.currentItem().text())
    
    def play(self):
        
        global index
        
        if self.listWidget.currentItem():

            text = getIDv3(self.listWidget.currentItem().text())
            index = self.listWidget.currentRow()

            self.setLabel(text)

            self.playSong(self.listWidget.currentItem().text())




    def next(self):
        global index
        
        temp = self.listWidget.item(index+1)
        
        if temp:
            text = getIDv3(temp.text())
            index+=1
            self.setLabel(text)
            self.playSong(self.listWidget.currentItem().text())


    def playSong(self,text):
        global currentSound

        if currentSound==text:
            if songStatus:
                song.play()
                #self.tick.start()
            else:
                #self.tick.cancel()
                song.pause()
                
        else:
            #self.tick.cancel()
            #self.sec=0
            currentSound = text
            song.set_mrl(text)
            song.play()
            #self.tick.start()        



    def setLabel(self, text):
        self.listWidget.setCurrentRow(index)
        time = str(int(text[3]/60)) + ":" + str(int(text[3]%60))
        self.label_3.setText(time)
        self.label_5.setText(text[0])
        self.label_2.setText(text[1])
        self.label_6.setText(text[2])
        self.label.setPixmap(QPixmap("temp.jpg"))
        self.label.setScaledContents(True)

    def ticker(self):
        
        self.sec+=1
        self.label_4.setText(str(int(self.sec/60)) + ":" + str(int(self.sec%60)))
        print(self.sec)


    
    def addFile(self):
        global maxIndex
        
        
        #self.listWidget.clear()
        
        ofd = QtWidgets.QFileDialog()
        ofd.setFileMode(QtWidgets.QFileDialog.AnyFile)
        #ofd.setNameFilters(["MP3 files (*.mp3)"])
        #ofd.selectNameFilter("MP3 files (*.mp3)")
        
        directory = ofd.getOpenFileNames(self,"Couse Files", "/home/kali/Desktop/mp3/BassitJaEbal/","MP3 files (*.mp3)")

        if directory:
            for file_name in directory[0]:
                self.listWidget.addItem(file_name)

        maxIndex = self.listWidget.count()
        


    def addFolder(self):
        global maxIndex
        
        #self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Chouse Folder","/home/kali/Desktop/mp3/BassitJaEbal/")
        
        if directory:
            for file_name in glob.glob(directory+"/*.mp3"):
                self.listWidget.addItem(file_name)
        
        maxIndex = self.listWidget.count()





def main():
    app = QtWidgets.QApplication(sys.argv)
    widnow = MP3()
    widnow.show()
    app.exec_()

if __name__ == '__main__':
    main()