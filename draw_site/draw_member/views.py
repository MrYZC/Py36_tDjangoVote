# Create your views here.
import random
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from .models import Member, History
from .forms import DrawForm

def home(request):
    form = DrawForm()
    return render(request, 'draw_member/home.html', {'form': form})

@require_GET
def draw(request):
    # Retrieve all related members
    form = DrawForm(request.GET)

    if form.is_valid():
        group_name = form.cleaned_data['group']
        if group_name == 'ALL':
            valid_members = Member.objects.all()
        else:
            valid_members = Member.objects.filter(group_name=group_name)
    else:
        # Raise 404 if no members are found given the group name
        raise Http404("No member in group '%s'" % form.data.get('group', ''))
    # Lucky draw
    lucky_member = random.choice(valid_members)
    # Update history
    draw_history = History(member=lucky_member)
    draw_history.save()

    return render(request, 'draw_member/draw.html', {'lucky_member': lucky_member})

def history(request):
    recent_draws = History.objects.order_by('-time').all()[:10]
    return render(request, 'draw_member/history.html', {'recent_histories': recent_draws})
