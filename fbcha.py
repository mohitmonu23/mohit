import fbchat
from fbchat.models import *
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
	name = str(input("Name: "))
	friends = client.searchForUsers(name) # return a list of names
	friend = friends[0]
	msg = str(input("Message: "))
	sent = client.send(Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)
	if sent:
		print("Message sent successfully!")
