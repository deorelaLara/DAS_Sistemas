import requests
import pprint
import ramapi
from ramapi import *
import ClaseCharacter
import BDCharacter


#r = requests.get('https://rickandmortyapi.com/api/character/?page=')

ramapi.Base.api_info()
ramapi.Base.schema()


for n in range(1,26):
    
    
    cosa = ramapi.Character.get_page(n)
    #pprint.pprint(cosa)

    for personaje in cosa['results']:

        item = ClaseCharacter.Personaje(id = personaje['id'],name = personaje['name'],status = personaje['status'],species = personaje['species'], ttype = personaje['type'], gender = personaje['gender'], originName = personaje['origin']['name'], orginUrl = personaje['origin']['url'], locationName = personaje['location']['name'], locationUrl = personaje['location']['url'], image = personaje['image'], episode = personaje['episode'], url = personaje['url'], created = personaje['created'])
        print("-------------Inicio de Personaje--------------\n")
        #print(item)
        BDCharacter.insertarP(item)
        
        print("-------------Final de Personaje--------------\n")
        
#pprint.pprint(cosa)    
    
BDCharacter.VisualizarPersonaje()

