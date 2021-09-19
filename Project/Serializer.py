from rest_framework import serializers
from django_filters import rest_framework as filters
from Project.models import News, ImageNews, Law, FavouriteNews


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id title publication_date image short_description'.split()


class ImageNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = 'id image'.split()


class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageNewsSerializer(many=True)

    class Meta:
        model = News
        fields = 'id title link full_description images'.split()


class LawListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title types short_description'.split()


class LawItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title full_description '.split()


class CharFilterinFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class LawFilter(filters.FilterSet):
    filter = CharFilterinFilter(field_name='types__id', lookup_expr='in')

    class Meta:
        model = Law
        fields = ['types']


class FavouriteSerializers(serializers.ModelSerializer):
    news = NewsListSerializer

    class Meta:
        model = FavouriteNews
        fields = "__all__"


class NewsWictFavouriteSerializers(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "id title is_favourite".split()

    def get_is_favourite(self, news):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and FavouriteNews.objects.filter(user=request.user, news=news).count() > 0)