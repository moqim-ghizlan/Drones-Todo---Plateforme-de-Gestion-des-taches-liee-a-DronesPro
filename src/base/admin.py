from django.contrib import admin
from .models import Todo, User, Category
from django.contrib.auth.admin import UserAdmin

admin.site.register(Category)


class TodoAdminConfig(admin.ModelAdmin):
    list_display = ('get_title', 'get_description', 'get_completed')
    list_display_links = ('get_title', 'get_description','get_completed')


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


    def get_title(self, obj):
        if len(obj.title) > 20:
            return f'{obj.title[:20]} ...'
        return obj.title
    def get_description(self, obj):
        if len(obj.description) > 20:
            return f'{obj.description[:20]} ...'
        return obj.description

    def get_completed(self, obj):
        return obj.completed


    def get_status(self, obj):
        return obj.get_franch_phrase()


    def is_active(self, obj):
        return obj.active


    get_title.string = True
    get_title.short_description = 'Titre'

    get_description.string = True
    get_description.short_description = 'Description'



    get_completed.boolean = True
    get_completed.short_description = 'Complété'





admin.site.register(Todo, TodoAdminConfig)






class UserAdminConfig(UserAdmin):
    list_display = ('username', 'email')
    list_display_links = ('username', 'email')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(User, UserAdminConfig)
