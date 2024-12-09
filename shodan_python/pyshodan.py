from shodansearch import ShordanSearch
from dotenv import load_dotenv 
import os

def main():
    load_dotenv()
    SHODAN_API_KEY =  os.getenv("SHODAN_API_KEY")
    print("esta es la clave",SHODAN_API_KEY)
    ssearch  = ShordanSearch(SHODAN_API_KEY)
    resultados = ssearch.search("title:dvwa",page=1)
    for i in range(10):
        print(f"\n Resultado {i}")
        print(f"Dirrecion IP:{resultados["matches"][i]["ip_str"]}")
        print(f"Dirrecion IP:{resultados["matches"][i]["hostnames"]}")
        print(f"Localizacion: {resultados["matches"][i]["location"]}")


if __name__=="__main__":
    main()