# Utilizado é utlizado para configurar o aplicativo dentro do projeto. Ele define, personaliza, registra e integra o aplicativo

from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class RecsoundingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "recsounding"
    verbose_name = "Recommending Sounds"

    # Customização da inicialização sobreescrevendo o método ready() da classe AppConfig.
    def ready(self):
        # Configuração de sinais, uteis quando se deseja executar codigo em resposta a certoos eventos, como a criação, atualização ou exclusão de uma instancia de modelo.
        try:
            import recommender.signals
        except ImportError:
            logger.warning("Não foi possivle importar recommender.singals")

        # Customização da inicialização
        logger.info("Recsounding app is initialized.")

        # Configuração d eaplicativos Externos
        try:
            from .external_services import initialize_service
        except ImportError:
            logger.warning("Não foi possível importar initialize_service")

        # Confiuração de tarefas agendadas
        try:
            import recommender.tasks
        except ImportError:
            logger.warning("Não foi possivel importar recommender.tasks")

        # Configurar dados iniciais
        try:
            from .initial_data import load_initial_data

            load_initial_data()
        except:
            logger.warning("Não foi possivel importar recommender.initial_data")

        # Inicialização de dados de teste
        try:
            from . import initial_data

            initial_data.load()
        except ImportError:
            logger.warning("Não foi possível importar initial_data")

        # Inicializar variaveis globais ou Configuraões
        global FEATURED_SONGS
        FEATURED_SONGS = []

        # Configuração de URLS ou Views
        from django.conf import settings

        settings.ROOT_URLCONF = "recommender.urls"

        # Mensagens de log
        logger.info("Recsounding app is ready")
