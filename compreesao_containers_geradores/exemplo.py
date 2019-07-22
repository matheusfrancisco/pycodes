def dist_chars(text: str, n: int) -> list:
    return [text[i: i+n] for i in range(0, len(text), n)]


with open('exemplo.txt') as _file:
    result = dist_chars(_file.read(), 76)



assert len(result[0]) == 76
