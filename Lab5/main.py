from boyes_moore_substring import BoyesMooreSubstring

def main():
    txt = BoyesMooreSubstring("when it's all over")
    print(txt.search("l"))
    print(txt.search("when"))
    print(txt.search("over"))



if __name__ == '__main__':
    main()