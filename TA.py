import os
import time
import MySQLdb
import serial

ser=serial.Serial('dev/ttyUSB0',9600)
n=0

while 1:
    lines=ser.readline()
    print ("%s"%(lines))
    hum,temp,direct,speed=lines.split(",")
    print ("H=%s T=%s Arah=%s Kecepatan=%s"%(hum,temp,direct,speed))

    db = MySQLdb.connect(host="sql143.main-hosting.eu",   # your host, usually localhost
                     user="u745172280_byan",         # your username
                     passwd="21byan21",  # your password
                     db="u745172280_ta")        # name of the data base
    cur = db.cursor()
    try:

        cur.execute("INSERT INTO cuaca_tb (suhu, hum, arah, kecepatan, date, time) VALUES (%s,%s,%s,%s,%s,%s)",(temp, hum, direct, speed, time.strftime("%x"), time.strftime("%H:%M:%S"))
        db.commit()
        print ("sukses")

    except:
        db.rollback()
    db.close()
    time.sleep(2)
