from array import array
import heapq
from typing import Any
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

array0000_0199 = ['P0000 No trouble code', 'P0001 Fuel Volume Regulator Control Circuit / Open', 'P0003 Fuel Volume Regulator Control Circuit Low', 'P0004 Fuel Volume Regulator Control Circuit High', 'P0005 Fuel Shutoff Valve Control Circuit / Open', 'P0006 Fuel Shutoff Valve Control Circuit Low', 'P0007 Fuel Shutoff Valve Control Circuit High', 'P0008 Engine Position System Performance - Bank 1', 'P0009 Engine Position System Performance - Bank 1', 'P0010 Intake Camshaft Position Actuator Circuit / Open (Bank 1)', 'P0011 Intake Camshaft Position Timing - Over-Advanced (Bank 1)', 'P0012 Intake Camshaft Position Timing - Over-Retarded (Bank 1)', 'P0013 Exhaust Camshaft Position Actuator Circuit / Open (Bank 1)', 'P0014 Exhaust Camshaft Position Timing - Over-Advanced (Bank 1)', 'P0015 Exhaust Camshaft Position Timing - Over-Retarded (Bank 1)', 'P0016 Crankshaft Position Camshaft Position Correlation Bank 1 Sensor A', 'P0017 Crankshaft Position Camshaft Position Correlation Bank 1 Sensor B', 'P0018 Crankshaft Position Camshaft Position Correlation Bank 2 Sensor A', 'P0019 Crankshaft Position Camshaft Position Correlation Bank 2 Sensor B', 'P0020 Intake Camshaft Position Actuator Circuit / Open (Bank 2)', 'P0021 Intake Camshaft Position Timing - Over-Advanced (Bank 2)', 'P0022 Intake Camshaft Position Timing - Over-Retarded (Bank 2)', 'P0023 Exhaust Camshaft Position Actuator Circuit / Open (Bank 2)', 'P0024 Camshaft Position B - Timing Over-Advanced or System Performance (Bank 2)', 'P0025 Exhaust Camshaft Position Timing - Over-Retarded (Bank 2)', 'P0026 Intake Valve Control Solenoid Circuit Range/Performance (Bank 2)', 'P0027 Exhaust Valve Control Solenoid Circuit Range/Performance (Bank 2)', 'P0028 Intake Valve Control Solenoid Circuit Range/Performance (Bank 2)', 'P0029 Exhaust Valve Control Solenoid Circuit Range/Performance (Bank 2)', 'P0030 Heated Oxygen Sensor (H02S) Heater Control Circuit Bank 1 Sensor 1', 'P0031 Heated Oxygen Sensor (HO2S) Heater Circuit Low Voltage Bank 1 Sensor 1', 'P0032 Heated Oxygen Sensor (HO2S) Heater Circuit High Voltage Bank 1 Sensor 1', 'P0033 Turbo/Super Charger Bypass Valve Control Circuit / Open', 'P0034 Turbo/Super Charger Bypass Valve Control Circuit Low', 'P0035 Turbo/Super Charger Bypass Valve Control Circuit High', 'P0036 Heated Oxygen Sensor (HO2S) Heater Control Circuit Bank 1 Sensor 2', 'P0037 Heated Oxygen Sensor (HO2S) Heater Circuit Low Voltage Bank 1 Sensor 2', 'P0038 Heated Oxygen Sensor (HO2S) Heater Circuit High Voltage Bank 1 Sensor 2', 'P0039 Turbo/Super Charger Bypass Valve Control Circuit Range/Performance', 'P0040 Oxygen Sensor Signals Swapped Bank 1 Sensor 1 / Bank 2 Sensor 1', 'P0041 Oxygen Sensor Signals Swapped Bank 1 Sensor 2 / Bank 2 Sensor 2', 'P0042 HO2S Heater Control Circuit (Bank 1, Sensor 3)', 'P0043 HO2S Heater Control Circuit Low (Bank 1, Sensor 3)', 'P0044 HO2S Heater Control Circuit High (Bank 1, Sensor 3)', "P0046 Turbocharger/Supercharger Boost Control 'A' Circuit Range/Performance", "P0047 Turbocharger/Supercharger Boost Control 'A' Circuit Low", "P0048 Turbocharger/Supercharger Boost Control 'A' Circuit High", 'P0049 Turbo/Super Charger Turbine Overspeed', 'P0050 Heated Oxygen Sensor (HO2S) Heater Circuit Bank 2 Sensor 1', 'P0051 Heated Oxygen Sensor (HO2S) Heater Circuit Low Voltage Bank 2 Sensor 1', 'P051B Crankcase Pressure Sensor Circuit Range/Performance', 'P0052 Heated Oxygen Sensor (HO2S) Heater Circuit High Voltage Bank 2 Sensor 1', 'P0053 HO2S Heater Resistance Bank 1 Sensor 1 (PCM)', 'P0054 HO2S Heater Resistance Bank 1 Sensor 2 (PCM)', 'P0055 HO2S Heater Resistance Bank 1 Sensor 3 (PCM)', 'P0056 Heated Oxygen Sensor (HO2S) 2, Bank 2, Heater control - Circuit Malfunction', 'P0057 Heated Oxygen Sensor (HO2S) Heater Circuit Low Voltage Bank 2 Sensor 2', 'P0058 Heated Oxygen Sensor (HO2S) Heater Circuit High Voltage Bank 2 Sensor 2', 'P0059 HO2S Heater Resistance (Bank 2, Sensor 1)', 'P0060 HO2S Heater Resistance (Bank 2, Sensor 2)', 'P0061 HO2S Heater Resistance (Bank 2, Sensor 3)', 'P0062 HO2S Heater Control Circuit (Bank 2, Sensor 3)', 'P0063 HO2S Heater Control Circuit Low (Bank 2, Sensor 3)', 'P0064 HO2S Heater Control Circuit High (Bank 2, Sensor 3)', 'P0065 Air Assisted Injector Control Range/Performance', 'P0066 Air Assisted Injector Control Circuit or Circuit Low', 'P0067 Air Assisted Injector Control Circuit or Circuit High', 'P0068 MAP / MAF - Throttle Position Correlation', 'P0069 MAP - Barometric Pressure Correlation', 'P0070 Ambient Air Temperature Sensor Circuit', 'P0071 Ambient Air Temperature Sensor Range/Performance', 'P0072 Ambient Air Temperature Sensor Circuit Low Input', 'P0073 Ambient Air Temperature Sensor Circuit High Input', 'P0074 Ambient Air Temperature Sensor Circuit Intermittent/Erratic', 'P0075 Intake Valve Control Circuit (Bank 2)', 'P0076 Intake Valve Control Circuit Low (Bank 2)', 'P0077 Intake Valve Control Circuit High (Bank 2)', 'P0078 Exhaust Valve Control Circuit (Bank 2)', 'P0079 Exhaust Valve Control Circuit Low (Bank 2)', 'P0080 Exhaust Valve Control Circuit High (Bank 2)', 'P0081 Intake Valve Control Circuit (Bank 2)', 'P0082 Intake Valve Control Circuit Low (Bank 2)', 'P0083 Intake Valve Control Circuit High (Bank 2)', 'P0084 Exhaust Valve Control Circuit (Bank 2)', 'P0085 Exhaust Valve Control Circuit Low (Bank 2)', 'P0086 Exhaust Valve Control Circuit High (Bank 2)', 'P0087 Fuel Rail/System Pressure - Too Low', 'P0088 Fuel Rail/System Pressure - Too High', 'P0089 Fuel Pressure Regulator Performance', 'P0090 Fuel Pressure Regulator Control Circuit', 'P0091 Fuel Pressure Regulator Control Circuit Low', 'P0092 Fuel Pressure Regulator Control Circuit High', 'P0093 Fuel System Leak Detected - Large Leak', 'P0094 Fuel System Leak Detected - Small Leak', 'P0095 Intake Air Temperature Sensor 2 Circuit', 'P0096 Intake Air Temperature Sensor 2 Circuit Range/Performance', 'P0097 Intake Air Temperature Sensor 2 Circuit Low Input',
                  'P0098 Intake Air Temperature Sensor 2 Circuit High Input', 'P0099 Intake Air Temperature Sensor 2 Circuit Intermittent/Erratic', 'P00b7 Engine Coolant Flow Low/Performance', 'P0100 Mass or Volume Air flow Circuit Malfunction', 'P0101 Mass or Volume Air flow Circuit Range/Performance Problem', 'P0102 Mass or Volume Air Flow Circuit low Input', 'P0103 Mass or Volume Air flow Circuit High Input', 'P0104 Mass or Volume Air flow Circuit Intermittent', 'P0105 Manifold Absolute Pressure/Barometric Pressure Circuit Malfunction', 'P0106 Manifold Absolute Pressure/Barometric Pressure Circuit Range/Performance Problem', 'P0107 Manifold Absolute Pressure/Barometric Pressure Circuit Low Input', 'P0108 Manifold Absolute Pressure/Barometric Pressure Circuit High Input', 'P0109 Manifold Absolute Pressure/Barometric Pressure Circuit Intermittent', 'P0110 Intake Air Temperature Circuit Malfunction', 'P0111 Intake Air Temperature Circuit Range/Performance Problem', 'P0112 Intake Air Temperature Circuit Low Input', 'P0113 Intake Air Temperature Circuit High Input', 'P0114 Intake Air Temperature Circuit Intermittent', 'P0115 Engine Coolant Temperature Circuit Malfunction', 'P0116 Engine Coolant Temperature Circuit Range/Performance Problem', 'P0117 Engine Coolant Temperature Circuit Low Input', 'P0118 Engine Coolant Temperature Circuit High Input', 'P0119 Engine Coolant Temperature Circuit Intermittent', 'P0120 Throttle Pedal Position Sensor/Switch A Circuit Malfunction', 'P0121 Throttle/Pedal Position Sensor/Switch A Circuit Range/Performance Problem', 'P0122 Throttle/Pedal Position Sensor/Switch A Circuit Low Input', 'P0123 Throttle/Pedal Position Sensor/Switch A Circuit High Input', 'P0124 Throttle/Pedal Position Sensor/Switch A Circuit Intermittent', 'P0125 Insufficient Coolant Temperature for Closed Loop Fuel Control', 'P0126 Insufficient Coolant Temperature for Stable Operation', 'P0127 Intake Air Temperature Too High', 'P0128 Coolant Thermostat (Coolant Temp Below Thermostat Regulating Temperature)', 'P0129 Barometric Pressure Too Low', 'P0130 O2 Sensor Circuit Malfunction (Bank 1 Sensor 1)', 'P0131 O2 Sensor Circuit Low Voltage (Bank 1 Sensor 1)', 'P0132 O2 Sensor Circuit High Voltage (Bank 1 Sensor 1)', 'P0133 O2 Sensor Circuit Slow Response (Bank 1 Sensor 1)', 'P0134 O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 1)', 'P0135 O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)', 'P0136 O2 Sensor Circuit Malfunction (Bank 1 Sensor 2)', 'P0137 O2 Sensor Circuit Low Voltage (Bank 1 Sensor 2)', 'P0138 O2 Sensor Circuit High Voltage (Bank 1 Sensor 2)', 'P0139 O2 Sensor Circuit Slow Response (Bank 1 Sensor 2)', 'P0140 O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 2)', 'P0141 O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 2)', 'P0142 O2 Sensor Circuit Malfunction (Bank 1 Sensor 3)', 'P0143 O2 Sensor Circuit Low Voltage (Bank 1 Sensor 3)', 'P0144 O2 Sensor Circuit High Voltage (Bank 1 Sensor 3)', 'P0145 O2 Sensor Circuit Slow Response (Bank 1 Sensor 3)', 'P0146 O2 Sensor Circuit No Activity Detected (Bank 1 Sensor 3)', 'P0147 O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 3)', 'P0148 Fuel Delivery Error', 'P0149 Fuel Timing Error', 'P0150 O2 Sensor Circuit Malfunction (Bank 2 Sensor 1)', 'P0151 O2 Sensor Circuit Low Voltage (Bank 2 Sensor 1)', 'P0152 O2 Sensor Circuit High Voltage (Bank 2 Sensor 1)', 'P0153 O2 Sensor Circuit Slow Response (Bank 2 Sensor 1)', 'P0154 O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 1)', 'P0155 O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 1)', 'P0156 O2 Sensor Circuit Malfunction (Bank 2 Sensor 2)', 'P0157 O2 Sensor Circuit Low Voltage (Bank 2 Sensor 2)', 'P0158 O2 Sensor Circuit High Voltage (Bank 2 Sensor 2)', 'P0159 O2 Sensor Circuit Slow Response (Bank 2 Sensor 2)', 'P0160 O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 2)', 'P0161 O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 2)', 'P0162 O2 Sensor Circuit Malfunction (Bank 2 Sensor 3)', 'P0163 O2 Sensor Circuit Low Voltage (Bank 2 Sensor 3)', 'P0164 O2 Sensor Circuit High Voltage (Bank 2 Sensor 3)', 'P0165 O2 Sensor Circuit Slow Response (Bank 2 Sensor 3)', 'P0166 O2 Sensor Circuit No Activity Detected (Bank 2 Sensor 3)', 'P0167 O2 Sensor Heater Circuit Malfunction (Bank 2 Sensor 3)', 'P0168 Engine Fuel Temperature Too High', 'P0169 Incorrect Fuel Composition', 'P0170 Fuel Trim Malfunction (Bank 1)', 'P0171 System Too Lean (Bank 1)', 'P0172 System Too Rich (Bank 1)', 'P0173 Fuel Trim Malfunction (Bank 2)', 'P0174 System Too Lean (Bank 2)', 'P0175 System Too Rich (Bank 2)', 'P0176 Fuel Composition Sensor Circuit Malfunction', 'P0177 Fuel Composition Sensor Circuit Range/Performance', 'P0178 Fuel Composition Sensor Circuit Low Input', 'P0179 Fuel Composition Sensor Circuit High Input', 'P018C Fuel Pressure Sensor B Circuit Low', 'P0180 Fuel Temperature Sensor A Circuit Malfunction', 'P0181 Fuel Temperature Sensor A Circuit Range/Performance', 'P0182 Fuel Temperature Sensor A Circuit low Input', 'P0183 Fuel Temperature Sensor A Circuit Intermittent', 'P0184 Fuel Temperature Sensor A Circuit Intermittent', 'P0185 Fuel Temperature Sensor B Circuit Malfunction', 'P0186 Fuel Temperature Sensor B Circuit Range/Performance', 'P0187 Fuel Temperature Sensor B Circuit Low Input', 'P0188 Fuel Temperature Sensor B Circuit High Input', 'P0189 Fuel Temperature Sensor B Circuit Intermittent', 'P0190 Fuel Rail Pressure Sensor Circuit Malfunction', 'P0191 Fuel Rail Pressure Sensor Circuit Range/Performance', 'P0192 Fuel Rail Pressure Sensor Circuit Low Input', 'P0193 Fuel Rail Pressure Sensor Circuit High Input', 'P0194 Fuel Rail Pressure Sensor Circuit Intermittent', 'P0195 Engine Oil Temperature Sensor Malfunction', 'P0196 Engine Oil Temperature Sensor Range/Performance', 'P0197 Engine Oil Temperature Sensor Low', 'P0198 Engine Oil Temperature Sensor High', 'P0199 Engine Oil Temperature Sensor Intermittent']
def topN(list1, N):
    final_list = []
    for i in range(0, N):
        max1 = 0
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
        list1.remove(max1)
        final_list.append(max1)
    return final_list

def searchKeywords(userWords):
    #wordList = userWords.split(",")
    for x in range(len(array0000_0199)):
        ratioArray = []
        for y in range(len(array0000_0199)):
            ratio = similar(userWords, array0000_0199[y])
            rounded = round(ratio,2)
            ratioArray.append(rounded)
   
    top3ratios = heapq.nlargest(3, ratioArray)
    largestPosition = ratioArray.index(top3ratios[0])
    secondPosition = ratioArray.index(top3ratios[1])
    thirdPosition = ratioArray.index(top3ratios[2])
    #largestRatio = max(ratioArray)
    #ratioPosition = ratioArray.index(largestRatio)
    #print(largestRatio)
    #print(ratioArray.index(largestRatio))
    print("Here is the top 3 closest issues to your description:\n")
    print(top3ratios[0]*100, "% -", array0000_0199[largestPosition], "\n")
    print(top3ratios[1]*100, "% -", array0000_0199[secondPosition], "\n")
    print(top3ratios[2]*100, "% -", array0000_0199[thirdPosition])
    #print(ratioPosition)
            #if ((similar(userWords,array0000_0199[y])) >= 0.50):
            #    print(array0000_0199[y])
            #else:
            #    print("these keywords do not match.")


#print(array0000_0199[98])
#print(similar(userWords, array0000_0199))
#createArray(troubleCodes)

generic = "0 indicates that the code is generic, standardized SAE (Society of Automotive Engineers) code. Generic codes are adopted by all cars that follow the OBD-II standard."
dealerSpecific = "1 indicates that the code is vehicle manufacturer-specific.These codes are unique to a specific car make or model and are typically less common."

ss_one = "1: refers to the fuel or air metering system\n"
ss_two = "2: refers to the fuel or air metering injection system\n"
ss_three = "3: refers to the ignition system\n"
ss_four = "4: refers to the emissions system\n"
ss_five = "5: refers to the vehicle speed controls and idle control system\n"
ss_six = "6: refers to the computer output circuit\n"
ss_seven = "7: indicate that the issue is transmission-related\n"
ss_eight = "8: indicate that the issue is transmission-related\n"
ss_nine = "9: indicate that the issue is transmission-related\n"

formCode = ""

print("\n------------------------------------------------ Diagnosis Porgram ------------------------------------------------\n")
controlSystem = input("Which Control System Is at Fault? \n\nP(powertrain)\nC(chassis)\nB(body)\nU(network)\n\nAnswer: ")
formCode = formCode + controlSystem
match controlSystem:
    case "P":
        print("\n-------------------------------------------------------------------------------------------------------------------\n")
        print("Which Type of Code Is at Fault? \n\n0(",generic,")\n1(",dealerSpecific,")\n")
        codeType = input("Answer: ")
        formCode = formCode + codeType
        match codeType:
            case "0":
                print("\n-------------------------------------------------------------------------------------------------------------------\n")
                print("Which subsystem is at fault?\n", ss_one, ss_two, ss_three, ss_four, ss_five, ss_six, ss_seven, ss_eight, ss_nine)
                subSystem = input("Answer: ")
                formCode = formCode + subSystem
                print(formCode)
                match subSystem:
                    case "1":
                        print("\n-------------------------------------------------------------------------------------------------------------------\n")
                        print("To get the most accurate results, please insure the following:\n")
                        print("- Include atleast 5 keywords.\n")
                        print("- Seperate by space.\n")
                        faultDescription = input("Try to describe your issue with atleast 4 keywords:\n")
                        print("-------------------------------------------------------------------------------------------------------------------")
                        print("-------------------------------------------------------------------------------------------------------------------")
                        searchKeywords(faultDescription)
                        print("-------------------------------------------------------------------------------------------------------------------")
                        print("-------------------------------------------------------------------------------------------------------------------")
                    case "2":
                        print("")
                    case "3":
                        print("")
                    case "4":
                        print("")
                    case "5":
                        print("")
                    case "6":
                        print("")
                    case "7":
                        print("")
                    case "8":
                        print("")
                    case "9":
                        print("")
                    case _:
                        print("Please choose one of the options given")
            case "1":
                print("u chose 1")
            case _:
                print("please choose either 0 or 1.")
    case "C":
        print("u chose C")
    case "B":
        print("u chose B")
    case "U":
        print("u chose U")
    case _:
        print("please choose from the dropdown menu")
