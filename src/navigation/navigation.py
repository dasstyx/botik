from src.page.page_data import PageData


class Navigation:
    def __init__(self):
        self.page_factory = None
        self.path_to_page_data = {}

    def init_page_factory(self, page_factory):
        self.page_factory = page_factory

    def add_page_data(self, data: PageData):
        self.path_to_page_data[data.path] = data

    def get_page_data(self, path):
        return self.path_to_page_data[path]

    def get_user_page(self, user):
        return user.current_page

    async def change_page(self, user, path):
        page = await self._render_page(user, path)
        user.set_page(page)

    async def get_back(self, user):
        page = self.get_user_page(user)
        back_path = page.get_back_path()
        await self.change_page(user, back_path)

    def _make_page(self, page_data):
        return self.page_factory.create(page_data)

    async def _render_page(self, user, path):
        data = self.get_page_data(path)
        page = self._make_page(data)
        await page.make_page_content(user)
        return page
