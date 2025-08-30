import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it charges 2 dollars per day")
elif type == "t3.medium":
    print("it charges you 4 dollars per day")
else:
    print("provide valid input")

