
#Question1
def multiply_bitwise(multiplicand,multiplier):
    # convert the multiplier into binary number
    multiplier_binary =  bin(multiplier)
    # make an empty list called binary
    binary = []

    # put the binary numbers into list
    for j in range(2,len(multiplier_binary)):
        binary.append(multiplier_binary[j])

    #reversing the list becasue binary start multiplying from right, but looping starts from left
    binary.reverse()

    answer = 0
    final = 0

    # finding the 1s in the binary list and shifting the multiplicand according to its position in binary
    # which is the same as the count of i
    for i in range(0,len(binary)):
        if binary[i] == '1':
            answer = multiplicand<<i
            final += answer

    print("The product of " + str(multiplicand) + " and " + str(multiplier) + " is " + str(final))



multiply_bitwise(10,14)



