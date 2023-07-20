from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .utils import *
from .models import *
from .forms import *


# Create your views here.

class HomeView(DataMixin, ListView):
    model = AnimeArtModel
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return AnimeArtModel.objects.filter(is_published=True)


def searchView(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = AnimeArtModel.objects.filter(name__icontains=query)

    context = {
        'form': form,
        'results': results,
        'title': 'Страница поиска',
        'menu': menu,
    }
    return render(request, 'main/search.html', context=context)


class ImagesView(DataMixin, ListView):
    model = AnimeArtModel
    template_name = 'main/images.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Картинки')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return AnimeArtModel.objects.filter(is_published=True)



def aboutView(request):
    context = {
        'title': 'О нас',
        'menu': menu,
    }
    return render(request, 'main/about.html', context=context)


def contactView(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()
    if form.is_valid():
        form.save()
        redirect('home')

    context = {
        'title': 'Обратная связь',
        'form': form,
        'menu': menu,
    }
    return render(request, 'main/contact.html', context=context)


class SignUpView(DataMixin, CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_success_url(self):
        reverse_lazy('login')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    success_url = reverse_lazy('home')
    template_name = 'main/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profileView(request):
    context = {
        'title': 'Профиль',
        'menu': menu,
    }
    return render(request, 'main/profile.html', context)


class ProfileView(DataMixin, LoginRequiredMixin, ListView):
    # def get(self, request):
    #     return render(request, 'accounts/profile.html')
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'main/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Профиль')

        return dict(list(context.items()) + list(c_def.items()))


class EditProfileView(DataMixin, LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    # fields = '__all__'
    template_name = 'main/edit_profile.html'
    success_url = reverse_lazy('profile')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Изменение профиля')

        return dict(list(context.items()) + list(c_def.items()))

    def get_object(self, queryset=None):
        return self.request.user


class DeleteProfileView(DataMixin, LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'main/delete_profile.html'
    success_url = reverse_lazy('logout')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Удаление профиля')

        return dict(list(context.items()) + list(c_def.items()))

    def get_object(self, queryset=None):
        return self.request.user


def publicationView(request):
    if request.method == 'POST':
        form = AnimeArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images')  # Предполагается, что у вас есть представление anime_list для отображения списка аниме.
    else:
        form = AnimeArtForm()
    return render(request, 'main/publication.html', {'form': form, 'menu': menu, 'title': 'Публикация'})