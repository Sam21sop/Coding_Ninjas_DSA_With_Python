import sys

# Function to compute character frequency counts for a string
def compute_char_counts(s):
    char_counts = [0] * 26
    char_counts[ord('a') - ord('a')] = s.count('a')
    char_counts[ord('b') - ord('a')] = s.count('b')
    return char_counts


# Function to check if it is possible to rearrange Q to form P
def is_possible_to_rearrange(P, Q):
    if len(P) != len(Q):
        return False
    char_counts = [0] * 26
    for p, q in zip(P, Q):
        char_counts[ord(p) - ord('a')] += 1
        char_counts[ord(q) - ord('a')] -= 1
    return all(count == 0 for count in char_counts)


def main():
    M = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())
    for _ in range(K):
        W, X, Y, Z = map(int, sys.stdin.readline().split())
        P = M[W-1:X]
        Q = M[Y-1:Z]
        if is_possible_to_rearrange(P, Q):
            sys.stdout.write("true\n")
        else:
            sys.stdout.write("false\n")


if __name__ == "__main__":
    main()