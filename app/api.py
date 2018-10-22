from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app import models
from app.backends import CustomFirebaseAuthentication
from app.serializers import CommentSerializer, ComplaintSerializer


class BaseViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CustomFirebaseAuthentication, BasicAuthentication)


class CommentViewSet(BaseViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer


class ComplaintViewSet(BaseViewSet):
    queryset = models.Complaint.objects.all()
    serializer_class = ComplaintSerializer
