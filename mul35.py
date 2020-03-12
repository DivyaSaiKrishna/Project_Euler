multiple3 = [i for i in range(1, 1000) if i % 3 == 0]
multiple5 = [i for i in range(1, 1000) if i % 5 == 0]
multiple15 = [i for i in range(1, 1000) if i % 15 == 0]
mul3=sum(multiple3)
mul5=sum(multiple5)
mul15=sum(multiple15)
a=mul3+mul5-mul15
print(mul3)
print(mul5)
print(a)
