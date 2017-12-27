def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    def generate(p, left, right, parens=[]):
        if left > 0:     generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if right == 0:   parens += p,
        return parens

    return generate('', n, n)


result = generateParenthesis(4)
print (result)
