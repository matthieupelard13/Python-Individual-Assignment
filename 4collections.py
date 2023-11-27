#4collections.py

# 4.1 PYTHON Lists

fruits = ["kiwi", "pineapple", "apple"]

# 4.1.1 Print the second item in the fruits list.
# TODO: Write your code below
print(fruits[1]) 


# 4.1.2 Change the value from "kiwi" to "orange", in the fruits list.
# TODO: Write your code below
fruits[0] = "orange" 
print(fruits) 


# 4.1.3 Use the insert method to add "lemon" as the second item in the fruits list.
# TODO: Write your code below
fruits.insert(1, "lemon") 
print(fruits) 


# 4.1.4 Use the remove method to remove "pineapple" from the fruits list.
# TODO: Write your code below
fruits.remove("pineapple") 
print(fruits) 


# 4.1.5 Use negative indexing to print the last item in the list.
# TODO: Write your code below
print(fruits[-1]) 

# 4.1.6 Use a range of indexes to print the third, fourth, and fifth item in the list fruits2.

fruits2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# TODO: Write your code below
print(fruits2[2:5]) 


# 4.1.7 Use the correct syntax to print the number of items in the list fruits
# TODO: Write your code below
print(len(fruits)) 


# 4.1.8  Write a program that add the average of numbers in a list scores.
# you are not allowed to use the sum() or len() functions.

scores = [50, 55, 56, 70, 80, 60, 66]

# TODO: Write your code below

lenght=0
total=0
for X in scores:
   total+=X
   lenght+=1

   print(total)
   print(lenght)
   print(total/lenght) 

# 4.1.9 Write a program that calculates the highest number in a list scores
# you are not allowed to use the max or min functions.
scores = [50, 55, 56, 70, 80, 60, 66]
highest_score = scores[0] 
for score in scores: 
    if score > highest_score: 
        highest_score = score 
print("Highest score:", highest_score) 

# TODO: Write your code below


# 4.1.10






# 4.2. PYTHON Dictionaries

car =	{
  "brand": "Renault",
  "model": "Clio",
  "year": 2018
}

# 4.2.1 Use the get method to print the value of the "model" key of the car dictionary.
# TODO: Write your code below
print(car.get("model")) 


# 4.2.2 Change the "year" value from 2018 to 2020 in the car dictionary.
# TODO: Write your code below
car["year"] = 2020 
print(car) 


# 4.2.3 TODO: Add the key/value pair "color" : "blue" to the car dictionary.
# TODO: Write your code below
car["color"] = "blue" 
print(car) 


# 4.2.4 Use the pop method to remove "model" from the car dictionary.
# TODO: Write your code below
car.pop("model") 
print(car) 


# 4.2.5 Use the clear method to empty the car dictionary.
# TODO: Write your code below
car.clear() 
print(car) 
