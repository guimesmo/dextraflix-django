from django.shortcuts import render
from video.models import Video, Author

from django import forms


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        exclude = ['slug']


def home(request):
    message = None
    videos = Video.objects.all()
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            author_form = AuthorForm()
            message = "O autor foi criado com sucesso"
    else:
        author_form = AuthorForm()

    return render(request, "home.html",
                  {"videos": videos,
                   "author_form": author_form,
                   "message": message})
