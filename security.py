from werkzeug.security import safe_str_cmp
from user import User

# THESE ARE OLD WAY AND HARD CODED
# SO WE CREATED A CLASS TO CREATED USER FOR EASITY AND ACESS THEM
# users = [
# 	{
# 		'id': 1,
# 		'username': 'bob',
# 		'password': 'superstrong'
# 	}
# ]


# username_mapping = { 
# 	'bob': {
# 		'id': 1,
# 		'username': 'bob',
# 		'password': 'superstrong'
# 	}
# }


# userid_mapping = {
# 	1: {
# 		'id': 1,
# 		'username': 'bob',
# 		'password': 'superstrong'
# 	}
# }

users = [
	User(1, 'bob', 'testing123')
]


username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
	# .get() is a way to access the key of a dictionary
	# None is the default value
	user = username_mapping.get(username, None)  

	# it is not a good idea to compare string directly. instead we will use safe string compare(safe_str_cmp)
	# if user and user.password == password:
	if user and safe_str_cmp(user.password, password):
		return user


# generate unique JWT Token for each user
def indentity(payload):
	user_id = payload['indentity']
	return userid_mapping.get(user_id, None)