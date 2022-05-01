z
# Variable assignment


name = "Hello Master Bennett"
print(name)

a = b = c = d = "Godly"

print(a)
print(b)
print(c)
print(d)

#===================

txt = " Hello World "
print(txt)
x = txt.strip()
print(x)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020
print(car)
car['color']="Red"
print(car.get('model'))
print(car)

i = 1
for i in range(10):
  while i < 6:
    if i == 3:
      i += 1
  print(zip(i))
 
e = 2
while e < 6:
   print(i)
   e += 1
else:
   print("e is no longer less than 6")
print(e)

ruits = ["apple", "banana", "cherry"]
for o in ruits:
  if o == "banana":
   continue
print(o)

def my_function():
  print("Hello from a function")
my_function()

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
