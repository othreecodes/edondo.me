from rest_framework import serializers

from app import models


class UserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
        fields = ('username', 'image')

    def get_username(self, object):
        return object.profile.username

    def get_image(self, object):
        return "https://api.adorable.io/avatars/150/{}.png".format(object.profile.username)


class CommentSerializer(serializers.ModelSerializer):
    commenter = UserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        exclude = ('id',)


class ComplaintSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, source='comment_set', read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Complaint
        fields = ('user', 'text', 'time', 'comments')
