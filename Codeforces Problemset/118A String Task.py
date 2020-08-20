class StringTask:
    def solve(self, str):

        return "".join("." + char.lower() for char in str if char.lower() not in "aeiouy")


if __name__ == "__main__":
    str = input()
    st = StringTask()
    print (st.solve(str))