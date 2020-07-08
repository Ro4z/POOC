import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from video_module import ShowVideo, ImageViewer


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, layout_widget):
        QtWidgets.QMainWindow.__init__(self)
        self.setCentralWidget(layout_widget)
        button1 = QtWidgets.QPushButton('Show messagebox', self)
        button1.clicked.connect(self.click_method)
        button1.resize(200,64)
        button1.move(50,50)

    def click_method(self):
        QtWidgets.QMessageBox.about(self, "Title", "Content")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)
    #
    # thread2 = QtCore.QThread()
    # thread2.start()
    # keyDetector = KeyDetector()
    # keyDetector.moveToThread(thread)

    image_viewer1 = ImageViewer()
    image_viewer2 = ImageViewer()

    vid.VideoSignal1.connect(image_viewer1.set_image)
    vid.VideoSignal2.connect(image_viewer2.set_image)

    push_button1 = QtWidgets.QPushButton('Start')
    push_button2 = QtWidgets.QPushButton('Exit')
    push_button1.clicked.connect(vid.start_video)

    push_button2.clicked.connect(vid.exit)

    vertical_layout = QtWidgets.QVBoxLayout()
    horizontal_layout = QtWidgets.QHBoxLayout()
    horizontal_layout.addWidget(image_viewer1)
    horizontal_layout.addWidget(image_viewer2)
    vertical_layout.addLayout(horizontal_layout)
    vertical_layout.addWidget(push_button1)
    vertical_layout.addWidget(push_button2)

    layout_widget = QtWidgets.QWidget()
    layout_widget.setLayout(vertical_layout)

    # main_window = QtWidgets.QMainWindow()
    main_window = MainWindow(layout_widget)
    # main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())