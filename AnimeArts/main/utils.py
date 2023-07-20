from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Поиск', 'url_name': 'search'},
    {'title': 'Картинки', 'url_name': 'images'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Публиковать', 'url_name': 'publication'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        animeArts = AnimeArtModel.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            if not self.request.user.is_superuser:
                pass
            user_menu.pop(-1)


        context['menu'] = user_menu
        context['animeArts'] = animeArts

        return context
