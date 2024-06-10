from collections import Counter

if __name__ == '__main__':
    ransomNote="aa"
    magazine="aab"

    a = Counter()
    b = Counter()
    for val in ransomNote:
        a[val]+=1

    print(a.get("a"))

    # if (len(ransomNote) != len(magazine)):
    #     print("False")
    #
    # for i in ransomNote:
    #     if i in a.keys():
    #         a[i] += 1
    #     else:
    #         a[i] = 1
    #
    # for j in magazine:
    #     if j in b.keys():
    #         b[j] += 1
    #     else:
    #         b[j] = 1
    #
    # if a.items() == b.items():
    #     print("True")
