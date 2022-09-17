from src.user.storage import Storage


class User:
    def __init__(self, user_id):
        self.id = user_id
        self.storage = Storage()
        self.current_path = "/"
        self.current_page = None

    def set_page(self, page):
        self.current_page = page
        self.current_path = page.path
