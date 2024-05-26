from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from pathlib import Path
import sys

MODULE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(MODULE_DIR))
from core import item, schedule


# Create your views here.

# global_items = [Item('apple', 5),
#                 Item('banana', 3),
#                 Item('tomato', 3)]

# items_cart = []
# total_target_price = None
# total_current_price = 0
scheduler = schedule.Scheduler(item.ItemCorpus())

def index(request):
    # return HttpResponse("Hello, world!\n <h1>This is add-on items!</h1>")
    # if 'items' not in request.session:
    #     request.session['items'] = []
    
    # request.session['items'].append(Item('apple', 5))
    # print('-' * 20)
    # print('global items:')
    # for item in request.session['items']:
    #     print(item)
    # print('-' * 20)

    # return render(request, 
    #               'addon_items/index.html',
    #               {
    #                 'items': request.session['items'],
    #                 'has_item': len(request.session['items']) > 0
    #               })

    #########################################################
    # items_cart
    # backup_items
    # target total price
    # current total price
    #########################################################
    backup_items = scheduler.recommend_items()
    item_cart = scheduler.item_cart
    target_total_price = scheduler.target_total_price
    current_total_price = scheduler.total_price

    return render(request,
                  'addon_items/index.html',
                  {
                    'item_cart': item_cart,
                    'backup_items': backup_items,
                    'has_backup_item': len(backup_items) > 0,
                    'target_total_price': target_total_price,
                    'current_total_price': current_total_price
                  })

@require_http_methods(['POST'])
def add(request):
    item_name = request.POST.get('item_name', '')
    item_price = request.POST.get('item_price', '')

    new_item = item.Item(item_name, float(item_price))
    scheduler.add_item(new_item)

    # log
    print('#' * 20)
    print(f"new item: {str(new_item)}")
    print('#' * 20)

    return HttpResponseRedirect(reverse("addon_items:index"))

@require_http_methods(['POST'])
def target(request):
    target_total_price = request.POST.get('target_price', '')
    scheduler.set_target_total_price(float(target_total_price))

    # log
    print('#' * 20)
    print(f'Target total price: {target_total_price}')
    print('#' * 20)

    return HttpResponseRedirect(reverse("addon_items:index"))

def greet(request, name):
    # return HttpResponse(f"<h1>Hello, {name}</h1>\n Welcome to <b>Add-on Items!</b>")
    return render(request,
                  'addon_items/welcome.html',
                  {
                      'name': name.capitalize()
                  })