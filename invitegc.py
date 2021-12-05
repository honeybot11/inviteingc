import aminofix as amino
import concurrent.futures, pyfiglet
from threading import Thread
from colorama import init, Fore, Back, Style
init()
print(Fore.RED + Style.NORMAL)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminoinvitebo", font="small"))
client = amino.Client()
client.login(email=input("Email >> "), password=input("Password >> "))
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_Id = clients.comId[int(input("Select the community >> ")) - 1]
sub_client = amino.SubClient(comId=com_Id, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
    print(f"{z}.{title}")
chat_Id = chats.chatId[int(input("Select the chat >> ")) - 1]

# invite functions
# thanks to https://github.com/LynxN1 for example


def invite_online_users():
    with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
        for i in range(0, 2000, 250):
            online_users = sub_client.get_online_users(start=i, size=100)
            if online_users:
                for nickname, user_Id in zip(
                    online_users.profile.nickname, online_users.profile.userId
                ):
                    print(f"{nickname} Invited...")
                    _ = [executor.submit(sub_client.invite_to_chat, user_Id, chat_Id)]
                    j = Thread(
                        target=sub_client.invite_to_chat, args=[user_Id, chat_Id]
                    ).start()
            else:
                break
        for i in range(0, 2000, 250):
            public_chats = sub_client.get_public_chat_threads(
                type="recommended", start=i, size=100
            ).chatId
            joined_chats = sub_client.get_chat_threads(start=i, size=100).chatId
            chats = [*public_chats, *joined_chats]
            if chats:
                for chat_id in chats:
                    for i in range(0, 1000, 50):
                        chat_users = sub_client.get_chat_users(
                            chatId=chat_id, start=i, size=100
                        )
                        if chat_users:
                            for nickname, user_Id in zip(
                                chat_users.nickname, chat_users.userId
                            ):
                                try:
                                    print(f"{nickname} Invited...")
                                    _ = [
                                        executor.submit(
                                            sub_client.invite_to_chat, user_Id, chat_Id
                                        )
                                    ]
                                    j = Thread(
                                        target=sub_client.invite_to_chat,
                                        args=[user_Id, chat_Id],
                                    ).start()
                                except:
                                    pass
                        else:
                            break
                            print("Invited Online Users...")


def invite_user_followers():
    user_Info = client.get_from_code(input("User Link >> "))
    object_Id = user_Info.objectId
    with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
        for i in range(0, 2000, 250):
            user_followers = sub_client.get_user_followers(
                userId=object_Id, start=i, size=100
            )
            if user_followers:
                for nickname, user_Id in zip(
                    user_followers.profile.nickname, user_followers.profile.userId
                ):
                    print(f"{nickname} Invited...")
                    _ = [executor.submit(sub_client.invite_to_chat, user_Id, chat_Id)]
                    j = Thread(
                        target=sub_client.invite_to_chat, args=[user_Id, chat_Id]
                    ).start()
            else:
                break
                print("Invited User Followers...")


def invite_recent_users():
    with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
        for i in range(0, 2000, 250):
            recent_users = sub_client.get_all_users(type="recent", start=i, size=100)
            if recent_users:
                for nickname, userId in zip(
                    recent_users.profile.nickname, recent_users.profile.userId
                ):
                    print(f"{nickname} Invited")
                    _ = [executor.submit(sub_client.invite_to_chat, user_Id, chat_Id)]
                    j = Thread(
                        target=sub_client.invite_to_chat, args=[user_Id, chat_Id]
                    ).start()
            else:
                break
                print("Invited Recent Users...")


# invite functions
# thanks to https://github.com/LynxN1 for example
print(
    """[1] Invite Online Users
[2] Invite User Followers
[3] Invite Recent Users"""
)
select = input("Select >> ")
if select == "1":
    invite_online_users()

elif select == "2":
    invite_user_followers()

elif select == "3":
    invite_recent_users()