from .models import Song

def load_initial_data():
    if not Song.objects.exists():
        Song.objects.create(title='Initial Song', artists='Initial Artist', genre='pop', release_date='2024-01-01')
        print('Dados iniciais carregados.')