class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        
user_1 = User("001", "angela")
user_2 = User("002", "jack")

print(user_1.username)

##Testing the use of methods:

# print(f"Followers user_1: {user_1.followers}")
# print(f"Following user_1: {user_1.following}")

# print(f"Followers user_2: {user_2.followers}")
# print(f"Following user_2: {user_2.following}")

# user_1.follow(user_2)

# print("-----------------------------")

# print(f"Followers user_1: {user_1.followers}")
# print(f"Following user_1: {user_1.following}")

# print(f"Followers user_2: {user_2.followers}")
# print(f"Following user_2: {user_2.following}")