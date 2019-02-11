users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]


def num_friends(user):
    count = 0
    id = 0
    for i in users:
        if i["name"] == user:
            id = i["id"]

    for x in friendship:
        for y in x:
            if y == id:
                count += 1
    return count


def sort_by_num_friends():
    friends = []
    for i in users:
        friends.append((num_friends(i["name"]), i["name"]))
    friends.sort(reverse=True)
    return friends


X = sort_by_num_friends()
for i in X:
    print('{} has {} friends'.format(i[1], i[0]))