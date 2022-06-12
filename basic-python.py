import time
friend = []
friend.append('James')
print(friend)
['James']
friend.append('Jo')
print(friend)
['James', 'Jo']
friend.append('Noy')
print(friend)
['James', 'Jo', 'Noy']
friend.insert(2, 'Tom')
print(friend)
['James', 'Jo', 'Tom', 'Noy']
print(len(friend))
4
girl = friend[3]
print(friend)
['James', 'Jo', 'Tom', 'Noy']
print(girl)
Noy
print(friend[-1])
Noy
print(friend[-2])
Tom
for f in friend:
    print(f)


James
Jo
Tom
Noy
for i in range(10):
    print(i)


0
1
2
3
4
5
6
7
8
9
for i in range(1, 11):
    print(i)


1
2
3
4
5
6
7
8
9
10
for i in range(1, 11):
    print(i+1)
    time.sleep(1)


2
3
4
5
6
7
8
9
10
11
for i in range(10):
    print(i+1)
    time.sleep(1)


1
2
3
4
5
6
7
8
9
10
for i in range(10):
    print(10-i)
    time.sleep(1)


10
9
8
7
6
5
4
3
2
1
for i in range(10):
    print(10-i)
    time.sleep(3)


10
9
8
7
6
5
4
3
2
1
for i in range(1, 10):
    print(i)
    time.sleep(1)


1
2
3
4
5
6
7
8
9
for i in range(1, 11):
    print(i)
    time.sleep(0)


1
2
3
4
5
6
7
8
9
10
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(7, 11))
[7, 8, 9, 10]
list(range(2, 10, 2))
[2, 4, 6, 8]
list(range(2, 10, 3))
[2, 5, 8]
num = [10, 20, 30, 40]
print(num[:2])
[10, 20]
print(num[2:])
[30, 40]
friend
['James', 'Jo', 'Tom', 'Noy']
friend.remove('Noy')
friend
['James', 'Jo', 'Tom']
del friend[0]
friend
['Jo', 'Tom']
