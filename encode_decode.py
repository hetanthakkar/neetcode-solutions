def remove_first_occurrence(main_string, sub_string):
    index = main_string.find(sub_string)
    if index != -1:
        return main_string[:index] + main_string[index + len(sub_string) :]
    return main_string


class Codec:
    def __init__(self) -> None:
        self.password = ""

    def encode(self, strs) -> str:
        key = set()

        for i in strs:
            key.update(i)
        a = ""
        for t in key:
            a += t
        sort = "".join(sorted(a))

        ret_string = ""
        for i in strs:
            i += sort
            ret_string += i
        return ret_string

    def decode(self, s: str):

        key = set()
        for i in s:

            key.update(i)
        a = ""
        for t in key:
            a += t
        sort = "".join(sorted(a))

        t = remove_first_occurrence(s, sort)
        if sort == t:
            return [sort]
        else:
            temp = s.split(sort)
        temp.pop()
        print(temp)

        return temp


codec = Codec()
strs = ["ab", "abab"]
encoded = codec.encode(strs)
print("Encoded:", encoded)
decoded = codec.decode(encoded)
print("Decoded:", decoded)
