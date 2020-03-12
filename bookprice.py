book_cost=24.95
discount=float(40)/float(100)
shipping=3
additional=0.75
shipfor60=shipping+(59*0.75)
copy = (book_cost-(book_cost*discount))
copy60=60*copy+shipfor60
print(copy60)
