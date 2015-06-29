import requests
import couchdb
import easygui
couch=couchdb.Server()
db=couch['mydb']
try:
    print "accessing server"
    r=requests.get("http://*********")
    items=r.json()
    for item in items:
        item_db=item
        item_db['sent']=False
        db.save(item_db)
except Exception as e:
    easygui.msgbox('Cant connect to messaging server contact ', 'Server')
            
