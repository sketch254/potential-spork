def anagram(str_one, str_two):
    if len(str_one) > len(str_two): return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(str_one)):
        s1Count[ord(str_one[i]) - ord("a")] += 1
        s2Count[ord(str_two[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    left = 0
    for right in range(len(str_one), len(str_two)):
        if matches == 26: return True

        index = ord(str_two[right]) - ord("a")
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1

        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(str_two[left]) - ord("a")
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1

        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1

        left += 1
    return matches == 26

print(anagram("program", "leetcodehelpsmelikeprogramming"))
