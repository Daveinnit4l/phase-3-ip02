from review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def add_review(self, review):
        self.reviews.append(review)

    def average_star_rating(self):
        total_rating = sum(review.get_rating() for review in self.reviews)
        num_reviews = len(self.reviews)
        return total_rating / num_reviews if num_reviews > 0 else 0

if __name__ == "__main__":
    sample_restaurant = Restaurant("Java")

    sample_review = Review("Guyo Halake", "Java", 4)

    sample_restaurant.add_review(sample_review)

    print(f"Restaurant Name: {sample_restaurant.get_name()}")
    print(f"Reviews: {sample_restaurant.get_reviews()}")
    print(f"Average Star Rating: {sample_restaurant.average_star_rating()}")
