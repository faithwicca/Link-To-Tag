# this script changes all the [[tag]] to #tag in every .md file in a folder
from os import listdir
folder = input('folder?')
folderList = listdir(folder)  # makes a list of all files in a vault
# print(folderList)
tag = input('tag?')
hashtag = tag.replace(' ', '_')

for f in folderList:  # goes through all files in a vault
    dot = f.find('.')
    md = f.find('.md')
    if dot != 0 and md != -1:  # ensures that file is only a note (.md and no '.' in first place of name)
        file = open(folder + '/' + f, 'r')
        filest = file.read().splitlines()  # reading a note into a list line by line
        isThereTag = False  # in case there is no tag in this note
        for i in range(len(filest)):  # checks all the lines
            n = filest[i].find('[[' + tag)  # finds where link is in the file
            if n != -1:
                isThereTag = True
                endOfTag = filest[i].find(']]', n)

                # preparing text to insert instead of link. if link has display text, it will take it,
                # otherwise the link name(tag)
                instead = filest[i][n + 2:endOfTag]
                stick = instead.find('|')
                if stick != -1:
                    instead = instead[stick + 1:]

                # changing link to text
                filest[i] = filest[i][:n] + instead + filest[i][endOfTag + 2:]
        file.close()

        if isThereTag:
            file = open(folder + '/' + f, 'w')
            # writing the note back from the list, corrected
            for element in filest:
                print(element, file=file)
            print('#' + tag, file=file)  # adding a tag at the end of file
            print('tag "', hashtag, '" updated in file ', f[:-3], sep='')
            file.close()
        else:
            print('no such tag in file ' + f[:-3])
