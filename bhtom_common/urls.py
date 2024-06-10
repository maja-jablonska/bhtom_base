"""bhtom_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from .views import CustomPasswordResetView
from django.contrib.auth import views as auth_views
from bhtom_base.bhtom_common.api_views import GroupViewSet
from bhtom_base.bhtom_common.views import UserListView, UserPasswordChangeView, UserCreateView, UserDeleteView, UserUpdateView
from bhtom_base.bhtom_common.views import CommentDeleteView, GroupCreateView, GroupUpdateView, GroupDeleteView

from .api_router import collect_api_urls, SharedAPIRootRouter  # DRF routers are setup in each INSTALL_APPS url.py

router = SharedAPIRootRouter()
router.register(r'groups', GroupViewSet, 'groups')

urlpatterns = [
    path('', TemplateView.as_view(template_name='bhtom_common/index.html'), name='home'),
    path('about/',TemplateView.as_view(template_name='bhtom_common/about.html'), name='about'),
    path('targets/', include('bhtom_base.bhtom_targets.urls', namespace='targets')),
    path('alerts/', include('bhtom_base.bhtom_alerts.urls', namespace='alerts')),
    path('comments/', include('django_comments.urls')),
    path('catalogs/', include('bhtom_base.bhtom_catalogs.urls')),
    path('observations/', include('bhtom_base.bhtom_observations.urls', namespace='observations')),
    path('dataproducts/', include('bhtom_base.bhtom_dataproducts.urls', namespace='dataproducts')),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/changepassword/', UserPasswordChangeView.as_view(), name='admin-user-change-password'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('comment/<int:pk_target>//<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/', include((collect_api_urls(), 'api'), namespace='api')),
    path('api/token-auth/', views.obtain_auth_token)
    # The static helper below only works in development see
    # https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
