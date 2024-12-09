from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Post,Category
from .forms import PostCreateForm
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View
import json

class loginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('homes')  
            else:
                messages.error(request, 'You do not have permission to access this page.')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Invalid credential')
            return render(request, 'login.html')

# class HomeView(View):
#     def get(self, request):
#         print(f"User authenticated: {request.user.is_authenticated}")
#         posts = Post.objects.all() 
#         post_id = request.GET.get('post_id')
#         categories=None
#         selected_post = None
        
#         if post_id:
#             categories = Post.objects.all()
#             selected_post = Post.objects.filter(id=post_id).first()
#         else:
#             selected_post = posts.first()
#         context = {
#             "posts": posts,
#             "categories":categories,
#             "selected_post": selected_post,
#         }
#         return render(request, "home_view.html", context)

# class HomesView(LoginRequiredMixin,View):
#    def get(self, request):
#         posts = Post.objects.all() 
#         print(posts) 
#         selected_post = None
#         post_id = request.GET.get('post_id') 

#         if post_id:
#             selected_post = Post.objects.filter(id=post_id).first()
            
#         else:
#             selected_post = posts.first()  

#         context = {
#             'posts': posts,
#             'selected_post': selected_post,
#         }
#         return render(request, 'homes.html', context)
# class PostCreateView(View):
#     def get(self, request):
#         form = PostCreateForm()
#         posts = Post.objects.all() 
#         return render(request, 'post_create.html', {'form': form, 'posts': posts})

#     def post(self, request):
#         form = PostCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('homes')  
        
#         posts = Post.objects.all()
#         return render(request, 'post_create.html', {'form': form, 'posts': posts})


# class PostEditView(LoginRequiredMixin, View):
#     def get(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         form = PostCreateForm(instance=post) 
#         return render(request, 'post_create.html', {'form': form})

#     def post(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         form = PostCreateForm(request.POST, instance=post) 
        
#         if form.is_valid():
#             form.save()  
#             return redirect('homes')
# class PostDeleteView(LoginRequiredMixin, View):
#     def post(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         if post:
#             post.delete()  
#         return redirect('homes')  
# class SearchView(View):
#     def get(self, request):
#         query = request.GET.get('query', '').strip()
#         if query:
#             results = Post.objects.filter(title__icontains=query) | Post.objects.filter(category__icontains=query)
#             data = [
#                 {
#                     "id": result.id,
#                     "title": result.title,
#                     "category": result.category,
#                 }
#                 for result in results
#             ]
#         else:
#             data = []
#         return JsonResponse({"results": data})


       
# class logoutView(View):
#     def get(self, request):
       
#         logout(request)
#         return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('homes')
            else:
                messages.error(request, 'You do not have permission to access this page.')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'login.html')


class HomeView(View):
    def get(self, request):
    
        categories = Category.objects.all()
        category_id = request.GET.get('category_id')
        post_id = request.GET.get('post_id')
        sort_by=request.GET.get('sort_by','A-Z')
        selected_category = None
        selected_post = None
        posts = []

        if not category_id and categories.exists():
            selected_category = categories.first()
            posts = selected_category.posts.all()
        elif category_id:
            selected_category = get_object_or_404(Category, pk=category_id)
            posts = selected_category.posts.all()
        if sort_by == 'A-Z':
            posts = posts.order_by('title')
            print(posts)
        elif sort_by== 'Z-A':
            posts = posts.order_by('-title')
            print(posts)
        elif sort_by== 'new':
            posts = posts.order_by('-date_posted')
            print(posts)
        elif sort_by == 'old':
            posts = posts.order_by('date_posted')
            print(posts)

        

      
        if post_id and selected_category:
            selected_post = get_object_or_404(posts, pk=post_id)

      
        return render(request, 'home_view.html', {
            'categories': categories,
            'selected_category': selected_category,
            'posts': posts,
            'selected_post': selected_post, 
            'selected_sort': sort_by
        })




class HomesView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all() 
        category_id = request.GET.get('category_id')
        post_id = request.GET.get('post_id')
        sort_by=request.GET.get('sort_by','A-Z')
        selected_category = None
        selected_post = None
        posts = []
        if not category_id and categories.exists():
            selected_category = categories.first()
            posts = selected_category.posts.all()
        elif category_id:
            selected_category = get_object_or_404(Category, pk=category_id)
            posts = selected_category.posts.all()
        if sort_by == 'A-Z':
            posts = posts.order_by('title')
            print(posts)
        elif sort_by== 'Z-A':
            posts = posts.order_by('-title')
            print(posts)
        elif sort_by== 'new':
            posts = posts.order_by('-date_posted')
            print(posts)
        elif sort_by == 'old':
            posts = posts.order_by('date_posted')
            print(posts)
        if post_id and selected_category:
          
            selected_post = get_object_or_404(posts, pk=post_id)
            print(selected_post.title)


        return render(request, 'homes.html', {
            'categories': categories,
            'selected_category': selected_category,
            'posts': posts,
            'selected_post': selected_post,
            'selected_sort': sort_by, 

        })
class PostCreateView(View):
    def get(self, request):
        form = PostCreateForm()
        categories = Category.objects.all()
        return render(request, 'post_create.html', {'form': form, 'categories': categories})
    def post(self, request):
        category_id = request.POST.get('category')  
        new_category = request.POST.get('new_category', '').strip()  
        print(new_category)
        form_data = request.POST.dict()  
        print(form_data)
        if category_id == 'other' and new_category:
            category, created = Category.objects.get_or_create(name=new_category)
            form_data['category'] = category.id 
            print(form_data['category'])
        form = PostCreateForm(form_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully!")
            return redirect('homes')  
        
        categories = Category.objects.all()
        return render(request, 'post_create.html', {'form': form, 'categories': categories})

class PostEditView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        categories = Category.objects.all()
        form = PostCreateForm(instance=post)
        return render(request, 'post_edit.html', {'form': form, 'categories': categories, 'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form_data = request.POST.dict() 
        category_id = request.POST.get('category')
        new_category = request.POST.get('new_category', '').strip()
        
        if category_id == 'other' and new_category:
            try:
                category = Category.objects.get(name=new_category)
            except Category.DoesNotExist:
                category = Category.objects.create(name=new_category)
            form_data['category'] = category.id  
        elif category_id:
            category = get_object_or_404(Category, id=category_id)
            form_data['category'] = category_id
        
        form = PostCreateForm(form_data, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "The changes have been saved successfully.")
            return redirect('homes')
        categories = Category.objects.all()
        return render(request, 'post_create.html', {'form': form, 'categories': categories, 'post': post})






class PostDeleteView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
      
        return redirect('homes')

class SearchView(View):
    def get(self, request):
        query = request.GET.get('query', '').strip()  

        if len(query) < 3:
            return JsonResponse({
                'results': [],
                'message': 'Please enter at least 3 characters to search.'
            })

        posts = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            category__name__icontains=query
        )

        results = [
            {
                'id': post.id,
                'title': post.title,
                'category': post.category.name,
                'content': post.content  
            }
            for post in posts
        ]

        if results:
            return JsonResponse({'results': results})
        else:
            return JsonResponse({
                'results': [],
                'message': 'No results found for your query.'
            })
class DeleteCategoryView(View):
    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return JsonResponse({'success': True})



class UpdateCategoryView(View):
    def post(self, request, *args, **kwargs):
        # Extract category_id and category_name from POST data
        category_id = request.POST.get("category_id")
        new_name = request.POST.get("category_name")

        if not category_id or not new_name:
            return JsonResponse({"success": False, "message": "Invalid data provided."}, status=400)

        category = get_object_or_404(Category, id=category_id)
        category.name = new_name
        category.save()  

        return JsonResponse({"success": True, "message": "Category updated successfully!", "new_name": new_name})

# class SortedPostsView(View):
#     def get(self, request, *args, **kwargs):
#         category_id = request.GET.get('category_id')
#         category = get_object_or_404(Category, id=category_id)
#         sortBy = request.GET.get('sort', 'name')

#         posts = category.posts.all()

#         if sortBy == 'name':
#             posts = posts.order_by('title')
#         elif sortBy == 'name_desc':
#             posts = posts.order_by('-title')
#         elif sortBy == 'updatedAt':
#             posts = posts.order_by('-date_updated')
#         elif sortBy == 'oldest_created':
#             posts = posts.order_by('date_posted')

#         posts_data = list(posts.values('id', 'title', 'category__name'))

#         # Return JSON response if AJAX
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             return JsonResponse({'posts': posts_data, 'category_id': category_id})

#         # Fallback for non-AJAX requests
#         return render(request, 'posts_list.html', {'posts': posts, 'category': category})



class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')




