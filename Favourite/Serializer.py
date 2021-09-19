from rest_framework import serializers
from Project.Serializer import LawListSerializer
from .models import Favourite
from Project.models import Law
class FavouriteSerializer(serializers.ModelSerializer):
    legis = LawListSerializer

    class Meta:
        model = Favourite
        fields = "__all__"


class WictFavouriteSerializer(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = Law
        fields = "id title is_favourite".split()

    def get_is_favourite(self, izb):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and Favourite.objects.filter(user=request.user, izb=izb).count() > 0)