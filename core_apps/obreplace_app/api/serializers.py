from rest_framework import serializers
from core_apps.obreplace_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = '__all__'                         # return all fields
        # fields = ['id', 'name', 'description']   # return in fields choices
        # exclude = ['name']                       # exclude -> not retrun


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchSerializer(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='stream-platfrom'
    # )

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'stream-platfrom'},
        }

    # def get_len_title(self, object):
    #     return len(object.title)

    #     # validate fields from data required

    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError('Title and description must be different')
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name must be at least 2 characters long')
    #     else:
    #         return value
