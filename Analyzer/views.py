import logging
from django.http import HttpResponse
from django.shortcuts import render
from kafka import KafkaConsumer
from kafka import TopicPartition
from django.shortcuts import render
from Analyzer.forms import TopicForm
from .twitter_handler import TwitterAccess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def index(request):
    form = TopicForm(request.POST)
    return render(request, 'Analyzer/topic.html', {'form': form})


# Create your views here.
def process(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            search_topic = form.cleaned_data['topic']
            TwitterAccess.get_stream(search_topic)
            return render(request, 'Analyzer/index.html')
    else:
        return HttpResponse("Only POST is supported")

    return HttpResponse("Error")


def get_coordinates(request, offset):
    consumer = KafkaConsumer()
    topic_partition = TopicPartition('Python', 0)
    consumer.assign([topic_partition])
    consumer.seek(partition=topic_partition, offset=int(offset))
    data = {}
    while not data:
        data = consumer.poll(timeout_ms=0, max_records=1)
    location = ''
    logger.debug(data)
    for k, v in data.items():
        location = str(v[0].value, 'utf-8')

    return HttpResponse(location)


def load_data(request):
    return render(request, 'Analyzer/dashboard.html')

