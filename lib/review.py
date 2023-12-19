class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating

    def get_rating(self):
        return self._rating

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

if __name__ == "__main__":
    sample_review = Review("Guyo Halake", "Java", 4.5)

    print(f"Rating: {sample_review.get_rating()}")
    print(f"Customer: {sample_review.get_customer()}")
    print(f"Restaurant: {sample_review.get_restaurant()}")
