# Problem Statement

# At the annual meeting of Board of Directors of Acme Inc, every one starts shaking hands with everyone else in the room. Given the fact that any two persons shake hand exactly once, Can you tell the total count of handshakes?

# Input Format
# The first line contains the number of test cases T, T lines follow.
# Each line then contains an integer N, the total number of Board of Directors of Acme.

# Output Format

# Print the number of handshakes for each test-case in a new line.

# Constraints

# 1 <= T <= 1000
# 0 < N < 106

# Enter your code here. Read input from STDIN. Print output to STDOUT
def shakes(a):
    ans = 0
    for i in range(1,a):
        ans += i
        i+=1
    return ans
n = int(raw_input())
for i in range(n):
    a = int(raw_input())
    ans = shakes(a)
    print ans