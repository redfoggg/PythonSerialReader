#!/usr/bin/python2.7
import time;
import serial;
import DbContext;
import DadosParaPlotarModel as model



viagens = 0;

ser = serial.Serial('/dev/ttyUSB0', 9600);

moda_coord = 0
moda_router = 0;
range_coord = False
range_router = False



def range_ponto_fixo():
    global range_coord
    global range_router
    if moda_coord >= 30 and moda_coord <= 40:
        print 'entrou range Coord'
        range_coord = True
    else:
        range_coord = False
    if moda_router >= 45 and moda_router <= 55:
        print 'entrou range router'
        range_router = True
    else:
        range_router = False

def ponto_de_carga():
    global viagens
    print 'range router: ' + str(range_router) + ' range coord: ' + str(range_coord)
    if  range_router and range_coord:
        viagens += 1;
        print 'viagens = ' + str(viagens)
        while range_router and range_coord:
            print 'Esta na posicao'
            break

    return;

time.sleep(1.8)
while 1==1:
    VALUE_SERIAL = ser.readline();

    
    
    if "RSSI END/COORD (-dBm) = " in VALUE_SERIAL:
        moda_coord = float(VALUE_SERIAL[24:].strip())
        print "valor de moda_coord = " + str(moda_coord)
    
    if "RSSI ROUTER/COORD (-dBm) = " in VALUE_SERIAL :
        moda_router = float(VALUE_SERIAL[27:].strip())
        print "valor de moda_router = " + str(moda_router)

    if (moda_coord != 0) and (moda_router != 0):
        print 'verificando range e ponto de carga'
        range_ponto_fixo()
        ponto_de_carga()
        moda_coord = 0
        moda_router = 0
        


    print VALUE_SERIAL





ser.close();
