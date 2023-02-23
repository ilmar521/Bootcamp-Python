
class Pagination:
    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = int(page_size)
        self.current_page = 1
        pages = []
        i = 0
        for x in items:
            if i == 0:
                i += 1
                pages.append([x])
            else:
                if i == self.page_size - 1:
                    i = 0
                    pages[-1].append(x)
                else:
                    i += 1
                    pages[-1].append(x)
        self.total_pages = len(pages)
        self.pages = pages

    def prev_page(self):
        self.current_page -= 0 if self.current_page == 1 else 1
        return self

    def next_page(self):
        self.current_page += 0 if self.total_pages == self.current_page else 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page):
        self.current_page = int(page)
        if self.current_page < 1:
            self.current_page = 1
        elif self.current_page > self.total_pages:
            self.current_page = self.total_pages

        return self

    def get_visible_items(self):
        return self.pages[self.current_page - 1]


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.next_page().next_page().next_page().next_page().next_page().next_page().next_page()
print(p.get_visible_items())
p.prev_page().prev_page().prev_page().prev_page()
print(p.get_visible_items())
p.last_page()
print(p.get_visible_items())
p.first_page()
print(p.get_visible_items())
p.go_to_page(3)
print(p.get_visible_items())
p.go_to_page(-1)
print(p.get_visible_items())
p.go_to_page(8)
print(p.get_visible_items())
