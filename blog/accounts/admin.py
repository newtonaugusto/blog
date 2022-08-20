
from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """Configurando o formulário de criação de usuário"""
    model = User
    list_display = ['id', 'username', 'email']
    search_fields = ['username']


admin.site.register(User, UserAdmin)
