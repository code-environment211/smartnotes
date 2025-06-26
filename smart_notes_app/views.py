from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import User, Note
from .serializers import RegisterSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def register_template(request):
    return render(request, 'register.html')

def login_template(request):
    return render(request, 'login.html')

@login_required
def notes_template(request):
    return render(request, 'notes.html')
