from rest_framework import serializers

from server.models import Sensor


class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    voltage = serializers.IntegerField(required=True)
    current = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.voltage = validated_data.get('voltage', instance.voltage)
        instance.current = validated_data.get('current', instance.current)
        instance.save()
        return instance
