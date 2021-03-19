EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Energy Meter Board"
Date "2021-03-18"
Rev "V1.0"
Comp ""
Comment1 "made for: ITI Graduation Project "
Comment2 "designed by: Mazen OSama Faoruk"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L YAAJ_BluePill:YAAJ_BluePill U1
U 1 1 6054606E
P 5200 4850
F 0 "U1" H 5200 3519 50  0000 C CNN
F 1 "YAAJ_BluePill" H 5200 3428 50  0000 C CNN
F 2 "STM32_BluePill:YAAJ_BluePill_1" V 5125 5800 50  0001 C CNN
F 3 "" V 5125 5800 50  0001 C CNN
	1    5200 4850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J2
U 1 1 6054E954
P 2100 5150
F 0 "J2" V 2064 4962 50  0000 R CNN
F 1 "Screw_Terminal_01x02" V 2200 5400 50  0000 R CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal" H 2100 5150 50  0001 C CNN
F 3 "~" H 2100 5150 50  0001 C CNN
	1    2100 5150
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J1
U 1 1 6054EBDC
P 2050 4100
F 0 "J1" V 2014 3912 50  0000 R CNN
F 1 "Screw_Terminal_01x02" V 2200 4350 50  0000 R CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal" H 2050 4100 50  0001 C CNN
F 3 "~" H 2050 4100 50  0001 C CNN
	1    2050 4100
	0    -1   -1   0   
$EndComp
$Comp
L power:+3V3 #PWR0101
U 1 1 60552555
P 6550 850
F 0 "#PWR0101" H 6550 700 50  0001 C CNN
F 1 "+3V3" H 6565 1023 50  0000 C CNN
F 2 "" H 6550 850 50  0001 C CNN
F 3 "" H 6550 850 50  0001 C CNN
	1    6550 850 
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR0102
U 1 1 60552EA6
P 10100 1200
F 0 "#PWR0102" H 10100 950 50  0001 C CNN
F 1 "GNDREF" H 10105 1027 50  0000 C CNN
F 2 "" H 10100 1200 50  0001 C CNN
F 3 "" H 10100 1200 50  0001 C CNN
	1    10100 1200
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR0104
U 1 1 6056F9EE
P 5000 6100
F 0 "#PWR0104" H 5000 5850 50  0001 C CNN
F 1 "GNDREF" H 5005 5927 50  0000 C CNN
F 2 "" H 5000 6100 50  0001 C CNN
F 3 "" H 5000 6100 50  0001 C CNN
	1    5000 6100
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0105
U 1 1 605702B3
P 5300 3550
F 0 "#PWR0105" H 5300 3400 50  0001 C CNN
F 1 "+3V3" H 5315 3723 50  0000 C CNN
F 2 "" H 5300 3550 50  0001 C CNN
F 3 "" H 5300 3550 50  0001 C CNN
	1    5300 3550
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0106
U 1 1 60570C28
P 9400 3950
F 0 "#PWR0106" H 9400 3800 50  0001 C CNN
F 1 "+3V3" H 9415 4123 50  0000 C CNN
F 2 "" H 9400 3950 50  0001 C CNN
F 3 "" H 9400 3950 50  0001 C CNN
	1    9400 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 3550 5300 3750
Wire Wire Line
	5000 5950 5000 6100
Wire Wire Line
	9400 3950 9400 4000
Wire Wire Line
	9600 4200 9600 4000
Wire Wire Line
	9600 4000 9400 4000
Connection ~ 9400 4000
Wire Wire Line
	9400 4000 9400 4200
Wire Wire Line
	9500 4200 9500 4100
Wire Wire Line
	9500 4100 9700 4100
Text GLabel 9700 4100 2    50   Input ~ 0
DISP_RST
Wire Wire Line
	8650 5200 8550 5200
Wire Wire Line
	8650 5300 8500 5300
Wire Wire Line
	8650 5400 8500 5400
Text GLabel 8550 5200 0    50   Input ~ 0
DISP_A0
Text GLabel 8500 5300 0    50   Input ~ 0
DISP_SDA
Text GLabel 8500 5400 0    50   Input ~ 0
DISP_SCK
Text GLabel 6500 2600 0    50   Input ~ 0
DISP_A0
Text GLabel 6500 3000 0    50   Input ~ 0
DISP_RST
Text GLabel 6500 1800 0    50   Input ~ 0
RPi_UART_RX
Text GLabel 10100 1000 2    50   Input ~ 0
DISP_CS
Text GLabel 6550 2700 0    50   Input ~ 0
DISP_SDA
Text GLabel 10050 900  2    50   Input ~ 0
DISP_SCK
Wire Wire Line
	10100 1100 10100 1200
Wire Wire Line
	6550 900  6550 850 
Wire Wire Line
	4400 4550 4250 4550
Text GLabel 4250 4550 0    50   Input ~ 0
RPi_UART_RX
Wire Wire Line
	6000 5150 6200 5150
Wire Wire Line
	6000 5250 6200 5250
Text GLabel 6200 5150 2    50   Input ~ 0
CURRENT_SENSOR
Text GLabel 6200 5250 2    50   Input ~ 0
VOLTAGE_SENSOR
$Comp
L power:+3V3 #PWR0107
U 1 1 60588909
P 2150 4450
F 0 "#PWR0107" H 2150 4300 50  0001 C CNN
F 1 "+3V3" V 2165 4578 50  0000 L CNN
F 2 "" H 2150 4450 50  0001 C CNN
F 3 "" H 2150 4450 50  0001 C CNN
	1    2150 4450
	0    1    1    0   
$EndComp
$Comp
L power:GNDREF #PWR0108
U 1 1 60589134
P 2000 4450
F 0 "#PWR0108" H 2000 4200 50  0001 C CNN
F 1 "GNDREF" V 2005 4322 50  0000 R CNN
F 2 "" H 2000 4450 50  0001 C CNN
F 3 "" H 2000 4450 50  0001 C CNN
	1    2000 4450
	0    1    1    0   
$EndComp
Wire Wire Line
	2050 4300 2050 4450
Wire Wire Line
	2050 4450 2000 4450
Wire Wire Line
	2150 4450 2150 4300
Text GLabel 2200 5450 2    50   Input ~ 0
CURRENT_SENSOR
Text GLabel 2100 5450 0    50   Input ~ 0
VOLTAGE_SENSOR
Wire Wire Line
	2100 5450 2100 5350
Wire Wire Line
	2200 5450 2200 5350
Text GLabel 8550 5100 0    50   Input ~ 0
DISP_CS
Wire Wire Line
	8550 5100 8650 5100
Wire Wire Line
	9400 5750 9400 5600
$Comp
L power:GNDREF #PWR0103
U 1 1 6056F1E0
P 9400 5750
F 0 "#PWR0103" H 9400 5500 50  0001 C CNN
F 1 "GNDREF" H 9405 5577 50  0000 C CNN
F 2 "" H 9400 5750 50  0001 C CNN
F 3 "" H 9400 5750 50  0001 C CNN
	1    9400 5750
	1    0    0    -1  
$EndComp
$Comp
L TFT_ST7735_symbol:TFT_ST7735_symbol U3
U 1 1 6054C1C8
P 9200 4700
F 0 "U3" H 8800 5150 50  0000 L CNN
F 1 "TFT_ST7735_symbol" H 9150 4150 50  0000 L CNN
F 2 "TFT_ST7735_footprint:ST7735_TFT_DISP" H 9150 4900 50  0001 C CNN
F 3 "" H 9150 4900 50  0001 C CNN
	1    9200 4700
	1    0    0    -1  
$EndComp
$Comp
L Raspberry_Pi_2_or_3:Raspberry_Pi_2_3 RP1
U 1 1 605AFFA9
P 6850 900
F 0 "RP1" H 8300 1165 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 8300 1074 50  0000 C CNN
F 2 "Raspberry-Pi-3-library-for-kicad-master:raspberrypi2" H 8050 1800 50  0001 L CNN
F 3 "https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/PiZero_1.pdf" H 8050 1500 50  0001 L CNN
F 4 "Raspberry Pi Zero 2 or 3 Single-board Computers" H 8050 1400 50  0001 L CNN "Description"
F 5 "RASPBERRY-PI" H 8050 1700 50  0001 L CNN "Manufacturer_Name"
F 6 "Raspberry Pi 2 or 3" H 8050 1600 50  0001 L CNN "Manufacturer_Part_Number"
	1    6850 900 
	1    0    0    -1  
$EndComp
Wire Wire Line
	6550 900  6850 900 
Wire Wire Line
	9750 1100 10100 1100
Wire Wire Line
	6500 1800 6850 1800
Wire Wire Line
	9750 900  10050 900 
Wire Wire Line
	9750 1000 10100 1000
Wire Wire Line
	6500 2600 6850 2600
Wire Wire Line
	6550 2700 6850 2700
Wire Wire Line
	6500 3000 6850 3000
$EndSCHEMATC
