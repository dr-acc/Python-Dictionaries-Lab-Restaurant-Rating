"""Restaurant rating lister."""

def add_rating(file):
    opened_file = open(file)
    ratings_library = {}

    for line in opened_file:
        restaurant_and_rating = line.split(":")
        
    
        print(restaurant = restaurant_and_rating[0])
        print(rating = restaurant_and_rating[1])
        # ratings_library[rating] = #automatic 
    
    # # unpack each line with .items()
    # for restaurant, rating in ratings_library.items():
    #     print(restaurant, rating)

add_rating("scores.txt")

# put your code here
# adding (brainstorm) animals["pony"]=2
#ratings_library["rating"]=value
ratings_library.items()
