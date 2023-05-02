from rest_framework import serializers
from listaprojetos.models import Projetos


class ProjetosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projetos
        fields = "__all__"
