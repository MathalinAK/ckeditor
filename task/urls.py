from django.contrib import admin
from django.urls import path
from .views import loginView, HomeView, HomesView, PostCreateView, logoutView, UpdateCategoryView,DeleteCategoryView, PostEditView,PostDeleteView,SearchView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
    path('homes/', HomesView.as_view(), name='homes'),
    path('create/', PostCreateView.as_view(), name='post_create'),
   
    path('logout/',  logoutView.as_view(), name='logout'),
    path('edit/<int:category_id>/<int:post_id>/', PostEditView.as_view(), name='post_edit'),
    path('edit/<int:post_id>/', PostEditView.as_view(), name='post_edit'),
    path('delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('search/', SearchView.as_view(), name='search'),
    path('categories/delete/<int:category_id>/', DeleteCategoryView.as_view(), name='delete_category'),
  # path('sorted-posts/', SortedPostsView.as_view(), name='sorted_posts'),
   path("update-category/", UpdateCategoryView.as_view(), name="update_category"),

]
