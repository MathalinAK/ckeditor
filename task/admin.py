# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import task,Post
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from django import forms

# class taskAdmin(UserAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active')  
#     search_fields = ('username', 'email')  
#     readonly_fields = ('date_joined', 'last_login')  

#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     actions = ['delete_selected'] 


#     def delete_selected(self, request, queryset):
#         count = queryset.count()
#         queryset.delete()  
#         self.message_user(request, f'Deleted {count} user(s) successfully.')

#     delete_selected.short_description = "Delete selected users"  
# admin.site.register(task, taskAdmin)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
 
#     list_display = ('title',  'date_posted', 'date_updated')
#     search_fields = ('categories','title', 'content', )  
#     list_filter = ('date_posted', )  
#     ordering = ('-date_posted',) 

    
#     actions = ['delete_selected_posts']

#     def delete_selected_posts(self, request, queryset):
#         count = queryset.count()
#         queryset.delete()
#         self.message_user(request, f'Deleted {count} post(s) successfully.')

#     delete_selected_posts.short_description = "Delete selected posts"
#     content = forms.CharField(widget=CKEditorUploadingWidget())
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Post,task
class taskAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  
    search_fields = ('username', 'email')  
    readonly_fields = ('date_joined', 'last_login')  

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    actions = ['delete_selected'] 


    def delete_selected(self, request, queryset):
        count = queryset.count()
        queryset.delete()  
        self.message_user(request, f'Deleted {count} user(s) successfully.')

    delete_selected.short_description = "Delete selected users"  
admin.site.register(task, taskAdmin)



class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())  

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',) 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = ('title', 'category', 'date_posted', 'date_updated')  
    search_fields = ('title', 'content', 'category__name')  
    list_filter = ('category', 'date_posted')  
    ordering = ('-date_posted',)  
    autocomplete_fields = ('category',)  

