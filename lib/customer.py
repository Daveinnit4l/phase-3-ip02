from review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]

if __name__ == "__main__":
    sample_customer = Customer("Guyo", "Halake")

    sample_review = Review(sample_customer.full_name(), "Java", 4)

    sample_customer.reviews.append(sample_review)

    print(f"Given Name: {sample_customer.get_given_name()}")
    print(f"Family Name: {sample_customer.get_family_name()}")
    print(f"Full Name: {sample_customer.full_name()}")
    print(f"Number of Reviews: {sample_customer.num_reviews()}")
    print(f"Find Customer by Name: {Customer.find_by_name(sample_customer.full_name())}")
