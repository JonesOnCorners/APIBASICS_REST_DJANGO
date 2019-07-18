from rest_framework import serializers, viewsets
from .models import Snippet, LANGUAGE_CHOICES, LEXERS, STYLE_CHOICES

#Add a new comment
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Snippet
        fields = ['created', 'title', 'code', 'linenos', 'language', 'style']