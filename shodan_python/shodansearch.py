import  shodan 

class ShordanSearch:
    def  __init__(self, api_key):
        self.client = shodan.Shodan(api_key)

    def search (self, query, page=1):
        ''' Realiza una consulta en Shodan y devueleve una pagina de resultados '''
        try:
            resultados =  self.client.search(query, page=page)
            return resultados
        except Exception as e:
            print("El error al realizar la peticion a Shodan : ", e)


