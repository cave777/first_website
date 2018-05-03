from django.views import generic
from .models import Albums
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from.models import Albums
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'musicapp/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Albums.objects.all

class DetailView(generic.DetailView):
    model = Albums
    template_name = 'musicapp/detail.html'


class AlbumCreate(CreateView):
    model = Albums
    fields = ['artist','album_title','genre','album_logo']
    template_name = 'musicapp/albums_form.html'


class AlbumEdit(UpdateView):
    model = Albums
    fields = ['artist','album_title','genre','album_logo']
    template_name = 'musicapp/albums_form.html'


class AlbumDelete(DeleteView):
    model = Albums
    success_url = reverse_lazy('musicapp:index')



class UserFormView(View):
    form_class = UserForm
    template_name = 'musicapp/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)# wont save at databse , saves locally
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('musicapp:index')

        return render(request, self.template_name,{'form': form})









