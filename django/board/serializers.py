from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['author', 'subject', 'content', 'create_date']

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['author', 'question', 'content', 'create_date']
