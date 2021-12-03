from rest_framework import serializers

class ActionSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    text = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)



class ActionAddSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)


class ActionUpdateSerializer(ActionAddSerializer):
    pass