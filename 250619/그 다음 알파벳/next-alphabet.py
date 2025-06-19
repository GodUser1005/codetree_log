alpha = input()
idx = ord(alpha) - ord('a')
next_idx = (idx + 1) % 26

print(chr(ord('a') + next_idx))