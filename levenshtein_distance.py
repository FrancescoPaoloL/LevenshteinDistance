def levenshtein_distance(s: str, t: str) -> int:   
    # get the length of each string...
    n, m = len(s), len(t)

    # and create a matrix to hold the minimum distances
    # between each prefix of the two strings
    d = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
        
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Calculate minimum distance between 
            # string prefixes by comparing character positions.
            
            # If the characters at position i and j match, 
            # we can assume that no edit operation is required for these characters. 
            # Therefore, we take the value from the previous diagonal entry, 
            # which represents the minimum number of operations required 
            # to transform the prefixes up to positions i-1 and j-1.
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                # If the characters at position i and j don't match, 
                # we need to consider three possible edit operations: insertion, 
                # deletion, or substitution. 
                # To find the minimum number of operations required to transform 
                # the prefixes up to positions i and j, we take the minimum value 
                # from one of these entries:
                #  - the left entry, because represents the number of operations 
                #    required to transform the prefix up to position i-1 into 
                #    the prefix up to position j;
                #  - the above entry, because represents the number [...] 
                #    to transform the prefix up to position i into the prefix up 
                #    to position j-1. 
                #  - The above-left entry represents the number [...] 
                #    to position i-1 into the prefix up to position j-1
                # and add 1.
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1

    # return the final value in the matrix, which is the
    # Levenshtein Distance between the two input strings
    return d[-1][-1]


if __name__ == '__main__':
    s1 = "The quick brown fox jumps over the lazy dog."
    s2 = "Pack my box with five dozen liquor jugs."
    distance = levenshtein_distance(s1, s2)
    print(f"The Levenshtein distance between '{s1}' and '{s2}' is {distance}")
