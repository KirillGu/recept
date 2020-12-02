with open('file1.txt') as f:
    text = f.readlines()
    size = len(text)


with open('file2.txt') as fe:
    text1 = fe.readlines()
    size2 = len(text1)

store = [size, size2]

#print(max(store))

for items in store:
    if items == min(store):
        item = min(store)
        print(item)

if item == size:
    print(f'filee.txt', size, text[0], text[1], sep = '\n')
    print('***********')
    print('file2.txt', size2, text1[0], text1[1], sep = '\n')
elif item == size2:
    print('file2.txt', size2, text1[0], text1[1], sep = '\n')
    print('***********')
    print(f'filee.txt', size, text[0], text[1], sep = '\n')
