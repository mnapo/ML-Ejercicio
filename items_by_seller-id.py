##################################

# Script que crea un archivo log de los ítems publicados para los seller_id indicados
# Versión en Python 3.7.4
# Última modificación 16/09/19
# ATENCIÓN: FALTA TESTEAR Y DEBUGUEAR


# se importa la librería requests
import requests

# se inicializan variables
url_api = "https://api.mercadolibre.com"
url_api_MLA_seller_id = url_api + "/sites/MLA/search?seller_id="
url_api_items = url_api + "/items?ids="

seller_id = "81644614"
log_content = ""
delimiter = ","

##################################


# se obtienen los items del seller_id=81644614
seller_req = requests.get( url_api_MLA_seller_id + seller_id )

# se deserializa la estructura JSON a diccionario
req_json = req.json()

# se obtiene la lista de IDs de los ítems publicados por el vendedor
results = req_json[ "results" ]

# se convierte la lista a cadena separada por comas, para pasar mediante GET a la API
items_list = delimiter.join( results )

# se obtiene la info de cada ítem publicado
items_req = requests.get( url_api_items + items_list )


# se parsea la lista de IDs de ítems como cadena 
# items_list = json.dumps( json.loads( results ), indent = 4 )