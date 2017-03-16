import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Place
from .forms import NewPlaceForm, UpdatePlaceForm


def place_list(request):

    # If a POST request, this must be from user clicking Add button
    # in the form. Check if new place is valid and add to list, then
    # redirect to 'place_list' route - which ends up creating a GET
    # request for this same method.
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            place = form.save()
            place.save()
            return redirect('place_list')

    # If not a POST request, or the form is not valid, display the page
    # with the form, and place list
    # places = Place.objects.filter(visited=False)
    places = Place.objects.all()
    form = NewPlaceForm()
    return render(request,
                  'travel_wishlist/wishlist.html',
                  {'places': places, 'form': form})


# def places_visited(request):
#     visited = Place.objects.filter(visited=True)
#     return render(request, 'travel_wishlist/visited.html', {'visited': visited})


# def place_is_visited(request):
#
#     if request.method == 'POST':
#         pk = request.POST.get('pk')
#         place = get_object_or_404(Place, pk=pk)
#         place.visited = True
#         place.save()
#
#     return redirect('place_list')


def place_detail(request, pk):

    place = get_object_or_404(Place, pk=pk)

    # This means we have submitted details to make an unvisited place visited
    if request.method == "POST":
        form = UpdatePlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            # Any other post logic goes here
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = UpdatePlaceForm(instance=place)
        if form:
            print("FORM")

    return render(request,
                  'travel_wishlist/place_detail.html',
                  {'place': place, 'form': form},
                  )
