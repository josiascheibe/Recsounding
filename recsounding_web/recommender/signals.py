import logging
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver, Signal
from .models import Song

# Configuração do logger para registrar informações e eventos
logger = logging.getLogger(__name__)

# Sinal customizado
song_played = Signal(providing_args=["instance", "user"])


# Receptor do sinal customizado
@receiver(song_played)
def handle_song_played(sender, instance, user, **kwargs):
    logger.info(
        f"Song played: {instance.title} by {instance.artist}, played by {user.username}"
    )


# Conecta os sinais usando o decorador receiver
@receiver(pre_save, sender=Song)
def before_song_save(sender, instance, **kwargs):
    logger.info(f"Before saving song: {instance.title} by {instance.artist}")


@receiver(post_save, sender=Song)
# sender é o modelo que enfia o sinal. Aqui no caso esta usando o post_save
def after_song_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New song created: {instance.title} by {instance.artist}")
    else:
        logger.info(f"Song updated: {instance.title} by {instance.artist}")


@receiver(post_delete, sender=Song)
# Instance é a instancia especifica do modelo que esta sendo salva ou deletada.
def after_song_delete(sender, instance, **kwargs):
    logger.info(f"Song deleted: {instance.title} by {instance.artist}")


@receiver(post_save, sender=Song)
# Created é um booleano que indica se a instancia do modelo foi criada ou atualizada, especifico para o sinal post_save
def update_featured_status(sender, instance, created, **kwargs):
    if created:
        if instance.play_count > 1000:
            instance.is_featured = True
        elif instance.play_count > 500:
            instance.is_featured = False  # Some other condition
        instance.save()

"""
kwargs é um dicionario que captura quaisquer argmentos nomeados aicioais que foram passados para o sinal. isso permite que a funçao receptor aceite um numero variavel de argumentos sem precisar lsitar todos explicitamente.
"""