class User:
    def __init__(self, username):
        self.username = username
        self.reviews = []

    def __repr__(self):
        return f"User({self.username})"

class Business:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_average_rating(self):
        if not self.reviews:
            return 0
        return round(sum(r.rating for r in self.reviews) / len(self.reviews), 2)

    def __repr__(self):
        return f"{self.name} ({self.category}) - Avg. Rating: {self.get_average_rating()}"

class Review:
    def __init__(self, user, business, rating, comment=""):
        self.user = user
        self.business = business
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f"{self.user.username} rated {self.business.name} {self.rating}/5: {self.comment}"

class YelpSystem:
    def __init__(self):
        self.users = {}
        self.businesses = {}

    def add_user(self, username):
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username)

    def add_business(self, name, category):
        if name in self.businesses:
            raise ValueError("Business already exists.")
        self.businesses[name] = Business(name, category)

    def add_review(self, username, business_name, rating, comment=""):
        if username not in self.users:
            raise ValueError("User not found.")
        if business_name not in self.businesses:
            raise ValueError("Business not found.")

        user = self.users[username]
        business = self.businesses[business_name]
        review = Review(user, business, rating, comment)

        user.reviews.append(review)
        business.add_review(review)

    def show_business(self, business_name):
        if business_name not in self.businesses:
            raise ValueError("Business not found.")
        business = self.businesses[business_name]
        print(f"--- {business.name} ---")
        print(f"Category: {business.category}")
        print(f"Average Rating: {business.get_average_rating()}")
        print("Reviews:")
        for r in business.reviews:
            print(f" - {r}")

    def search_business(self, keyword):
        results = [b for b in self.businesses.values() if keyword.lower() in b.name.lower() or keyword.lower() in b.category.lower()]
        return results
