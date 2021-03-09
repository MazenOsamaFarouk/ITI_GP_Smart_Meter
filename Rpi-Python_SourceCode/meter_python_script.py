import GoogleSheetsPyAPI as gsp
import my_text_module   as txt
from datetime import datetime
from threading import Timer, Thread

SheetID = '1-A7x_W7RNImgUUj8LIsDAM5GBiopJsOxDZLWydZW3b4'
KeyFile = 'My Project-a7f7a4e8569b.json'

UpdatePeriod = 2        # in seconds 
Power = 1
Energy = 1
pf = 1
LINE_OFFSET = 25

gsp.GoogleSheetsInit(KeyFile,SheetID)
txt.DisplayInit()

def DisplayAllText():
    global Power
    global Energy
    global pf
    txt.DisplayClear()
    txt.DisplayRotatedText( "Power= {} KW".format(Power), (15, 20), 90, fill=(255,255,255))
    txt.DisplayRotatedText( "Energy= {} KWH".format(Energy), (15+(LINE_OFFSET*1), 20), 90,  fill=(255,255,255))
    txt.DisplayRotatedText( "Power Factor= {}".format(pf), (15+(LINE_OFFSET*2), 20), 90, fill=(255,255,255))
    txt.DisplayShow()


def UpdateSheet():
    global Power
    global Energy
    global pf
    current_date = datetime.now().strftime("%d-%B,%H:%M:%S")
    Power += 1
    Energy += 1
    pf += 1
    DisplayAllText()
    updated = [[current_date,Power,Energy,pf]]
    print("writing new values: current time={} \nPower={}, Energy={}, pf={}".format(current_date,Power,Energy,pf))
    gsp.AppendRange("PerDay!A2",updated)
    print("Done...")
    Timer_PerDay=Timer(UpdatePeriod,UpdateSheet)
    Timer_PerDay.start()




gsp.ClearRange("PerDay!A2:D")

Timer_PerDay=Timer(UpdatePeriod,UpdateSheet)
Timer_PerDay.start()
while True:
    
    pass