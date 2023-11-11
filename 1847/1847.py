A, B, C = map(int, input().split())

if A > B and B <= C:
    print(":)")
elif A < B and B >= C:
    print(":(")
elif A < B and B < C and (B - A) > (C - B):
    print(":(")
elif A < B and B < C and (B - A) <= (C - B):
    print(":)")
elif A > B and B > C and (A - B) > (B - C):
    print(":)")
elif A > B and B > C and (A - B) <= (B - C):
    print(":(")
elif A == B and B < C:
    print(":)")
else:
    print(":(")