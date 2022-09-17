class Router:
    def add(self, path, page):
        self.path_to_page[path] = page

    def get_page(self, path):
        return self.path_to_page[path]


router = Router()
