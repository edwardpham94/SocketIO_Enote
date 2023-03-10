from pymongo import MongoClient
import socket
import pickle

cluster = MongoClient(
    "mongodb+srv://thanhanphan17:05062003@cluster0.dwxs1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["e-note"]
clt = db["note"]

notes = clt.find()


def convert_to_list(notes):
    tmp = []

    for x in notes:
        tmp.append(x)

    return tmp


def send_all_note(conn, username):
    global notes
    new_note = []
    notes = convert_to_list(notes)

    for x in notes:
        if x["author"] == username:
            new_note.append(x)

    # print(new_note)
    data = pickle.dumps(new_note)
    conn.sendall(data)
