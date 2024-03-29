from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .validators import validate_file_extension

from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializer,UserSerializer

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def register(request):
    data=request.data

    user=SignUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user=User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )

            return Response ({
                'message':'User Registered Successfully!'},
                status=status.HTTP_200_Ok
            )
        else:
            return Response ({
                'error':'User Already Exists!'},
                status=status.HTTP_400_BAD_REQUEST
            )

    else:
        return Response(user.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):

    user=UserSerializer(request.user)

    return Response(user.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request):
    user=request.user

    

    data=request.data

    user.first_name=data['first_name']
    user.last_name=data['last_name']
    user.username=data['email']
    user.email=data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    serializer=UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def uploadResume(request):

    
    user=request.user
    resume=request.FILES['resume']
    

    if resume == '':
        return Response({'error':'Please Upload Your Resume!'}, status=status.HTTP_400_BAD_REQUEST)
    
    isValidFile=validate_file_extension(resume.name)

    if not isValidFile:
        return Response({'error':'Only PDF Files are Valid!'}, status=status.HTTP_400_BAD_REQUEST)
    

    user.userprofile.resume=resume
    user.userprofile.save()

    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)