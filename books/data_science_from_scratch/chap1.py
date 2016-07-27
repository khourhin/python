"""
Chapter One from "Data science from scratch"
"""

import logging as log
import itertools
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict, Counter

log.basicConfig(level=log.INFO, format='')


# Data
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

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]

user_ids_by_interest = defaultdict(list)
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    interests_by_user_id[user_id].append(interest)
    

class User(object):
    count = 0
    connections = 0
    _registry = []
    
    def __init__(self, id, name, friendships):
        self._registry.append(self)
        self.id = id
        self.name = name
        self.friends = self.set_friends(friendships)
        User.count += 1
        User.connections += len(self.friends)

    def set_friends(self, friendships):

        friends = []
        for i, j in friendships:
            if i == self.id:
                friends.append(j)
            if j == self.id:
                friends.append(i)

        return set(friends)

    def get_friends_of_friends(self):
        foaf = set(itertools.chain(*[x.friends for x in self._registry
                                     if x.id in self.friends]))
        foaf = foaf - set(self.friends)
        
        return foaf

    def get_friends_in_common(self, other_user):
        return self.friends & other_user.friends

    
def find_by_interest(target_interest):
    return [user_id for user_id, interest in interests
            if interest == target_interest]


def most_common_interests_with(user_id):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user_id]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user_id)


def most_popular_interests(interests):
    return (Counter(word
            for user_id, interest in interests
            for word in interest.lower().split()))


if __name__ == "__main__":
    for user in users:
        log.info('Registering user: {}'.format(user['name']))
        User(user['id'], user['name'], friendships)

    # Output stats
    log.info('Total number of users: {}'.format(User.count))
    log.info('Total number of connections: {}'.format(User.connections))
    log.info('Average number of friends per user: {}'.format(User.connections /
                                                             User.count))
    # Iterate through User objects:
    for user in User._registry:
        log.info('User: %s' % user.name)
        log.info(user.get_friends_of_friends())
        
    # Print sorted by number of friends
    for u in sorted(User._registry,
                    key=lambda user: len(user.friends),
                    reverse=True):
        log.info('{0} {1} {2}'.format(u.id, u.name, u.friends))

    # Print friends in common:
    for u1, u2 in itertools.combinations(User._registry, 2):
        log.info("Friends in common for {0} and {1}: {2}".format(
            u1.name, u2.name, len(u1.get_friends_in_common(u2))))
        
    # Print ids by interest:
    log.info([user.name for user in User._registry
              if user.id in find_by_interest('Hadoop')])

    print(most_common_interests_with(0))

    # Graph the interests_by_user_id
    t = most_popular_interests(interests)
    print(t)
    labels, values = zip(*t.items())
    indexes = np.arange(len(labels))
    width = 1
    
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels, rotation=90)
    plt.show()
