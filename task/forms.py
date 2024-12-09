# from django import forms
# from .models import Post
# from ckeditor.widgets import CKEditorWidget

# class PostCreateForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Post
#         fields = ['title', 'category', 'content'] 


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if field_name not in ['title', 'category']: 
#                 field.label = ''
# from django import forms
# from .models import Category, Post



# class PostCreateForm(forms.ModelForm):
#     class Meta:
#         model = Post  # This tells Django that this form is tied to the Post model
#         fields = ['title', 'content', 'category']  # Specify the fields you want from the Post model
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Dynamically set the queryset for category to include all categories
#         self.fields['category'].queryset = Category.objects.all()
from django import forms
from .models import Post, Category

class PostCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),required=True,empty_label="Select a category")
        


    class Meta:
        model = Post
        fields = ['title', 'category','content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        new_category = cleaned_data.get('new_category')
        if category == 'other' and not new_category:
            self.add_error('new_category', 'This field is required for "Other" category.')
        return cleaned_data

