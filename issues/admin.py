from django.contrib import admin
from .models import Issue, Vote

# Register your models here.
admin.site.register(Issue)
admin.site.register(Vote)
