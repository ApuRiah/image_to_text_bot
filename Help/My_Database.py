# My database for saving file_path
# Storage path file image in dictionary

my_database = {}
#save your chooosing languge
my_languge = {}
def insert_languge(chat_id:int, message_id:int, Mlanguge:str) -> None:
    try:
        my_languge[chat_id][message_id] = Mlanguge
    except KeyError:
        my_languge[chat_id] = {}
        my_languge[chat_id][message_id] = "Eng"

def get_languge(chat_id:int, message_id:int):
    try:
        Mlanguge = my_languge[chat_id][message_id]
        if Mlanguge is None :
            return "Eng"
        return Mlanguge
    except KeyError:
        return "Eng"
#Save file path img chat_id:massege_id:file path
def insert_file_path(chat_id:int, message_id:int, file_path:str) -> None:
    try:
        my_database[chat_id][message_id] = file_path
    except KeyError:
        my_database[chat_id] = {}
        my_database[chat_id][message_id] = file_path

def get_file_path(chat_id:int, message_id:int):
    try:
        file_path = my_database[chat_id][message_id]
        del my_database[chat_id][message_id]
        return file_path
    except KeyError:
        return None
