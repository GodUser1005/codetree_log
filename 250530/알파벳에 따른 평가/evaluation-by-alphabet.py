grade = input()
ans = ""
if grade == "S":
    ans = "Superior"
elif grade == "A":
    ans = "Excellent"
elif grade == "B":
    ans = "Good"
elif grade == "C":
    ans = "Usually"
elif grade == "D":
    ans = "Effort"
else:
    ans = "Failure"
print(ans)