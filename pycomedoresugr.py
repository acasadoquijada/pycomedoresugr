from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime as date

import re
import json
import locale
import codecs


def get_menu_semana(url="http://scu.ugr.es/"):

    if url=="http://scu.ugr.es/":
        page = urlopen(url)
        soup = BeautifulSoup(page,"html.parser")

    else:
        f = codecs.open(url, 'r', 'utf-8')
        soup = BeautifulSoup(f,"html.parser")
        f.close()


    table = soup.find_all('table')[0]

    menu_semana = []

    for row in table.find_all("tr"):
        col = row.find_all("td")
        elem = col[0].getText().replace('\n',' ').replace("  "," ")
        menu_semana.append(elem)

    return menu_semana
    
def menu_semana_diccionario(url="http://scu.ugr.es/"):

    ms = get_menu_semana(url)
    
    d = {}
    dias = ['LUNES','MARTES','MIÉRCOLES','JUEVES','VIERNES','SÁBADO']
    
    for i in range(len(ms)):
        
        splitted = ms[i].split()

        dia = splitted[0]
        
        if dia in dias:
           
           #Mejorar esto
           var_cerrado = re.sub(' ', '',ms[i+1])
           
           if var_cerrado != "CERRADO": 
            d[dia] = [ms[i],ms[i+1], ms[i+2], ms[i+3]]
            i +=4 #Para evitar loops innecesarios
           
           else:
            d[dia] = [ms[i],ms[i+1]]
            i +=2 #Para evitar loops innecesarios
            
    return d

def menu_semana_json(url="http://scu.ugr.es/"):

    menu = menu_semana_diccionario(url)

    menu_json = json.dumps(menu,ensure_ascii=False)
    
    return menu_json

def menu_dia(dia="",url="http://scu.ugr.es/"):
    
    if dia == "":
        locale.setlocale(locale.LC_ALL, 'es_ES.utf8')
        dia = date.today().strftime("%A")
  
    dia = dia.upper()
    
    dias = ['LUNES','MARTES','MIÉRCOLES','JUEVES','VIERNES','SÁBADO']
    
    if dia in dias:
    
        menu_semana = menu_semana_diccionario(url)
    
        return menu_semana[dia]
        
    else:
        
        return ""
    
   
