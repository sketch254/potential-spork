def reverse(s):

    def reverse_str(l, r):

        if(l < r):
            reverse_str(l + 1, r - 1)
            s[l], s[r] = s[r], s[l]

    reverse_str(0, len(s) - 1)