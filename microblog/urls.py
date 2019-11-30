"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    # path('<URL>', views(関数), ニックネーム)
    # http://localhost:8000/<...> : index
    path('', BlogListView.as_view(), name="index"),
    # http://localhost:8000/20
    # 20 -> pk : pk = 20
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('create', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/update', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name="delete"),
    path('admin/', admin.site.urls),
]
