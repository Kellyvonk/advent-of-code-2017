input = open ('input', 'r').read()

list_input = list(input)

print ("-----------------PART 1-----------------")

sum = 0

for i in range(len(list_input)):
    if list_input[i] == list_input[(i+1)%len(list_input)]:
        sum += int(list_input[i])
print ("The sum is: ", sum)

print ("-----------------PART 2-----------------")

summ = 0
half = len(list_input)//2

for i in range(len(list_input)):
    if list_input[i] == list_input[(i+half)%len(list_input)]:
        summ += int(list_input[i])

print ("The summ is: ", summ)

