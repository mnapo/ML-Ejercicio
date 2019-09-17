##################################

'''
Script que crea un archivo log de los ítems publicados para los seller_id indicados
Versión en Pseudocódigo
'''

# se importa la librería requests
import requests

# se inicializan variables
url_api = "https://api.mercadolibre.com"
url_api_MLA_seller_id = url_api + "/sites/MLA/search?seller_id="
url_api_items = url_api + "/items?ids="

seller_id = "81644614"
delimiter = ","

log_content
log_file

##################################


# obtener ítems del seller_id=81644614
seller_req = requests.get( url_api_MLA_seller_id + seller_id )

# deserializar la estructura JSON a diccionario
seller_req_json = seller_req.json()

# obtener la lista de IDs de los ítems publicados por el vendedor
seller_results = req_json["results"]

# convertir la lista a cadena separada por comas, para pasar mediante GET a la API
items_list = delimiter.join( results )

# obtener la info de cada ítem publicado
items_req = requests.get( url_api_items + items_list )

# deserializar la estructura JSON a diccionario
items_req_json = items_req.json()

# recorrer ítems para generar log_content
for id in items_req_json:
	content_item_title = items_req_json[id]["title"]
	content_category_id = items_req_json[id]["category_id"]
	content_category_name = items_req_json[id]["category_name"]
	content = "ITEM " + id + ": " + content_item_title + content_category_id + content_category_name + "\n"
	log_content = content + "PUBLICACIONES DE SELLER_ID: " + seller_id + content

# crear archivo log
log_file = open("items-info.log","w+")
log_file.write(log_content)
log_file.close()
