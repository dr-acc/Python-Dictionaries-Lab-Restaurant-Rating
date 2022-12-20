"""Restaurant rating lister."""

def add_rating(file):
    opened_file = open(file)
    ratings_library = {}

    for line in opened_file:
        restaurant_and_rating = line.rstrip().split(":")
        ratings_library[restaurant_and_rating[0]] = int(restaurant_and_rating[1])

        #now what do we need to do with each line?
        #iterate over and pull out the names & ratings
        #for word in restaurant_and_rating:
            # [first section = restaurant name = key]
            # [second section is just a number(the rating) = value]
    
        # restaurant = restaurant_and_rating[0]
        # rating = restaurant_and_rating[1]
        # ratings_library[rating] = #automatic 
    
    # # unpack and sort each line with .items() and sorted
    for restaurant, rating in sorted(ratings_library.items()):
        print(f'{restaurant} is rated at {rating}.')

add_rating("scores.txt")

# put your code here
# adding (brainstorm) animals["pony"]=2
#ratings_library["rating"]=value
# ratings_library.items()


# words_dict[word] = words_dict.get(word, 0) + 1