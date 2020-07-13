from src.page.LoginPage import LoginPage
from src.page.MainPage import MainPage
from src.page.LogPage import LogPage
from src.page.PreViewPage import PreViewPage
from src.page.NoticePage import NoticePage
from src.page.ExamPage import ExamPage
from src.page.ResultPage import ResultPage

class Controller:
    def __init__(self):
        self.login_page = LoginPage()
        self.main_page = MainPage()
        self.log_page = LogPage()
        self.preview_page = PreViewPage()
        self.notice_page = NoticePage()
        self.exam_page = ExamPage()
        self.result_page = ResultPage()

    def show_login_page(self):
        self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.login_page.show()

    def show_main_page(self):
        self.login_page.close()
        self.result_page.close()
        self.main_page.switch_window_to_log.connect(self.show_log_page)
        self.main_page.switch_window_to_preview.connect(self.show_preview_page)
        self.main_page.show()

    def show_log_page(self):
        self.main_page.close()
        self.log_page.show()

    def show_preview_page(self):
        self.main_page.close()
        self.preview_page.switch_window_to_notice.connect(self.show_notice_page)
        self.preview_page.show()

    def show_notice_page(self):
        self.preview_page.close()
        self.notice_page.switch_window_to_exam.connect(self.show_exam_page)
        self.notice_page.show()

    def show_exam_page(self):
        self.notice_page.close()
        self.exam_page.switch_window_to_result.connect(self.show_result_page)
        self.exam_page.show()

    def show_result_page(self):
        self.exam_page.close()
        self.result_page.switch_window_to_main.connect(self.show_main_page)
        self.result_page.show()
