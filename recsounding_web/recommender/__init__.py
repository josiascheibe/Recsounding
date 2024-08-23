# Componente essencial em um projeto Python. Serve para marcar um diretório como um pacote Python, permitindo que os módulos dentro desse diretório sejam importados.


# Um __init__.py vazio é perfeitamente valido mas se pode usar coisas para importar submódulos automaticamente quando o pacote é importado
from .models import Song, Genre
from .views import index, recommend

# controle de importação, para definir quais submodelos devem ser importados quando usar o from package import
__all__ = ["models", "views"]


# Inicialização de pacotes complexos
def initialize_package():
    print("Inicializando pacote recommender...")


initialize_package()


"""
Importação condicional: importa modulos ou define veriaveis apenas sob certas condições:

if os.getenv('DJANGO_ENV') == 'development':
    from .dev_settings import *
else:
    from .prod_settings import *

"""
