import requests
import couchdb
import easygui
from overmodem import overmodem
couch=couchdb.Server()
modem=overmodem('COM9')
db=couch['mydb']
r=requests.get("http://localhost:5984/mydb/_design/notsentdesign/_view/notsentview")
output=r.json()
for row in output['rows']:
	if ("Message" in row['value']) & ("Numbers" in row['value']):
		numbers=row['value']['Numbers'].split(',')
		message=row['value']['Message']
		mid=row['key']
		sent_numbers={}
		response=[]
		if modem.working_modem:
			for number in numbers:
					response=modem.sms(int(number),message)
					sent_numbers[number]=response
					
			doc=db.get(mid)
			doc['sent']=True
			doc['response']=sent_numbers
			db.save(doc)

		else:
			easygui.msgbox('Your modem is not plugged in!', 'Modem update')


