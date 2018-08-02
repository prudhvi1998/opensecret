from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView

from opensecretapp.forms import *
from opensecretapp.models import *

class UserPermissionRequiredMixin(PermissionRequiredMixin):
    def has_permission(self):
        a=OpenSecretUser.objects.values('user__id').get(id=self.kwargs['pk'])['user__id']
        b=self.request.user.id
        # print(a)
        # print(type(a).__name__)
        # print(b)
        # print(type(b).__name__)
        if(self.request.user.id == OpenSecretUser.objects.values('user__id').get(id=self.kwargs['pk'])['user__id']):
            # print("good")
            return True
        else:
            # print("bad very bad")
            return False

class SignUp(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,template_name='signup.html',context={'title':'Open Secret Signup','form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                new = OpenSecretUser(user=user)
                new.save()
                login(request,user)
                return redirect('opensecretapp:home')


class Login(View):
    def get(self,request):
        form = LoginForm()
        return render(request,template_name='login.html',context={'title':'Open Secret Login','form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('opensecretapp:home')
            else:
                return redirect('opensecretapp:login')

def Logout(request):
    logout(request)
    return redirect('/opensecret/login/')

def redirecttologin(request):
    return redirect('opensecretapp:login')

class MessagesListView(LoginRequiredMixin,ListView):
    login_url = '/opensecret/login/'
    model = Message
    context_object_name = 'messages'
    template_name = 'messages_listview.html'

    def get_context_data(self, **kwargs):
        context = super(MessagesListView,self).get_context_data(**kwargs)
        # m=Message.objects.values('id', 'msg', 'd_t', 'sender', 'receiver').filter(receiver=self.request.user.id)
        # sorted(L, key=itemgetter(2))
        # print(m)
        context['messages'] = Message.objects.values('id', 'msg', 'd_t').filter(receiver=self.request.user.id).order_by('-d_t')
        context['currentuser'] = OpenSecretUser.objects.get(user=self.request.user)
        return context


class OutBoxListView(LoginRequiredMixin,ListView):
    login_url = '/opensecret/login/'
    model = Message
    context_object_name = 'messages'
    template_name = 'outbox_listview.html'

    def get_context_data(self, **kwargs):
        context = super(OutBoxListView, self).get_context_data(**kwargs)
        # m = Message.objects.values('id', 'msg', 'd_t', 'receiver__user__username', 'receiver__pro_pic').filter(sender=self.request.user.id).order_by('-d_t')
        # sorted(L, key=itemgetter(2))
        context['messages'] = Message.objects.values('id', 'msg', 'd_t', 'receiver__user__username', 'receiver__pro_pic').filter(sender=self.request.user.id).order_by('-d_t')
        context['currentuser'] = OpenSecretUser.objects.get(user=self.request.user)
        return context

class UserProfileView(LoginRequiredMixin,View):
    login_url = '/opensecret/login/'
    # model = OpenSecretUser
    # template_name = 'user_profile.html'
    success_url = reverse_lazy("opensecretapp:home")

    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileView,self).get_context_data(**kwargs)
    #     form = MessageForm()
    #     value = list(self.kwargs.values())
    #     context['userprofile'] = OpenSecretUser.objects.get(user__username=value[0])
    #     context['form'] = form
    #     return context

    def get(self,request, **kwargs):
        form = MessageForm()
        value = list(self.kwargs.values())
        return render(request,template_name='user_profile.html',context={'userprofile':OpenSecretUser.objects.get(user__username=value[0]),'form':form})

    def post(self,request, **kwargs):
        form = MessageForm(request.POST)
        value = list(self.kwargs.values())
        if form.is_valid():
            msg = form.cleaned_data['message']
            s = User.objects.get(id=self.request.user.id)
            r = User.objects.get(username=value[0])
            # print(s.username)
            # print(r.username)
            m = Message(msg=msg,sender=OpenSecretUser.objects.get(id=self.request.user.id),receiver=OpenSecretUser.objects.get(user__username=value[0]))
            m.save()
            u=OpenSecretUser.objects.get(user__username=value[0])
            u=OpenSecretUser.objects.get(user=User.objects.get(username=value[0]))
            u.messages.add(m)
            return redirect("opensecretapp:home")

class HomeView(LoginRequiredMixin,ListView):
    login_url = '/opensecret/login/'
    model = OpenSecretUser
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        context = super(HomeView,self).get_context_data(**kwargs)
        context['currentuser'] = OpenSecretUser.objects.get(user=self.request.user)
        context['userprofiles'] = OpenSecretUser.objects.exclude(user=self.request.user)
        return context

class UpdateProfileView(LoginRequiredMixin,UserPermissionRequiredMixin,UpdateView):
    login_url = '/opensecret/login/'
    model = OpenSecretUser
    form_class = UpdateProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy("opensecretapp:home")

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView,self).get_context_data(**kwargs)
        context['currentuser'] = OpenSecretUser.objects.get(user=self.request.user)
        return context

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})