from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member,Post,ForbiddenWord,Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MemberSerializer

def home(request):
    all_posts=Post.objects.all()
    all_categories=Category.objects.all()
    context={'posts':all_posts, 'categories':all_categories}
    return render(request,'blog/home.html',context)


def postDetails(request,post_id):
    one_post=Post.objects.get(id=post_id)
    context={'post':one_post}
    return render(request,'blog/post_details.html',context)

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))


# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))

#             else:
#                 return HttpResponse("Account is not active")

#         else:
#             print("Some try to login and failed")
#             print("Username: {} & password: {}".format(username,password))
#             return HttpResponse("Invilide login details supplied")

#     else:
#         return render(request, 'blog/login.html',{})




# @login_required
# def special(request):
#     return HttpResponse("You are loged in")



#login page function
# def login_user(request):
# 	if request.method == 'POST':
# 	    username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(request, 'sorry you are blocked contact the admin')
#                 return redirect('login')
#     else:
#         return render(request,'blog/login.html')








#rest Framework views here.
@api_view(['GET'])
def api_all_users(request):
    all_users = Member.objects.all()
    user_ser = MemberSerializer(all_users, many=True)
    return Response(user_ser.data)
@api_view(['GET'])
def api_one_user(request, user_id):
    user = Member.objects.get(id=user_id)
    user_ser = MemberSerializer(user, many=False)
    return Response(user_ser.data)
@api_view(['POST'])
def api_add_user(request):
    user_ser = MemberSerializer(data=request.data)
    if user_ser.is_valid():
        user_ser.save()
        return redirect('api-all')
@api_view(['POST'])
def api_edit_user(request, user_id):
    user= Member.objects.get(id=user_id)
    user_ser = MemberSerializer(data=request.data, instance=user)
    if user_ser.is_valid():
        user_ser.save()
        return redirect('api-all')
@api_view(['DELETE'])
def api_del_user(request, user_id):
    user= Member.objects.get(id=user_id)
    user.delete()
    return Response('User Deleted successfully!')