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
url_api_ctgs = url_api + "/categories?id="

seller_id = [ "81644614", "183952086", "70384506", "93829058" ]

delimiter = ","

items_offset = 50000

new_line = "\n"
separator
log_content
log_file

##################################

# recorrer lista de vendedores
for uid in seller_id:

    if uid==2:
        separator = new_line + "----------------------------" + new_line
    elif uid==len(seller_id):
        separator = ""

    # obtener ítems del seller_id
    seller_req = requests.get( url_api_MLA_seller_id + uid )

    # deserializar la estructura JSON a diccionario
    seller_req_json = seller_req.json()

    # obtener la lista de IDs de los ítems publicados por el vendedor
    seller_results = req_json[ "results" ]
    
    #acotamos al offset
    seller_results_len = len( seller_results )
    if ( seller_results_len > items_offset ):
        for res_id in range ( seller_results_len, items_offset, -1):
            seller_results.pop()
            #print( "se dejó afuera el item " + res_id )

    # convertir la lista a cadena separada por comas, para pasar mediante GET a la API
    items_list = delimiter.join( results )

    # obtener la info de cada ítem publicado
    items_req = requests.get( url_api_items + items_list )

    # deserializar la estructura JSON a diccionario
    items_req_json = items_req.json()

    # recorrer ítems para generar log_content
    for iid in items_req_json:
        content_item_title = items_req_json[ iid ][ "title" ]
        content_ctg_id = items_req_json[ iid ][ "category_id" ]
        content_ctg_req = requests.get( url_api_ctgs + content_ctg_id )
        content_ctg_req_json = seller_req.json()
        content_ctg_name = content_ctg_req_json[ "name" ]
        content = " ITEM " + iid + ": " + content_item_title + " -- " + content_ctg_id + " -- " + content_ctg_name
        log_content = log_content + separator + content + "PUBLICACIONES DE SELLER_ID: " + uid + content

# crear archivo log
log_file = open( "items-info.log","w+" )
log_file.write( log_content )
log_file.close()
