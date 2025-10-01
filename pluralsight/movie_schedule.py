current_movies = {
    'The Grinch': '11:00 AM',
    'Rodolph': '1:00 PM',
    'Frosty the Snoman': '3:00 PM',
    'Elf': '5:00 PM',
    'Home Alone': '7:00 PM',
    'The Polar Express': '9:00 PM'
}

print("We are showing the below movies:")
for key in current_movies:
    print(key)


movie = input("What movie would you like to see? \n")
showtime = current_movies.get(movie)

if showtime == None:
    print("Sorry, we are not showing that movie.")
else:
    print(f"{movie} is showing at {showtime}.")