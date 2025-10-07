def generate_subsequences(s):
    # Base case: empty string has one subsequence — the empty one
    if not s:
        return [""]

    # Split the string into first character and rest
    first = s[0]
    rest = s[1:]

    # Recursively get subsequences of the rest of the string
    subsequences_without_first = generate_subsequences(rest)

    # Add the first character to each of those subsequences
    subsequences_with_first = [first + sub for sub in subsequences_without_first]

    # Combine both sets: with and without the first character
    all_subsequences = subsequences_without_first + subsequences_with_first

    return sorted(all_subsequences, key=lambda x: (len(x)))


# Example:
result = list(filter(lambda x: len(x) == 3, generate_subsequences("abcdef")))
result.sort()
print(result)