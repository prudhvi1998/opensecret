def main(input):
    output = "This sentence contains "
    given = input.split(' ')
    length = len(given)
    result = list()
    for i in range(0, 26):
        result.append(0)
    result[0] = 1
    result[2] = 2
    result[4] = 3
    result[7] = 1
    result[8] = 2
    result[13] = 4
    result[14] = 1
    result[18] = 3
    result[19] = 2
    print(given)
    print(result)
    for i in given:
        result[ord(i) - ord('a')] += 1
        # if (result[ord(i) - ord('a')] > 1):
        #     result[18] += 1
    print(result)
    if (length > 1):
        result[0] += 1
        result[13] += 1
        result[3] += 1
    print(result)
    x = ""
    if (length == 1):
        temp = result[ord(given[0]) - ord('a')]
        if (temp == 1):
            x = "one " + given[0]
        elif (temp == 2):
            x = "two " + given[0] + "'s"
        elif (temp == 3):
            x = "three " + given[0] + "'s"
        elif (temp == 4):
            x = "four " + given[0] + "'s"
        elif (temp == 5):
            x = "five " + given[0] + "'s"
        output = output + x
    else:
        for i in given:
            if(i!='a' and i!='s'):
                result[ord(i) - ord('a')] += 1
        print(result)
        for i in range(0, length):
            temp = result[ord(given[i]) - ord('a')]
            print(given[i])
            print(ord(given[i]) - ord('a'))
            print(result[ord(given[i]) - ord('a')])
            if (temp == 1):
                x = "one " + given[i]
            elif (temp == 2):
                x = "two " + given[i] + "'s"
            elif (temp == 3):
                x = "three " + given[i] + "'s"
            elif (temp == 4):
                x = "four " + given[i] + "'s"
            elif (temp == 5):
                x = "five " + given[i] + "'s"
            output = output + x
            if (i < length - 2):
                output = output + ", "
            elif (i == length - 2):
                output = output + " and "
    print(output)

if __name__ == '__main__':
    main("a r")