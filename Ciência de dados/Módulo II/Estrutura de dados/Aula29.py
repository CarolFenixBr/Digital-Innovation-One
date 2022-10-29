"""Sorted"""

linguagens = ["Python", "Js", "C", "Java","Csharp"]

print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))

print(sorted(linguagens))