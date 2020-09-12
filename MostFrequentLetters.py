#Program to print letters in a string in decreasing order of frequency
import collections

def most_frequent(str):
    freq = {}

    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    sorted_freq = sorted(freq.items(), key = lambda p : p[1], reverse = True)
    for j in sorted_freq:
        print(j[0],":", j[1])


str = input("Please enter a string: ")
print("Count of all letters given string is:\n")
most_frequent(str)
