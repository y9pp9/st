#!/bin/python
import serial

SIGNAL = {'liv1lighton' : 'F70E114103020100A906F70E11C1060000010000002E0C',
          'liv1lightoff' : 'F70E114103020000A804F70E11C1060000000000002F0C',
          'liv2lighton' : 'F70E114103010100AA06',
          'liv2lightoff' : 'F70E114103010000AB06',
          'livthermoon' : 'F73511450100971A',
          'livthermooff' : 'F73511450101961A',
          'room1thermoon' : 'F735124501009418',
          'room1thermooff' : 'F73512450101951A',
          'room2thermoon' : 'F73513450100951A',
          'room2thermooff' : 'F73513450101941A',
          'room3thermoon' : 'F735144501009218',
          'room3thermooff' : 'F73514450101931A',
          'totthermoon' : 'F735FF45010079EA',
          'totthermooff' : 'F735FF45010178EA'
          }

def sendRs485(name, typ, mode):
    ser = serial.Serial(
     port='/dev/ttyUSB0',
     baudrate=9600,
     )
    key = name + typ + mode
    data = SIGNAL.get(key)
    data_byte = bytearray.fromhex(data)
    #print(data_byte)
    ser.write(data_byte)
    ser.close()

if __name__ == "__main__":
        sendRs485('liv1', 'light', 'on')
