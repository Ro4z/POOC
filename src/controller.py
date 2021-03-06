from src.page.LoginPage import LoginPage
from src.page.MainPage import MainPage
from src.page.LogPage import LogPage
from src.page.PreViewPage import PreViewPage
from src.page.NoticePage import NoticePage
from src.page.IdentifyPage import IdenPage
from src.page.ExamPage import ExamPage
from src.page.ResultPage import ResultPage
from src.page.ExamPage import log_list

from PyQt5 import QtWidgets

class Controller:
    def __init__(self):
        self.login_page = LoginPage()
        self.main_page = MainPage()
        self.log_page = LogPage()
        self.preview_page = PreViewPage()
        self.notice_page = NoticePage()
        self.iden_page = IdenPage()
        self.exam_page = ExamPage()
        self.result_page = ResultPage()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()
        self.LogForm = QtWidgets.QWidget()
        self.PreviewForm = QtWidgets.QWidget()
        self.NoticeForm = QtWidgets.QWidget()
        self.IdenForm = QtWidgets.QWidget()
        self.ExamForm = QtWidgets.QWidget()
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
        self.log_page.setupUi(self.LogForm)
        self.main_page.setupUi(self.MainForm)
        self.main_page.switch_window_to_login.connect(self.show_login_page)
        self.main_page.switch_window_to_log.connect(self.show_log_page)
        self.main_page.switch_window_to_preview.connect(self.show_preview_page)
        self.MainForm.show()

    def show_log_page(self):
        self.MainForm.close()
        self.log_page.setupUi(self.LogForm)
        self.LogForm.show()
        self.log_page.switch_window_to_main.connect(self.show_main_page)

    def show_preview_page(self):
        self.MainForm.close()
        self.preview_page.setupUi(self.PreviewForm)
        self.preview_page.start_timer()
        self.preview_page.switch_window_to_main.connect(self.show_main_page)
        self.preview_page.switch_window_to_notice.connect(self.show_notice_page)
        self.PreviewForm.show()

    def show_notice_page(self):
        self.preview_page.stop_timer()
        self.PreviewForm.close()
        self.notice_page.setupUi(self.NoticeForm)
        self.notice_page.switch_window_to_iden.connect(self.show_iden_page)
        self.NoticeForm.show()

    def show_iden_page(self):
        self.NoticeForm.close()
        self.iden_page.setupUi(self.IdenForm)
        self.iden_page.start_timer()
        self.iden_page.switch_window_to_exam.connect(self.show_exam_page)
        self.IdenForm.show()

    def show_exam_page(self):
        self.iden_page.stop_timer()
        self.exam_page.start_timer()
        self.IdenForm.close()
        self.exam_page.setupUi(self.ExamForm)
        self.exam_page.switch_window_to_result.connect(self.show_result_page)
        self.ExamForm.show()

    def show_result_page(self):
        self.exam_page.stop_timer()
        self.ExamForm.close()
        self.result_page.setupUi(self.ResultForm)
        self.result_page.switch_window_to_main.connect(self.show_main_page)
        self.ResultForm.show()