from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm


def index(request):
    """Homepage for Learning Log app"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Display all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Display single topic and all attached posts"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # no data, create empty form
        form = TopicForm()
    else:
        # POST data added, need conversion
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # display empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add new entry for a certain topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data, create empty form
        form = EntryForm()
    else:
        # POST data added, need conversion
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # display empty form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
