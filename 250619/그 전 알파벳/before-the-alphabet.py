alpha = input()
idx = ord(alpha) - ord('a')
prev = (idx + 25) % 26

print(chr(ord('a') + prev))