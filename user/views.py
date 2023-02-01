from .forms import UpdateUserForm
from .models import User
from .forms import UserCreateForm
from .forms import AdminUpdateUserForm
from .forms import UserUpdatePasswordForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


def admin_required(login_url=None):
    return user_passes_test(lambda x: x.is_superuser, login_url=login_url)


def home(request):
    return render(request, 'main/main.html')


@login_required(login_url='/login')
def profile(request, username):
    get_current_user = User.objects.get(
        id=request.session.get('_auth_user_id'))
    if request.method == 'POST':
        username2 = request.POST['username']
        try:
            get_user = User.objects.get(username=username2)
        except User.DoesNotExist:
            messages.error(request, 'User not found!!!')
            return redirect('/profile/{}'.format(get_current_user.username))
    else:
        try:
            get_user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User not found!!!')
            return redirect('/profile/{}'.format(get_current_user.username))
    return render(request, 'account/profile.html', {'get_user': get_user})


@login_required(login_url='/login')
def user_profile(request):
    return HttpResponseRedirect(reverse('user:profile', kwargs={
        'username': request.user.username}))


@login_required(login_url='/login')
def update_profile(request, username):
    get_user = User.objects.get(username=username)
    if request.method == 'POST':
        if request.user.is_superuser:
            form = UpdateUserForm(request.POST, instance=get_user)
        else:
            form = AdminUpdateUserForm(request.POST, instance=get_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile have been updated successfully')
            return HttpResponseRedirect(reverse('user:get_all_users'))
        else:
            messages.error(request, '''something went wrong
                           when update the user''')
            return HttpResponseRedirect(reverse('user:get_all_users'))
    else:
        users = User.objects.all()
        if request.user.is_superuser:
            form = AdminUpdateUserForm(instance=get_user)
        else:
            form = UpdateUserForm(instance=get_user)
    return render(request, 'registration/update_profile.html',
                  {'form': form, 'users': users, 'get_user': get_user})


@login_required(login_url="/login")
def update_user_password(request, username):
    get_user = User.objects.get(username=username)
    return render(request, 'registration/password_reset.html',
                  {'get_user': get_user})


@login_required(login_url="/login")
@admin_required(login_url='/profile')
def all_user(request):
    users = User.objects.all()
    return render(request, 'admins/user.html', {'users_list': users})


@admin_required(login_url='/profile}')
@login_required(login_url="/login")
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'User create successfully')
            return HttpResponseRedirect(reverse('user:get_all_users'))
        else:
            messages.error(request, 'something went wrong')
            return HttpResponseRedirect(reverse('user:get_all_users'))
    else:
        form = UserCreateForm()
    return render(request, 'admins/create_user.html', {'form': form})


@admin_required(login_url='/profile')
@login_required(login_url='/login')
def delete_user(request, username):
    user = User.objects.get(username=username)
    user.delete()
    messages.warning(request, 'User delete success')
    return HttpResponseRedirect(reverse('user:get_all_users'))


def reset_password(request, username):
    get_user = User.objects.get(username=username)

    if request.method == 'POST':
        form = UserUpdatePasswordForm(request.POST, request.FILES,
                                      instance=get_user)
        if form.is_valid():
            raw_password = form.cleaned_data['password1']
            filter_password = form.cleaned_data['password2']
            if raw_password != filter_password:
                messages.error(request, 'password did not match')
                return HttpResponseRedirect(reverse('user:reset_password',
                                                    kwargs={
                                                        'username':
                                                            get_user.username}
                                                    ))
            else:
                get_user.set_password(raw_password)
                get_user.save()
                form.save()
                messages.success(request, '''User {%get_user.username%}
                             password have been reset''')
                return HttpResponseRedirect(reverse('user:get_all_users'))
        else:
            messages.error(request, 'something went wrong')
            return HttpResponseRedirect(reverse('user:get_all_users'))
    else:
        form = UserUpdatePasswordForm(instance=get_user)
    return render(request, 'registration/reset-password-form.html',
                  {'form': form, 'user': get_user})


@login_required(login_url='/login')
@admin_required(login_url='/profile')
def ban_user(request, username):
    get_user = User.objects.get(username=username)
    get_user.is_active = False
    get_user.save()
    messages.error(request, 'the user has been ban')
    return HttpResponseRedirect(reverse('user:get_all_users'))


@login_required(login_url='/login')
@admin_required(login_url='/profile')
def unban_user(request, username):
    get_user = User.objects.get(username=username)
    get_user.is_active = True
    get_user.save()
    messages.warning(request, 'the user has ben unban')
    return HttpResponseRedirect(reverse('user:get_all_users'))
