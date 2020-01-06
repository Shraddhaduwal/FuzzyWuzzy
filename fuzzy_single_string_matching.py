from fuzzywuzzy import process

districts_with_correct_names = open('CSV_files/new.csv', 'r').read().split("\n")
print(districts_with_correct_names)
value = input("Enter the name of the district ")
output = process.extract(value, districts_with_correct_names)

print("Did you mean ", output[0])
for i in output[1:6]:
    ch = input("Type y/n ")
    if ch == 'y':
        break
    elif ch == 'n':
        print("Did you mean ", i)
    else:
        print("No matches found")
