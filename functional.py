square = lambda x: x ** 2
print(square(2))

power = lambda x, y: x ** y
print(power(2, 4))

numbers = [1,2,3,4,5,6]
squared = list(map(square, numbers))
print(f"Squared: {squared}")
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered: {filtered}")
summed = sum(numbers)
print(f"Summed: {summed}")

characters = ['abc', 'de', 'fghi']
lengths = list(map(len, characters))
print(f'Lengths of {characters} are {lengths}')

names = ["Deepu", "Lekshmi", "Malavika", "Avantika"]
names.reverse()
names.sort(key=lambda x: len(x))
print(names)