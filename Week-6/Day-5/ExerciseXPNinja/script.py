

# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.
#
# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
#
# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

str1 = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
str_arr = str1.split(', ')
print(len(str_arr))
str_arr.sort()
print(str_arr)
str_arr.sort(reverse=True)
print(str_arr)

arr2 = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
arr_set = set(arr2)

print(','.join(arr_set))
print(len(arr_set))

str_arr.sort()
for word in str_arr:
    print(word[::-1], end=', ')