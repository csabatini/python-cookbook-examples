class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User(%s)' % self.user_id


users = [User(55), User(23), User(3), User(99)]

# sorted() can be passed a callable that will return the attribute of the objects to sort on
users_by_id = sorted(users, key=lambda u: u.user_id)
print users_by_id
# [User(3), User(23), User(55), User(99)]

users_by_id_reverse = sorted(users, key=lambda u: u.user_id, reverse=True)
print users_by_id_reverse
# [User(99), User(55), User(23), User(3)]
