from .models import ClassMessage, Message
from rest_framework import serializers
from django.contrib.auth.models import User


class UserUserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class MessageSerializers(serializers.ModelSerializer):
    sender = UserUserNameSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['body', 'sender', 'parent_msg', 'sent_at']
        read_only_fields = ['sent_at', 'sender']


class ClassMessegeSerializers(serializers.ModelSerializer):
    msg = MessageSerializers()

    class Meta:
        model = ClassMessage
        fields = ['msg', 'classes']

    def create(self, validated_data):
        # order = Order.objects.get(pk=validated_data.pop('event'))
        # instance = Equipment.objects.create(**validated_data)
        # Assignment.objects.create(Order=order, Equipment=instance)read_only=True)
        msg_data = validated_data.pop('msg')
        sender = validated_data.pop('msg__sender')

        msg = Message.objects.create(
            **msg_data, sender=sender)
        msg.save()
        instance = ClassMessage.objects.create(**validated_data, msg=msg)
        return instance
