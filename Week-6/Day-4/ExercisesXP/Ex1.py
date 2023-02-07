my_fav_numbers = {6, 8, 16, 24}
my_fav_numbers.add(5)
my_fav_numbers.add(7)

my_fav_numbers.remove(7)

friend_fav_numbers = {3, 9, 10}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)