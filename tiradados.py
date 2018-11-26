# -*- coding: utf-8 -*-
import requests
import json
import time

def get_estados():
	r = requests.get('http://repasse.icmc.usp.br/rest/estado')
	return r.json()
	
    

def get_municipios(estado):
	r = requests.get('http://repasse.icmc.usp.br/rest/estado/'+estado+'/municipios')
	return r.json()
	
    
    
def municipio_valor(estado,municipio,ano,mes):
	r = requests.get('http://repasse.icmc.usp.br/rest/agregacao/AREA/area/10/'+str(ano)+'/'+str(mes)+'/municipio/'+str(municipio))
	return sum(r.json()['dadosAgregados'].values())
	
	
def pega(estado, ano, municipios):
    for mes in range(1,12):
            total = 0
            i=0
            for municipio in municipios :
                try:
                    i = i+1
                    print(str(i)+'/'+str(len(municipios))+ " mes: "+str(mes)+ "ano: "+str(ano), end="\r", flush=True)
                    total+= municipio_valor(estado,municipio['id'],ano,mes)
                except json.decoder.JSONDecodeError:
                    i = i+1
                    pass

                
    return total	
    
estados = ['PR','SP']
		
for estado in estados:
	print(estado)
	municipios = get_municipios(estado)
	for ano in range(2017,2018):
		print(pega(estado,ano,municipios))

    
 

 


