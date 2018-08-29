import os
import cv2
import sys
import math
import time
import json
import numpy as np
from ownLibraries.pathsandnames import PathsAndNames

def convertirAJSON(lista = None,file = 'datos'):
	if lista == None:
		lista = np.load(PathsAndNames.folderDeInstalacion+'/'+file+'.npy')
	
	diccionarioAJson = {'Carretera':lista[0]
								            }

	with open(jsonToWrite, 'w') as file:
		json.dump(diccionarioAJson, file)
	print('Archivo guardado como json exitosamente')

directorioDeVideos = PathsAndNames.directorioDeVideos+'/'
fileToWrite = PathsAndNames.folderDeInstalacion+'/datos.npy'
jsonToWrite = PathsAndNames.folderDeInstalacion+'/datos.json'

parser = argparse.ArgumentParser(description='Add newData')
parser.add_argument('-l', '--newLocation', default = None, type=str, help="Add new subfolder")
parser.add_argument('-s', '--source', default = None, type=str, help="Add input for debug")
parser.add_argument('-c', '--convertir', default = None, type=str, help="justConvertFile")
args = parser.parse_args()

if args.newLocation != None:
	nuevaLocalizacion = args.newLocation
	with open(PathsAndNames.archivoDeInstalacion, 'w') as file:
		file.write(nuevaLocalizacion)

if args.source != None:
	nameSourceVideo = args.source
	fileToWrite = fileToWrite[:-9]+nameSourceVideo[:-3]+'npy'
	jsonToWrite = jsonToWrite[:-10]+nameSourceVideo[:-3]+'json'
	archivo = args.source
else:
	nameSourceVideo = 0
	archivo = 'datos.mp4'

if args.convertir != None:
	convertirAJSON(file = archivo[:-4])
	__name__ = 'none'

listaCoordenadas=[]
listaA=[]
listaB=[]
listaC=[]
listaD=[]
lista=[]
##################################################################################################################
####Drawing the lines####
# mouse callback function
def Carretera_LineaA(event,x,y,flags,param):
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        listaA.append((x,y))
		if len(listaA)!= 0:
			cv2.line(frame, (x,y),2,(0,255,0),-1)
			cv2.imshow('Zona_Carretera',frame)
		if len(listaA)== 2:
			frame=cv2.line(frame,listaA[0],listaA[1],(0,0,255),3)
			cv2.imshow('Zona_Carretera',frame)
#############################################################################
def Carretera_LineaB(event,x,y,flags,param):
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        listaB.append((x,y))
		if len(listaB)!= 0:
			cv2.line(frame, (x,y),2,(0,255,0),-1)
			cv2.imshow('Zona_Carretera',frame)
		if len(listaB)== 2:
			frame=cv2.line(frame,listaB[0],listaB[1],(0,0,255),3)
			cv2.imshow('Zona_Carretera',frame)

#############################################################################
def Carretera_LineaC(event,x,y,flags,param):
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        listaC.append((x,y))
		if len(listaC)!= 0:
			cv2.line(frame, (x,y),2,(0,255,0),-1)
			cv2.imshow('Zona_Carretera',frame)
		if len(listaC)== 2:
			frame=cv2.line(frame,listaC[0],listaC[1],(0,0,255),3)
			cv2.imshow('Zona_Carretera',frame)

#############################################################################
def Carretera_LineaD(event,x,y,flags,param):
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        listaD.append((x,y))
		if len(listaD)!= 0:
			cv2.line(frame, (x,y),2,(0,255,0),-1)
			cv2.imshow('Zona_Carretera',frame)
		if len(listaD)== 2:
			frame=cv2.line(frame,listaD[0],listaD[1],(0,0,255),3)
			cv2.imshow('Zona_Carretera',frame)

##################################################################################################################
##############################Get the intersections####################################################
def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
################################################################################################################


L1 = obtenercoordernadas(np.array(listaA))
L2 = obtenercoordernadas(np.array(listaB))
L3 = obtenercoordernadas(np.array(listaC))
L4 = obtenercoordernadas(np.array(listaD))

R1 = intersection(L1, L3)
R2 = intersection(L1, L4)
R3 = intersection(L2, L3)
R4 = intersection(L2, L4)

listaCoordenadas=[R1,R2,R3,R4]
lista.append((listaCoordenadas))

convertirAJSON(lista)

cv2.destroyAllWindows()
