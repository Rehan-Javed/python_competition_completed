
string = input("Input the word:  ")

#convert string to a set in the list
set = list(set(string))

#sorting the set of alphabets
set.sort()

# counting the occurances of alphabets
item_count = []
for i in range(0, len(set)):
	current_item_count = string.count(set[i])
	item_count.append(current_item_count)

print("The alphabets are " + str(set))
print("the count of them is " + str(item_count))

evens = []
odds = []

# putting even and odd counts of alphabets in separate lists
for i in range(0,len(item_count)):
    if item_count[i]%2 == 0:
        evens.append(item_count[i])
    else:
        odds.append(item_count[i])

print("Number of odd values are")
print(odds)

print("Number of even values are")
print(evens)

# to be palindrome, all alphabets should occur even number of times
# or odd number of times plus 1 odd number of time
if len(odds) == 0 or len(odds) == 1:
    print("It is a palindrome")
else:
    print("it is not a palindrome")
