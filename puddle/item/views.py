from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm
from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(batch_name=item.batch_name).exclude(pk=pk)[:5]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
# part ini digunakan untuk menambahkan data murid baru melalui site. merupakan bagian dari item/form.html & forms.py
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            student = form.save(commit=False)
            student.added_by = request.user
            student.save()

            return redirect('item:detail', pk=student.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Student'
    })
