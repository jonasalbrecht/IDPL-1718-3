>>> [i for i in [1, 2, None] if i != None]
[1, 2]
>>> filter(lambda x: x != None, [1, 2, None])
[1, 2]
