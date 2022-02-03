#code for finding the largest number from the same digits using the same numbers.

s = input("enter number")
for br in range(len(s)-2,-1,-1):
    if s[br]<s[br+1]:
        break
else:
    raise ValueError("number is already in its largest form.")
x = sorted(s[br:]).index(s[br])
for val in sorted(s[br:])[x+1:]:
    if s[br]!=val:
        break
l = list(s[br:])
l.remove(val)
new = s[:br]+val+"".join(sorted(l))
print(new)
