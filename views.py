from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Event
from .forms import EventEditForm
from .decorators import user_is_author, user_is_creator

def event_list(request):
    events = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
    return render(request, 'diary/event_list.html', {'events': events})

def event_brief(request):
    events = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
    return render(request, 'diary/event_brief.html', {'events': events})

def event_detail(request, pk):
    event=get_object_or_404(Event, pk=pk)
    return render(request, 'diary/event_detail.html', {'event':event,})

def event_details_list(request):
    events = Event.objects.filter(is_weekly=False).filter(start_date__gte=timezone.now()).order_by('start_date')
    return render(request, 'diary/event_details_list.html', {'events': events})

def regulars_list(request):
    events = Event.objects.filter(is_weekly=True)
    return render(request, 'diary/event_details_list.html', {'events': events})

@user_is_creator
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventEditForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('event_view', pk=event.pk)
    else:
        form = EventEditForm(instance=event)
    return render(request, 'diary/event_edit.html', {'form': form, 'event':event})

@user_is_creator
def event_delete(request, *args, **kwargs):
    event = get_object_or_404(Event, pk=kwargs['pk'])

    if request.method == "POST":
        # Delete the event
        r_del = event.delete()
    
        #Return to Event list
        new_event = neweventForm()
        new_player = UserCreationForm()
        events = event.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        return redirect('/')

    # Show Confirmation dialog
    return render(request, 'diary/event_delete.html', {'event':event})
