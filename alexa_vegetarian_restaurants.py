'''
Alexa Vegetarian Restaurants

Amazon's Alexa team is working on optimizing the customer experience for scenarios where
customers ask generic questions. One example of a generic question is "What are good
vegetarian restaurants nearby?". In this scenario, Alexa would then search for a list of
vegetarian restaurants in the city and select the nearest X vegetarian restaurants relative
to the customer's location.

Algorithm that, given an array representing the locations of N vegetarian restaurants
in the city, finds the nearest X vegetarian restaurants to the customer's location.

Input:
The input to the function consists of two arguments:
`allLocations`, a list of elements where each element consists of a pair of integers representing
the x and y coordinates of the vegetarian restaurant locations, to a total max of N possible
vegetarian restaurants in the customer's city;
`numRestaurants`, an integer representing the number of nearby vegetarian restaurants that
would be returned to the customer (X).

Output:
Return a list of elements, where each element of the list represents the x and y coordinates
of the nearest recommended vegetarian restaurant.

Constraints:
numRestaurants <= totalRestaurants

Note:
The customer begins at the location [0, 0].
The distance from the customer's current location to a recommended vegetarian restaurant
location (x, y) is the square root of $x^2 + y^2$.
If there are ties, then return any of the locations as long as you satisfy returning X
nearby vegetarian restaurants.
'''

from math import sqrt

def nearest_vegetarian_restaurant(all_locations: list, num_restaurants: int) -> list:
    if num_restaurants <= 0:
        return []
    
    # Calculate the distance to every restaurant in the city
    distances = zip(all_locations, [ distance_to_location(loc) for loc in all_locations ])

    # Sort distances ascendantly
    distances = sorted(distances, key = lambda d: d[1])

    # Return the nearest N vegetarian restaurants
    return list(next(zip(*distances[: num_restaurants])))

# Calculate the euclidean distance between two pairs of coordinates
def distance_to_location(destination: list, origin: list = [0,0]) -> float:
    return sqrt((destination[0] - origin[0]) ** 2 + (destination[1] - origin[1]) ** 2)

def validate_test_case(test_input: list, result: list, solution: list):
    print('Input:', test_input)
    print('Result:', result)
    print('Result {}matches solution: {}\n'\
        .format('' if result == solution else 'NOT ', solution))




# Test cases evaluation

test_cases = [ ([[1, 2], [3, 4], [1, -1]], 2),
                ([[1, -3], [1, 2], [3, 4]], 1),
                ([[3, 6], [2, 4], [5, 3], [2, 7], [1, 8], [7, 9]], 3) ]
expected_results = [ [[1, -1], [1, 2]],
                    [[1, 2]],
                    [[2, 4], [5, 3], [3, 6]] ]

for case, solution in zip(test_cases, expected_results):
    my_result = nearest_vegetarian_restaurant(case[0], case[1])
    validate_test_case(case, my_result, solution)
