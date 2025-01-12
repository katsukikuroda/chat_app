from django.contrib import admin
from .models import Talk, User

admin.site.register(User)
#↓29で追加(教科書の掲載無し)
admin.site.register(Talk)