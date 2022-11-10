print("enter the leapyear b/w two given years")
print("enter first year")
start=int(input())
print("Eenter end year ")
end=int(input())
for year in range (start,end+1):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print(year)
