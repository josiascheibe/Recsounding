# É usado para registrar e personalizar/comportamento dos modelos do seu aplicativo no painel de administração do Django.

# Import o módulo administrativo do Django.
from django.contrib import admin

# Importa o modelo que se deseja registrar no admin
from .models import Song


# É uma classe que herda de admin.ModelAdmin e define como o modelo SongAdmin deve ser exibido e gerenciado na interface administrativa.
class SongAdmin(admin.ModelAdmin):

    # Especifica quais campos do modelo devem ser exibidos na lista de registros
    list_display = (
        "title",
        "artist",
        "genre",
        "release_date",
    )

    # Configura quais campos na listagem são links clicáveis
    list_display_links = ("title",)

    # Configura quais campos na lista podem ser editados diretamente da lista
    list_editable = "genre"

    # Define quais campos podem ser pesquisados no painel de administração
    search_fields = (
        "title",
        "artist",
        "album",
    )

    # Adiciona filtros para facilitar a busca de reistros especificos
    list_filter = (
        "genre",
        "release_date",
    )
    # Define a ordem padrão dos registros quando a pagina é caregada
    ordering = "release_date"

    # Personalize quais campos são eibidos no formulário de edição e como eles são agrupados
    fieldssets = (
        (None, {"fields": ("title", "artist")}),
        ("Album Information", {"fields": ("album", "genre", "release_date")}),
    )

    # Adiciona ações (com uma função) personalizadas que podem ser executadas em massa sobre os registros selecionados
    actions = ["make_featured"]


# Se for colocado dentro do 'SongAdmin'deve ser 'self' e fora tem que ser 'modelAdmin'
def make_featured(modelAdmin, request, queryset):
    queryset.update(is_featured=True)


make_featured.short_description = "Mark Selected songs as featured"


# Registra o modelo "MyModel" com a classe de administração personalizada "MyModelAdmin"
admin.site.register(Song, SongAdmin)


"""
Considerações

- Customização: O arquivo 'admin.py' permite uma vasta gama de personalizações para o painel de administração. Isso pode incluir a adição de campos de formulário personalizados, a configuração de filtros complexos e a modificação de como os dados são exibidos e manipulados.

- Integração com ouros modelos: Você pode registrar múltiplos modelos no 'admin.py' e tambem pode criar varias classes administrativas personalizadas para diferentes modelos.

- Manutenção: Sempre que você adicionar novos campos ou alterar modelos, não se esqueça de revisar e ajustar o admin.py para refletir essas mudanças.

"""
