# Restaurant Code Challenge

This project implements a simple Yelp-style domain with three models: `Customer`, `Restaurant`, and `Review`. The goal is to manage relationships between customers, restaurants, and their reviews.

## Project Structure

- `customer.py`: Contains the implementation of the `Customer` class.
- `restaurant.py`: Contains the implementation of the `Restaurant` class.
- `review.py`: Contains the implementation of the `Review` class.
- `user_input.py`: A sample script that prompts the user to input their information and a restaurant review.


### Prerequisites

- Python 3.x

## Classes and Methods

### Customer
__init__(self, given_name, family_name): Initializes a customer with given and family names.
get_given_name(self): Returns the customer's given name.
get_family_name(self): Returns the customer's family name.
full_name(self): Returns the full name of the customer.
all(cls): Returns a list of all customer instances.
num_reviews(self): Returns the total number of reviews authored by the customer.
find_by_name(cls, name): Returns the first customer whose full name matches the given name.
find_all_by_given_name(cls, given_name): Returns a list of all customers with the given name.

### Restaurant
__init__(self, name): Initializes a restaurant with a name.
get_name(self): Returns the restaurant's name.
reviews(self): Returns a list of all reviews for the restaurant.
customers(self): Returns a unique list of all customers who have reviewed the restaurant.
average_star_rating(self): Returns the average star rating for the restaurant based on its reviews.
add_review(self, customer, rating): Adds a new review to the restaurant.
all(cls): Returns a list of all restaurant instances.

### Review
__init__(self, customer, restaurant, rating): Initializes a review with a customer, restaurant, and rating.
get_rating(self): Returns the rating for the restaurant.
all(cls): Returns a list of all reviews.
customer(self): Returns the customer object for the review.
restaurant(self): Returns the restaurant object for the review.

