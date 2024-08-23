# É fundamental para definir a estrutura dos dados da aplicação. É onde define os modelos, que são represeentações das tabelas no banco de dados. É similar a classe @Entity no Spring Boot.

# bibliteca de modelos do django
from django.db import models

# Importa sinais e decorados de recepção do django
from django.db.models.signals import post_save
from django.dispatch import receiver


# Define o modelo genre
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Song(models.Model):

    # Define uma lista de opções para o campo.
    GENRE_CHOICES = [
        ("rock", "Rock"),
        ("pop", "Pop"),
        ("jazz", "jazz"),
        ("electronic", "Electronic"),
        ("hip hop", "Hip Hop"),
        ("funk", "Funk"),
        ("country", "Country"),
        ("classical", "Classical"),
    ]
    genre = models.CharField(
        max_length=50, choices=GENRE_CHOICES, blank=True, null=True
    )

    # ManyToMany para uma musica ter multiplos generos.
    genres = models.ManyToManyField("Genre")

    title = models.CharField(
        max_length=100
    )  # Campo para o titulo da musica, e assim por diante.
    artist = models.CharField(max_length=100, blank=True)
    album = models.CharField(max_length=100, blank=True)
    release_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    url = models.URLField(max_length=200, blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    # Método que retorna a representação em string da musica
    def __str__(self):
        return f"{self.title} by {self.artist}"

    # Método de classe para obter musicas destacadas
    @classmethod  # Decorador usado para definir métodos que pode ser chamado na propria classe, sem precisar de uma instancia. Ele recebem a clase ('cls') como o primeiro arugmento em vez de uma instancia de classe ('self'). cls representa a classe Song
    def get_featured_songs(cls):
        return cls.objects.filter(is_featured=True)

    # Métodos personalizado para manipular ou exibir dados de maneira especifica.
    def is_old_song(self):
        return self.release_date.year < 200

    def is_popular(self):
        return self.play_count > 1000


# Sinais do django permitem executar ações em resposta a eventos, como criação, atualização ou exclusão de um objeto
@receiver(
    post_save, sender=Song
)  # post_save é o sinal enviado apos um modelo ser salvo, receiver conecta a função 'update-play_count' ao sinal 'pos_save' par ao modelo 'Song'
def update_play_count(
    sender, instance, **kwargs
):  # Chamada toda vez que um 'Song' é salvo
    if instance.play_count > 1000:
        instance.is_featured = True
        instance.save()


"""
Char/Data/BoolearnField: Usado para campos de texto com comprimento limiteado, para armazenar datas, para valores boolearnos

Método __str__: Define a representação em string do modelo, que é util para exibir instancias de modelo em interfaces administrativas e outros lugares.

Considerações

Estrutura do Banco de Dados: Cada modelo deifne uma tabela no banco de dados. As isntancias dos modelos são registros nesa tabelas.

Validação: Os campos dos modelos podem incluir validação, como o comprimento máximo dos campos de texto e a obrigatoriedade de campos.

Relacionamentos: MOdelos podem ser relacionar ocm outros modelos, permitindo criar aplicativos mais complexos e interconectados.

"""
