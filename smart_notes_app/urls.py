from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, NoteViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_template, login_template, notes_template


router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

    path('register/', register_template, name='register_page'),
    path('loginpage/', login_template, name='login_page'),
    path('notespage/', notes_template, name='notes_page'),

    path('', include(router.urls)),
]


