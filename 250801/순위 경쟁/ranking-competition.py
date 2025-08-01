n = int(input())
logs = []
for _ in range(n):
    p,s = input().split()
    s = int(s)
    logs.append((p,s))

prev_honors = 'ABC'
scores = [0] * 3
count = 0

def return_honors():
    max_score = max(scores)
    honors = ""
    for i,score in enumerate(scores):
        if score == max_score:
            honors += chr(i + ord('A'))
    return honors

for p,s in logs:
    p = ord(p) - ord('A')
    scores[p] += s
    honors = return_honors()
    if prev_honors != honors:
        count += 1
        prev_honors = honors

print(count)

