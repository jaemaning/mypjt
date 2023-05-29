# from django.shortcuts import render
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
# from django.views.decorators.http import require_POST, require_http_methods

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import FollowSerializer
from .serializers import YourpageSerializer
# from .forms import RegistrationForm
# from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

# @api_view(['POST'])
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         print(form)
#         if form.is_valid(raise_exception=True):
#             print('99999999999999999999999999999999999')
#             auth_login(request, form.get_user())
#             print('user')
#             print('user', request.user)
#             # serializer.save()

#             return Response( status=status.HTTP_204_NO_CONTENT)
            
            
# @api_view(['POST'])
# def logout(request):
#     print('9999999999999999999999999999')
#     auth_logout(request)
#     print(request.user)

#     return Response( status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['POST'])
# def signup(request):
#     print("here")
#     print(request.method)
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         print(form)

#         if form.is_valid():
#             form.save()

#             return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                is_followed = False
            else:
                person.followers.add(user)
                is_followed = True
            # serializer = FollowSerializer(person)
        # serializer = {
        #     'followings' : person.followings.count(),
        #     'followers' : person.followers.count(),
        #     'is_follwed' : is_followed,
        # }
        # return JsonResponse(serializer, safe=False, status=status.HTTP_200_OK)
        serializer = YourpageSerializer(person)
        print(person.followers)
        print(serializer)
        return Response(serializer.data)

@api_view(['GET'])
def yourpage(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    if person.followers.filter(pk=user.pk).exists():        
        is_followed = False
    else:
        is_followed = True
    # serializer = {
    #         'username' : person.username,
    #         'followings' : person.followings,
    #         'followers' : person.followers,
    #         'is_follwed' : is_followed,
    #     }
    serializer = YourpageSerializer(person)
    return Response(serializer.data)

@api_view(['GET'])
def mypage(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = YourpageSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
def store_score(request):
    user = request.user
    user.point += int(request.data['score'])
    user.save()
    return Response(status=status.HTTP_200_OK)