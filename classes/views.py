# from django.shortcuts import render

# Create your views here.

# TODO
# - admin can create Course
# - admin can create TimeTable
# - Teacher can create class
# - Teacher can create and insert Attendence
from .messages import *
from accounts.custom_permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import CourseSerializer, TimeTableSerializer


class AdminCreateCourse(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': COURSE_REGISTER_SUCCESS_MESSAGE}, status=COURSE_REGISTER_SUCCESS_STATUS)


class AdminCreateTimeTable(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        serializer = TimeTableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # this is my code
