

# Time complexity: O(n), only iterate through the list once, use list indexing which is O(n)
# Space Complexity: O(n) bc we made a list of size n + 1
def newman_conway(num):
    if num < 1:
        raise(ValueError)

    memo = [None] * (num + 1)
    if num >= 1:
        memo[1] = 1
    if num >= 2:
        memo[2] = 1

    for i in range(3, num + 1):
        memo[i] = memo[memo[i - 1]] + memo[i - memo[i - 1]]

    result = str(memo[1])
    for i in range(2, len(memo)):
        result += " " + str(memo[i])
    return result

