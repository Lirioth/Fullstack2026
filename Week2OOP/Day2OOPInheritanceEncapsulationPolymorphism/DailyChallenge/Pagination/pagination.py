import math

class Pagination:
    # items: list of stuff to show, page_size: how many per page
    def __init__(self, items=None, page_size=10):
        self.items = [] if items is None else list(items)
        self.page_size = int(page_size)
        if self.page_size < 1:
            raise ValueError("page_size must be >= 1")
        self.current_idx = 0  # page index starts at 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # return items for the current page
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # go to a specific page (user uses 1..N)
    def go_to_page(self, page_num):
        page = int(page_num)
        if page < 1 or page > self.total_pages:
            raise ValueError("Invalid page number")
        self.current_idx = page - 1

    # go to first page (return self for chaining)
    def first_page(self):
        self.current_idx = 0
        return self

    # go to last page (return self for chaining)
    def last_page(self):
        self.current_idx = self.total_pages - 1 if self.total_pages > 0 else 0
        return self

    # go to next page if possible (return self)
    def next_page(self):
        if self.current_idx < max(self.total_pages - 1, 0):
            self.current_idx += 1
        return self

    # go to previous page if possible (return self)
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # print items of current page, one per line
    def __str__(self):
        return "\n".join(str(x) for x in self.get_visible_items())


# quick tests from the prompt
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.get_visible_items())          # ['a', 'b', 'c', 'd']
    p.next_page()
    print(p.get_visible_items())          # ['e', 'f', 'g', 'h']
    p.last_page()
    print(p.get_visible_items())          # ['y', 'z']

    try:
        p.go_to_page(10)                  # should raise ValueError
        print(p.current_idx + 1)
    except ValueError:
        print("ValueError")

    try:
        p.go_to_page(0)                   # should raise ValueError
    except ValueError:
        print("ValueError")
