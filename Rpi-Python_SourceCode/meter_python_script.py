import GoogleSheetsPyAPI as gsp
import my_text_module   as txt
from datetime import datetime
from threading import Timer

SheetID = '1-A7x_W7RNImgUUj8LIsDAM5GBiopJsOxDZLWydZW3b4'
KeyFile = 'My Project-a7f7a4e8569b.json'

gsp.GoogleSheetsInit(KeyFile,SheetID)
txt.DisplaInit()



gsp.ClearRange("PerDay!A2:D")

Power = 1
Energy = 1
pf = 1


def UpdateSheet():
    global Power
    global Energy
    global pf
    current_date = datetime.now().strftime("%d-%B,%H:%M:%S")
    Power += 1
    Energy += 1
    pf += 1
    updated = [[current_date,Power,Energy,pf]]
    print("writing new values: current time={} \nPower={}, Energy={}, pf={}".format(current_date,Power,Energy,pf))
    gsp.AppendRange("PerDay!A2",updated)
    print("Done...")
    Timer_PerDay=Timer(2,UpdateSheet)
    Timer_PerDay.start()


Timer_PerDay=Timer(2,UpdateSheet)
Timer_PerDay.start()

while True:
    
    pass