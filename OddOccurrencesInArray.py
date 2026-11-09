def solution(A):
    # Sorting puts equal numbers next to each other,
    # so pairs can be checked side by side
    A.sort()
    N = len(A)

    i = 0
    while i < N:
        # If we reach the last element, it never got a partner, so it's the answer
        if i == N - 1:
            return A[i]

        # If two neighbours don't match, A[i] is the one without a partner
        if A[i] != A[i + 1]:
            return A[i]

        # The pair matched, so skip both and check the next pair
        i = i + 2