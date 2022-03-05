from django.shortcuts import render,redirect
from .models import Profile, Dweet
from .forms import DweetForm
# Create your views here.


def dashboard(request):
    form = DweetForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("/")
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("created_at")

    
    return render(request, 'dashboard.html', {"form": form,"dweets": followed_dweets})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, "profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "profile.html", {"profile": profile})
