from rest_framework import serializers
from core_apps.obreplace_app.models import WatchList, StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'


class WatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'                         # return all fields
        # fields = ['id', 'name', 'description']   # return in fields choices
        # exclude = ['name']                       # exclude -> not retrun

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
