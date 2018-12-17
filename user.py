import json
import mysql.connector
from flask import request
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='users',
                                       user='root',
                                       port="3301",
                                       password='root')
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)



def read():
    conn=connect()
    cursor=conn.cursor()
    query = ("Select * From users")
    cursor.execute(query)
    records = cursor.fetchall()
    dico = {}
    i = 0
    for row in records:
        dico[i] = {row[0]: {
            "nom": row[1],
            "prenom": row[2],
            "mdp": row[3],
            "ddn": row[4],
            "mail": row[5],
            "adr_livraison": row[6],
            "code_pos": row[7],
            "ville": row[8],
            "pays": row[9],
            "tel": row[10],
            "num_carte": row[11],
            "username": row[12]
        }}
        i = i + 1
    cursor.close()
    return [dico[key] for key in sorted(dico.keys())]

def insert():
    conn = connect()
    cursor = conn.cursor()
    try :
        query = "INSERT INTO users(nom,prenom,mdp,ddn,mail,adr_livraison,code_pos,ville,pays,tel," \
                    "num_carte,username)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(query,(request.form["nom"], request.form["prenom"]
                           ,request.form["mdp"],request.form["ddn"],request.form["mail"],
                           request.form["adr_liv"], request.form["code"], request.form["ville"],
                           request.form["pays"],request.form["tel"], request.form["carte"],
                           request.form["username"]))
        conn.commit
    except Error as e:
        print(e)
    return "succes",200



def getid(id):
    conn = connect()
    cursor=conn.cursor()
    try:
        cursor.execute("Select * From users where username =  %s;",(id,))
        records = cursor.fetchall()
    except Error as e:
        return 0,404
    dico = {}
    i = 0
    for row in records:
        dico = {row[0]: {
            "nom": row[1],
            "prenom": row[2],
            "mdp": row[3],
            "ddn": row[4],
            "mail": row[5],
            "adr_livraison": row[6],
            "code_pos": row[7],
            "ville": row[8],
            "pays": row[9],
            "tel": row[10],
            "num_carte": row[11],
            "username": row[12]
        }}
    cursor.close()
    if bool(dico) :
        return [dico[key] for key in sorted(dico.keys())]
    else :
        return 0,404