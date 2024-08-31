"""
Serializers for experience APIs
"""
from rest_framework import serializers

from core.models import (Experience)


class ExperienceSerializer(serializers.ModelSerializer):
    """Serializer for experience."""
    class Meta:
        model = Experience
        fields = [
            'id', 'title', 'description'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a experience."""
        experience = Experience.objects.create(**validated_data)

        return experience

    def update(self, instance, validated_data):
        """Update a experience."""

        for k, v in validated_data.items():
            setattr(instance, k, v)

        instance.save()
        return instance

