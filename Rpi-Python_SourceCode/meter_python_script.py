# project specific imports
import GoogleSheetsPyAPI as gsp
import my_text_module   as txt
import myUART as uart

# standard library imports
from datetime import datetime
from threading import Timer, Thread, Lock


SheetID = '1-A7x_W7RNImgUUj8LIsDAM5GBiopJsOxDZLWydZW3b4'
KeyFile = 'My Project-a7f7a4e8569b.json'

UpdatePeriod = 2        # in seconds , set to 3600 seconds for 1 Hour UPdate Period
Hours = 0
Days = 0
Months = 0
Years = 0

LINE_OFFSET = 25


Power = 0.0
Energy = 0.0

P_real = list()
P_rms = list()    # Irms*Vrms
e_inst = list()   # P_rms * Time_increment , Time_increment = 78 us * 256 sample = 20 ms
PowerFactor = 0.0

gsp.GoogleSheetsInit(KeyFile,SheetID)
txt.DisplayInit()

def Accumalate():
    global P_rms
    global Power
    global Energy
    global e_inst
    global PowerFactor

    Energy = sum(e_inst)/(60*60*1000)       # in KWH [1/60x60x1000]
    try:
        Power  = (sum(P_rms)/len(P_rms))/1000   # in KW
        PowerFactor = abs(Power/(sum(P_real)/len(P_real)))
    except ZeroDivisionError:
        return -1

def DisplayAllText():
    global Power
    global Energy
    global PowerFactor
    while True:
        txt.DisplayClear()
        txt.DisplayRotatedText( "Power= {:.3f} KW".format(Power), (15, 20), 90, fill=(255,255,255))
        txt.DisplayRotatedText( "Energy= {:.3f} KWH".format(Energy), (15+(LINE_OFFSET*1), 20), 90,  fill=(255,255,255))
        txt.DisplayRotatedText( "Power Factor= {:.3f}".format(PowerFactor), (15+(LINE_OFFSET*2), 20), 90, fill=(255,255,255))
        txt.DisplayShow()


def UpdateSheet():
    global Power
    global Energy
    global PowerFactor
    global Hours
    global Days
    global Months

    current_date = datetime.now().strftime("%d-%B,%H:%M:%S")
    Accumalate()
    updated = [[current_date,Power,Energy,PowerFactor]]

    Hours += 1

    if Hours==23:
        Days+=1
        Hours = 0
        # print("writing new values: current time={} \nPower={}, Energy={}, pf={}".format(current_date,Power,Energy,PowerFactor))
        gsp.AppendRange("PerMonth!A2",updated)
        # print("Done...")
        gsp.ClearRange("PerDay!A2:D")

    elif Hours != 0:
        # print("writing new values: current time={} \nPower={}, Energy={}, pf={}".format(current_date,Power,Energy,PowerFactor))
        gsp.AppendRange("PerDay!A2",updated)
        # print("Done...")

    if Days==30: 
        # TODO: add more complicated logic here to account for each
        # month's number of days and caluclate how far are we 
        # from the end of the month and  so on
        Months += 1
        Days = 0
        gsp.ClearRange("PerMonth!A2:D")

    if Months == 11:
        Years +=1
        Months=0 

    
    Timer_PerDay=Timer(UpdatePeriod,UpdateSheet)
    Timer_PerDay.start()

def FillQueue(the_lock):
    global P_rms
    global e_inst
    global P_real

    while True:
        line=uart.Getline()
        print(line)
        line = line.rstrip("\r\n")
        line = line.split(",")
        P_rms_temp = float(line[0])*float(line[1])
        with the_lock:
            P_rms.append(P_rms_temp)
            P_real.append(float(line[2]))
            e_inst.append(P_rms_temp*2e-3)    # each 20 ms



gsp.ClearRange("PerDay!A2:D")
gsp.ClearRange("PerMonth!A2:D")

uart.Init()

lock = Lock()
uart_thread = Thread(target=FillQueue, args=(lock, ))
display_thread = Thread(target=DisplayAllText)

uart_thread.daemon = True
display_thread.daemon = True

uart_thread.start()
display_thread.start()

Timer_PerDay=Timer(UpdatePeriod,UpdateSheet)
Timer_PerDay.start()


while True:
    # infinite loop that does nothing
    # all program logic is handled inside Threads
    pass