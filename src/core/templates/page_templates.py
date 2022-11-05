from src.core.templates.button_templates import ButtonTemplates


class PageTemplates:
    def __init__(self, navigation):
        self.button = ButtonTemplates(navigation)
