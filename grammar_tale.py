s = """2 A Tiny Butterfly
4 A Fairy Tale for Night
5 New Mary’s Friend
5 Dandy The Alligator
4 A Magic Feather
5 A Wolf
4 Treasure
9 One Nut and Two Boys
0 Saviors of the Forest
5 A Magic wand
5 Amanda's Adventure
4 Friends
5 Jack Is Looking for Friends
5 A Little Story about Friendship
3 Beaver Benny 
11 Why Do Grasshoppers Jump?
9 A Kind Smile of the Rain
4 The Aye-Aye
12 An Orange Hare
7 Great Adventures
8 Underwater Christmas
5 A Lesson for Friends
11 A Fairy Tale
5 A Little Adventure
13 Her Majesty the Night
7 A Fairy and her Fairy Dust
4 A Magic Attic
15 Bad Advice
6 A Big Secret
6 School of Magic
5 A Little Giraffe
5 Best Friends
9 Five Knights and Stolen Gold
5 Two Chipmunks
5 The Smiths"""
cnt = 6
for elem in s.split('\n'):
    num, title = int(elem.split()[0]), elem.split()[1:]
    for i in range(num):
        print(cnt)
    cnt += 1
    if cnt == 20:
        cnt += 1
    if cnt == 40:
        cnt += 1
