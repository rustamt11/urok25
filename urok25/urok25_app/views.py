from django.shortcuts import render
from datetime import datetime, timedelta

from django.shortcuts import render
from datetime import datetime, timedelta

def home(request):
    context = {
        'var1': None,
        'var2': False,
        'var3': 'Hello World',
        'some_date': datetime.now() - timedelta(days=5),
        'file_size': 123456,
        'long_string': 'This is a very very long string. It has many characters.',
        'number': 150,
        'slug_string': "This is a test slug!",
        'list_items': ['apple', 'banana', 'cherry'],
        'safe_string': "<strong>This is a strong tag</strong>",
        'digits': 123456789,
        'html_string': "<p>This is a paragraph.</p>",
    }
    return render(request, 'urok25_app/home.html', context)


