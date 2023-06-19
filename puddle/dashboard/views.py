from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item, Category


@login_required
def index(request):
    batch_names = Category.objects.all()
    selected_batch = request.GET.get('batch_name_id', '')
    print(selected_batch)

    if selected_batch:
        selected_batch_name = get_object_or_404(Category, id=selected_batch).name
        items = Item.objects.filter(batch_name_id=selected_batch)
    else:
        selected_batch_name = None
        items = Item.objects.all()

    context = {
        'batch_names': batch_names,
        'items': items,
        'selected_batch': selected_batch,
        'selected_batch_name': selected_batch_name,
    }
    return render(request, 'dashboard/index.html', context)
