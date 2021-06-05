from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm, AddRequestForm, AddWorkForm
from .models import CustomUser,Works, Request


#Указать стандартной админке использовать новую форму customuser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','name')
    list_filter = ('email', 'is_staff', 'is_active','name')
    fieldsets = (
        (None, {'fields': ('email', 'password','name', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','name', 'image')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)




@admin.register(Request)
class AddRequestForm(admin.ModelAdmin):
    list_display = ("email", "name", "message")



@admin.register(Works)
class AddWorkForm(admin.ModelAdmin):
    list_display = ("title", "description", "category")

    

admin.site.register(CustomUser, CustomUserAdmin)
