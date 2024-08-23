# É um arquivo que você pode usar para configurar e inicializar serviços externos que sua aplicação pode precisar utilizar.

import logging
import os
import requests

logger = logging.getLogger(__name__)


#Classe para fazer requisicições a uma API externa
class ExternalAPIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_data(self, endpoint, params=None):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(
            f"{self.base_url}/{endpoint}", headers=headers, params=params
        )
        response.raise_for_status()
        return response.json()


# Inicializa e retorna um cliente de API configurado 
def initialize_api_client():
    api_key = os.getenv("EXTERNAL_API_KEY")
    base_url = "http://api.example.com"

    if not api_key:
        logger.error("API Key não está definida")
        return None

    return ExternalAPIClient(api_key, base_url)


# Configura e retorna um serviço de autenticação
def initialize_auth_service():
    # Exemplo de configuração de um serviço de autenticação
    client_id = os.getenv("AUTH_CLIENT_ID")
    client_secret = os.getenv("AUTH_CLIENT_SECRET")

    if not client_id or not client_secret:
        logger.error("As credenciais de autenticação não estão definidas")
        return None

    return {
        "client_id": client_id,
        "client_secret": client_secret,
        "auth_url": "https://auth.example.com/oauth/token",
    }


# Inicializa toos os serviços e os retorna em um dicionario
def initialize_services():
    api_client = initialize_api_client()
    auth_service = initialize_auth_service()

    return {"api_client": api_client, "auth_service": auth_service}


services = initialize_services()

# Obetnedo dados de um endpoint
if services["api_client"]:
    try:
        data = services["api_client"].get_data("some-endpoint")
        logger.info(f"Dados recebidos: {data}")
    except requests.HTTPError as e:
        logger.error(f"Erro ao obter dados da API: {e}")
