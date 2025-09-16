from category_persistence import save_categories, load_categories

class CategoryManager: 
    def __init__(self, filename = "categories.json"):
        self.filename = filename
        self.categories = load_categories(self.filename)

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)
            self.save_categories()

    def remove_category(self, category):
        if category in self.categories:
            self.categories.remove(category)
            self.save_categories()

    def get_categories(self):
        return self.categories

    def save_categories(self):
        save_categories(self.filename, self.categories)