def strStr(haystack: str, needle: str) -> int:
    """
    在主串(haystack)中查找子串(needle)的第一个出现位置。

    使用KMP算法进行字符串查找，避免了不必要的回溯，提高了查找效率。

    :param haystack: 主串，即我们要在其中查找子串的字符串
    :param needle: 子串，即我们要在主串中查找的字符串
    :return: 子串在主串中第一次出现的索引；如果不存在，则返回-1
    """
    # 初始化子串和主串的长度
    n = len(needle)
    m = len(haystack)

    # 将子串和主串拼接，并在中间插入一个分隔符'#'，用于区分子串和主串
    # 这样做的目的是为了在后续计算部分匹配表时，能够直接处理主串部分
    s = needle + '#' + haystack

    # 初始化部分匹配表
    pi = [0] * len(s)

    # 遍历字符串s，计算部分匹配表pi
    for i in range(1, len(s)):
        # 初始化当前长度为上一个字符的最长前缀后缀长度
        length = pi[i - 1]

        # 当当前长度不为0且当前字符不等于长度位置的字符时，缩小长度
        # 这里是KMP算法的核心，通过部分匹配表避免回溯
        while length and s[i] != s[length]:
            length = pi[length - 1]

        # 如果当前字符等于长度位置的字符，说明找到了一个更长的前缀后缀
        if s[i] == s[length]:
            pi[i] = length + 1

            # 如果当前长度等于子串长度，说明找到了子串，返回其在主串中的位置
            if pi[i] == n:
                return i - n * 2

    # 如果遍历结束还没找到子串，返回-1表示未找到
    return -1



haystack = "AGCATAATAATTAA"
needle = "ATAATA"

print(strStr(haystack, needle))
