def reverse(string):
    numbs = string.split()
    for i in range(1, len(numbs)+1):
        print(numbs[-i], end=" ")
words = input()
reverse(words)