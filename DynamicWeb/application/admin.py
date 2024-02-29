from django.contrib import admin
from application.models import Genre, Artist, Movie, ContactMessage
from .models import AboutContent

admin.site.register(AboutContent)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Movie)
admin.site.register(ContactMessage)