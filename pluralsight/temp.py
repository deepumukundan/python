look_up = input('What acronym would you like to lookup?: ')

found = False
with open('acronyms.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if not found:
    print('Acronym not found!')