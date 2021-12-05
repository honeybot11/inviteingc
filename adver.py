import aminofix as amino
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.THISTLE_1 + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminoadvbov2", font="slant"))

def main():
	client = amino.Client()    
	email = input("Email >> ")
	password = input("Password >> ")
	message = input("Message >> ")
	client.login(email=email, password=password)
	clients = client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	com_Id = clients.comId[int(input("Select the community >> "))-1]
	sub_client = amino.SubClient(comId=com_Id, profile=client.profile)
	while True:
		try:
			users = sub_client.get_online_users(start=0, size=100)
			for user_Id, level, nickname in zip(users.profile.userId, users.profile.level, users.profile.nickname):
				sub_client.start_chat(userId=[sub_client.profile.userId, user_Id], message=message)
				print(f"Sended Advertise {nickname}, level = {level}")
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"VerificationRequired")
			link = e.args[0]['url']
			print(link)
			verify = input("Waiting for verification >> ")
		except Exception as e:
			print(e)

main()