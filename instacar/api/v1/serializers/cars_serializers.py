from rest_framework import serializers

from cars.models import Car, Comment


class CarsSerializer(serializers.ModelSerializer):
    """Сериализатор Авто"""
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'description', 'owner',)
        read_only_fields = ('owner',)


class CreateCarsSerializer(serializers.ModelSerializer):
    """Сериализатор Создания Авто"""
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'description')

    def create(self, validated_data):
        return super().create(validated_data)


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализатор Комментария"""
    class Meta:
        model = Comment
        fields = ('content', 'author')
        read_only_fields = ('author',)


class CreateCommentSerializer(serializers.ModelSerializer):
    """Сериализатор Создания Комментария"""
    class Meta:
        model = Comment
        fields = ('content',)

    def create(self, validated_data):
        return super().create(validated_data)
