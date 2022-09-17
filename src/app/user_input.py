class UserInput:
    def __init__(self, navigator, users):
        self.users = users
        self.navigator = navigator

    def forward_inline_button(self, user, text):
        page = self.navigator.get_user_page(user)
        page.check_input(user, text)
        print("Forward button")

    def handle_input(self, user, text):
        # TODO: Do not render page on every user message!
        page = self.navigator.get_user_page(user)

        page.check_input(user, text)