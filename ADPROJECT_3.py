import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("Mydesign.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Clear_mv.clicked.connect(self.clearbuttonfunction)
        self.Loadcloud.clicked.connect(self.loadImageFromFile)
        self.rB_action.clicked.connect(self.radiobuttonclicked)
        self.rB_comedy.clicked.connect(self.radiobuttonclicked)
        self.rB_fantasy.clicked.connect(self.radiobuttonclicked)
        self.rB_mello.clicked.connect(self.radiobuttonclicked)

    def loadImageFromFile(self) :
        #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("testImage.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
        self.Picture.setPixmap(self.qPixmapFileVar)

    def radiobuttonclicked(self):
        #각각 버튼들이 눌릴 때 QComboBox에 장르에 따른 영화 리스트가 들어가게끔 함.
        Action_List = ["런", "800"]
        Comedy_List = ["이웃사촌", "그날이 온다", "더 프롬", "삼진그룹 영어토익반", "프리키 데스데이 순한맛"]
        Fantasy_List = ["미드나이트 스카이", "극장판 바이올렛 에버가든"]
        Mello_List = ["조제", "노트북"]
        if self.rB_action.ischecked:
            for i in range(1,len(Action_List)+1):
                self.MovieList.additem(Action_List[i-1])
        elif self.rB_comedy.ischecked:
            for i in range(1,len(Comedy_List)+1):
                self.MovieList.additem(Comedy_List[i-1])
        elif self.rB_fantasy.ischecked:
            for i in range(1,len(Fantasy_List)+1):
                self.MovieList.additem(Fantasy_List[i-1])
        elif self.rB_mello.ischecked:
            for i in range(1,len(Mello_List)+1):
                self.MovieList.additem(Mello_List[i-1])

    def clearbuttonfunction(self):
        #Clear CB버튼이 눌릴 때 콤보박스의 아이템들이 지워지게함.
        self.MovieList.clear()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 