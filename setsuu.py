set1 = {"east", "west"}
set2 = {"north", "south"}

set1.update(set2)

print(set1)
result=set1.union(set2)
print(result)
print(set1|set2)

result = set1.copy()
print(result)
