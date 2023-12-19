from customer import Customer
from restaurant import Restaurant
from review import Review

given_name = input("Enter your given name: ")
family_name = input("Enter your family name: ")

customer = Customer(given_name, family_name)

restaurant_name = input("Enter the name of the restaurant you went to: ")

restaurant = next((r for r in Restaurant.all_restaurants if r.get_name() == restaurant_name), None)
if not restaurant:
    restaurant = Restaurant(restaurant_name)

rating = int(input("Enter your rating for the restaurant (an integer between 1 and 5): "))
while rating < 1 or rating > 5:
    print("Invalid rating. Please enter a number between 1 and 5.")
    rating = int(input("Enter your rating for the restaurant (an integer between 1 and 5): "))

review = Review(customer.full_name(), restaurant.get_name(), rating)

customer.reviews.append(review)
restaurant.reviews.append(review)

print(f"Thank you, {customer.full_name()}, for your review of {restaurant.get_name()}!")

print(f"Number of reviews by {customer.full_name()}: {customer.num_reviews()}")
print(f"Average star rating for {restaurant.get_name()}: {restaurant.average_star_rating()}")
