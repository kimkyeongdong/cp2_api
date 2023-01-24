from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from common.serializers import UserSerializer, GroupSerializer
from board.models import Question, Answer
from board.serializers import QuestionSerializer, AnswerSerializer

from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-create_date')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Answer.objects.all().order_by('-create_date')
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]