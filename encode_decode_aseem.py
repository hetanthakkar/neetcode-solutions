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
        # print(sort)
        ret_string = ""
        for i in strs:
            i += sort
            ret_string += i
        print(ret_string, "hey")
        return ret_string

    def decode(self, s: str):
        # print(s)
        key = set()
        for i in s:
            # print(i)
            key.update(i)
        a = ""
        for t in key:
            a += t
        sort = "".join(sorted(a))
        if s == "":
            return [""]
        if s != "":
            temp = s.split(sort)
            temp.pop()
            print(temp)
        else:
            return ""
        return temp


codec = Codec()
strs = ["a", "a"]
encoded = codec.encode(strs)
print("Encoded:", encoded)
decoded = codec.decode(encoded)
print("Decoded:", decoded)
