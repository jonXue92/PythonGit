s = "Hello"
s1 = s
s2 = "He"
s3 = "llo"
s4 = s2+s3

print(s)   # "Hello"
print(s1)  # "Hello"
print(s2)  # "He"
print(s3)  # "llo"
print(s4)  #  "Hello"

print(s == s1)  # True
print(s == s2)  # False
print(s == s3)  # False
print(s == s4)  # True

s = "Hello"
for i in range(len(s)):
    print(s[i])
#另一种写法
for c in s:
    print(c)