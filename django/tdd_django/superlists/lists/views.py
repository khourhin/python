from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = 'You can not have an empty list item'        
        return render(request, 'home.html', {'error': error})
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))

