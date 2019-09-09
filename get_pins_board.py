##Docs: https://docs.python-guide.org/scenarios/scrape/
#http://docs.python-requests.org/en/master/api/#requests.Response
#https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
##https://developers.pinterest.com/docs/api/overview/?
#
#

from lxml import html
import requests
import json

#page = requests.get('https://pin.it/is4tpcdtcmvtvi')
requests.get('https://api.pinterest.com/v1/')
print(page.text)
#tree = html.fromstring(page.content)
#json_pins = tree.xpath('//script[@id="initial-state"]/text()')
#pins = json.loads(json_pins[0])
#pathname = pins["location"]["pathname"].split('/') # "/pin/459085755761840151/sent/?sfo=1&sender=259660872174066757&invite_code=4155b0f3858748c3abc79ab707d87c93"
#id_pin = pathname[2]
#print(pins["pins"][id_pin]['images']['orig'])



## https://developers.pinterest.com/tools/api-explorer/?

'''
GET/v1/boards/<board_spec:board>/pins/
Description: Retrieve the Pins on a Board
'''

access_token = 'Ao-JPEsUPqZ3uRL7Q7IO7Yl1x2cDFYuZkJRLJDVFsJuc9iC7RQOagDAAANxFRbCgFc9guKYAAAAA'
id_board = 259660803454824929
base_url = 'https://api.pinterest.com/v1/boards/'+id_board+'/pins/?access_token='+access_token

#También puede usar el fieldsparámetro para expandir los recursos anidados. Los atributos múltiples se agrupan en paréntesis y se separan por comas.
#fields=id,link,creator(id,first_name,last_name),board(id,name)
fields = '&fields=id,board,image,original_link,link' #quizas sea necesario reemplazar la ',' por '%2C'
limit = '&limit=1' #Maximo de 100. Default 25

request_url = base_url + fields + limit

#Paginacion:
#Al final de cada respuesta de búsqueda hay un valor cursor y nextPase. Envíe el valor cursor en su próxima solicitud para recibir los siguientes 25 elementos de la lista. 
#Para obtener una forma más fácil de obtener la página siguiente, use la nextURL que se proporciona al final de la respuesta. La nextURL no caduca.

'''
GET/v1/boards/<board_spec:board>/
Description: Retrieve information about a Board
'''


