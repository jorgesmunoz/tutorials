
from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippets-highlight', format='html')
    url = serializers.HyperlinkedIdentityField(view_name='snippets-detail')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code',
                  'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippets-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='users-detail')

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
