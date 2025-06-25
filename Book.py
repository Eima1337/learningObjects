class Book():

    def __init__(self, title="", pages=0, release_year=0):
        self.title = title
        self.pages = pages
        self.release_year = release_year

    def __str__(self):
        return f"Title {self.title}, pages {self.pages}, release year {self.release_year}"
