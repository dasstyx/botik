import logging
import os


class Navigation:
    def __init__(self):
        self.page_factory = None
        self.path_to_page_data = {}

    def init_page_factory(self, page_factory):
        self.page_factory = page_factory

    def add_page_data(self, data):
        self.path_to_page_data[data.path] = data

    def get_page_data(self, path):
        return self.path_to_page_data.get(path)

    def get_user_page(self, user):
        return user.current_page

    @staticmethod
    def concat_paths(source, destination):
        """
        Concatenate two paths.
        :param source: Source absolute path
        :param destination: Destination relative path
        :return: concatenated path
        """
        destination = destination.lstrip('/')
        if destination.startswith('~'):
            return destination[1:]

        # TODO: make a better OS-independent path handling
        combined_path = os.path.normpath((os.path.join(source, destination)))
        combined_path = str(combined_path).replace('\\', '/')
        return combined_path

    async def change_page(self, user, path):
        """
        Change page for user.
        :param user: User
        :param path: Absolute (starts with a '~') or relative path to page
        """
        current_page = self.get_user_page(user)
        current_path = current_page.path if current_page else '/'
        concat_path = Navigation.concat_paths(current_path, path)

        page = await self._render_page(user, concat_path)
        if page:
            user.set_page(page)
            if current_page:
                current_page.destruct()
            logging.debug(f"User {user.id} has changed page\n\tfrom {current_path}\n\tto {concat_path}")

    async def get_back(self, user):
        """
        Gets the path from the active page's 'get_back_path' method and navigates to the page at that path.
        :param user: User
        :param path: Absolute (starts with a '~') or relative path to page
        """
        page = self.get_user_page(user)
        back_path = page.get_back_path()
        await self.change_page(user, back_path)

    def _make_page(self, page_data):
        return self.page_factory.create(page_data)

    async def _render_page(self, user, path):
        data = self.get_page_data(path)
        if not data:
            return None

        page = self._make_page(data)
        await page.make_page_content(user)
        return page
