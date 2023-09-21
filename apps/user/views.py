from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views import View
from .models import User


def user_list(request):
    users = User.objects.all()[::-1]
    
    context = {
        'users': users,
    }
    
    return render(request, 'user/user_list.html',context)
    
class LoginView(View):
    template_name = "user/login.html"
    
    def get(self, request):
        form = AuthenticationForm()
        return render(
            request, 
            self.template_name, 
            {"form":form})
        
    def post(self,request):

        form = AuthenticationForm(data=request.POST)
        
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            
            #check if auth sucessfull
            if user is not None:
                # use the session to keep the authenticated users id
                login(request, user)
                #when we log in, the session will store the user id
                #auth middleware is going to use that id
                # and fetch the user from the dabase and store it in the
                # request.user object
                
                #redirect the user to his profile page
                #url path !name!
                return redirect("profile")
                
        else: 
            error_message = "No worky!"
        
        context = {"form": form, "error_message": error_message}       
        
        return render(
            request,
            self.template_name,
            context,
        )
    
class ProfileView(View):
    template_name="user/profile.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass