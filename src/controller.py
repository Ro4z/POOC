from src.page.LoginPage import LoginPage
from src.page.MainPage import MainPage
from src.page.LogPage import LogPage
from src.page.PreViewPage import PreViewPage
from src.page.NoticePage import NoticePage
from src.page.ExamPage import ExamPage
from src.page.ResultPage import ResultPage
from PyQt5 import QtWidgets


class Controller:
    def __init__(self):
        self.login_page = LoginPage()
        self.main_page = MainPage()
        self.log_page = LogPage()
        self.preview_page = PreViewPage()
        self.notice_page = NoticePage()
        self.exam_page = ExamPage()
        self.result_page = ResultPage()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()
        self.LogForm = QtWidgets.QWidget()
        self.PreviewForm = QtWidgets.QWidget()
        self.NoticeForm = QtWidgets.QWidget()
        self.ResultForm = QtWidgets.QWidget()


    def show_login_page(self):
        self.MainForm.close()
        self.login_page.setupUi(self.LoginForm)
        self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.LoginForm.show()

    def show_main_page(self):
        self.LoginForm.close()
        self.LogForm.close()
        self.PreviewForm.close()
        self.ResultForm.close()
        self.main_page.setupUi(self.MainForm)
        self.main_page.switch_window_to_login.connect(self.show_login_page)
        self.main_page.switch_window_to_log.connect(self.show_log_page)
        self.main_page.switch_window_to_preview.connect(self.show_preview_page)
        self.MainForm.show()

    def show_log_page(self):
        self.MainForm.close()
        self.log_page.setupUi(self.LogForm)
        self.log_page.switch_window_to_main.connect(self.show_main_page)
        self.LogForm.show()

    def show_preview_page(self):
        self.MainForm.close()
        self.preview_page.setupUi(self.PreviewForm)
        self.preview_page.switch_window_to_main.connect(self.show_main_page)
        self.preview_page.switch_window_to_notice.connect(self.show_notice_page)
        self.PreviewForm.show()

    def show_notice_page(self):
        self.PreviewForm.close()
        self.notice_page.setupUi(self.NoticeForm)
        self.notice_page.switch_window_to_exam.connect(self.show_exam_page)
        self.NoticeForm.show()

    def show_exam_page(self):
        self.NoticeForm.close()
        self.exam_page.switch_window_to_result.connect(self.show_result_page)
        self.exam_page.show()

    def show_result_page(self):
        self.exam_page.close()
        self.result_page.setupUi(self.ResultForm)
        self.result_page.switch_window_to_main.connect(self.show_main_page)
        self.ResultForm.show()