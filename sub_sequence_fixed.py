def generate_fixed_length_subsequences(s, k):
    result = []

    def generate_sub(index, current):
        # Base case: found a valid subsequence
        if len(current) == k:
            result.append(current)
            return
        
        # Base case: end of string or not enough chars left
        if index == len(s):
            return

        # Optimization: stop if even adding all remaining chars can't reach length k
        if len(current) + (len(s) - index) < k:
            return

        # Include current character
        generate_sub(index + 1, current + s[index])

        # Exclude current character
        generate_sub(index + 1, current)

    generate_sub(0, "")
    return sorted(result)


print(generate_fixed_length_subsequences("abcdef", 3))