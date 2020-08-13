import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    s = wrapper.fill(text=string)
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)