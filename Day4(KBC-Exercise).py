que = [
    "Who is the GOAT of football?", "messi or ronaldo?",
    "why ronaldo is better than messi?",
    "how many champions league ronaldo won?",
    "who is the top scorer of football?"
]

ans = ["a", "b", "a", "a", "b"]

options = [
    "a. ronaldo   b. messsi", "a. messi   b. ronaldo",
    "a. because he is better   b. he is not ", "a. 5   b. 7",
    "a. messi   b. ronaldo"
]

win = [10000, 100000, 1000000, 10000000, 20000000]

for i in que:
  print(i)
  print(options[que.index(i)])
  a = input()
  if a == ans[que.index(i)]:
    print("\n~~~ CORRECT ANSWER ~~~")
    print("    you won rs.", win[que.index(i)], "\n")
  else:
    print("\n!!! INCORRECT ANSWER !!!\n")
    if que.index(i) != 0:
      print("You won rs.", win[que.index(i) - 1], "\n")
    else:
      print("You won nothing\n")
    break
