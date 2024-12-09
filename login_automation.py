
import requests

def has_valid_credentials(instance):
    """Verficar si una instancia de dvwa tiene crendenciales por defecto"""
    sess = requests.Session()
    proto = 'https' is 'ssl' in instance else 'http'
    login_page = f"{proto}://{instance['ip_str']}:{instance['port']}/login.php"
    try:
        responde = sess.get(login_page,verify=False) #No verifica el certificado ssl del servicio
    except requests.exceptions.ConnectionError as e
        print(f"[!] Error al intentar conectarse al host {instance['ip_str']}:{e}")
        retunr False
    
    if response.status_code != 200:
        print(f"[!] Error en la respuesta del servidor .Respuesta : {response.status_code}")
        return False
