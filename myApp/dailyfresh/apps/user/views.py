from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail
import re
import time
from .models import User

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.conf import settings

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 1.获取post信息
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        # 数据校验
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        # 存入数据库
        user = User.objects.create_user(username, password, email)
        user.is_active = 0
        user.save()
        # 业务处理
        return redirect(reverse('goods:index'))


class RegisterView(View):

    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        # 1.获取post信息
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        # 数据校验
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        # 存入数据库
        user = User.objects.create_user(username, password, email)
        user.is_active = 0
        user.save()

        # 加密
        serializer = Serializer('11111', 3600)
        info = {"comfirm": user.id}
        token = serializer.dumps(info)
        token = token.decode()
        
        # 业务处理
        # 发送邮件

        def send_register_active_email(to_email, username, token):
            # 组织邮件信息
            subject = '天天生鲜欢迎信息'
            message = ''
            sender = settings.EMAIL_FROM
            receiver = [to_email]
            html_message = '<h1>%s, 欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)

            send_mail(subject, message, sender, receiver, html_message=html_message)

        send_register_active_email(email, username, token)

        return redirect(reverse('goods:index'))


class ActiveView(View):
    def get(self, request, token):
        serializer = Serializer('11111', 3600)
        try:
            info = serializer.loads(token)
            user_id = info['comfirm']
            user = User.objects.get(id=user_id)
            print(user)
            user.is_active = 1
            user.save()
            return redirect(reverse('user:login'))
        except SignatureExpired as identifier:
            return HttpResponse('激活己过期')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class test(View):
    def get(self, request, token):
        serializer = Serializer('11111', 3600)
        info = serializer.loads(token)
        user_id = info['comfirm']
        user = User.objects.get(id=user_id)
        return HttpResponse(user)