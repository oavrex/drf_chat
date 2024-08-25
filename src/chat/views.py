from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
	queryset = ChatRoom.objects.all()
	serializer_class = ChatRoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer

	def get_queryset(self):
		return self.queryset.filter(room_id=self.kwargs['room_pk'])

	def perform_create(self,serializer):
		serializer.save(user=self.request.user, room_id=self.kwargs['room_pk'])



