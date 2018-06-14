
if __name__ == '__main__':
    buff = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        buff.append([score, name])
    min_item = min(buff)
    buff = [item for item in sorted(buff) if item[0]!=min_item[0]]
    min_item = min(buff)
    buff = [item for item in buff if item[0]==min_item[0]]
    for item in buff:
        print(item[1])