from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import ChatUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
@admin.register(ChatUser)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = ChatUser
