from django.shortcuts import render

def team(request):
    return render(request, 'about/team.html')

def members(request):
    startings = ['이상해씨', '파이리', '꼬부기']
    return render(request, 'about/members.html', {'startings': startings})