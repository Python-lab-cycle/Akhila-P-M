#leap year
print("Print leap year between 2 given years")
print("enter start year")
syear=int(input())
print("enter last year")
lyear=int(input())
print("List of years")
for year in range(syear,lyear):
 if year%4==0:
   print(year)
