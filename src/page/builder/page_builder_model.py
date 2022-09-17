class PageBuilderModel:
    def __init__(self):
        self.buttons = None
        self.markup = None
        self.inline = None

    def add_button(self, button):
        self.buttons.append(button)

    def set_inline(self, inline):
        self.inline = inline

    def make_markup(self):
        # keyboard = Markup()
        pass
