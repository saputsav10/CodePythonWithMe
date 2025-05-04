# a="Helllo World"
# print(a.split("l"))

# a=15
# txt=f"My name is John {a}"
# print(txt, a)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = "We are the so-called \\\Vikings\\ from the north."
# print(txt)

# txt="Hello, this time I am practicing Python from my very heart and it will be awesome."
# print(txt.partition("4"))
# print(txt.translate("2"))

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# print(bool("Hello"))
# print(bool(15))

# def myFunction() :
#   return False

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

# x = 200
# print(isinstance(x, int))

# x="Hello"
# print(isinstance(x,int))

# print(-5+10*3)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# x=(thislist[2:5])
# print(x)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = [x for x in range(10) if x < 5]
# newlist=[x.upper() for x in fruits if "a" in x]
# newlist=["hello" for x in fruits]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)
# printnewlist=[a for a in fruits]

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

