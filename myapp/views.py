from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q

# Importing from rest_framework
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Data

# importing local serializer
from .serializers import DataSerializer

@login_required
def home(request):
    files = Data.objects.all()
    total_size = 0
    for file in files:
        file_size = file.file.size
        total_size += file_size
    file_size_gb = ((total_size/1024)/1024)/1024
    print(file_size_gb)
    total_file_size = round(file_size_gb, 3)
    print(total_file_size)
    storage_size = f"{total_file_size}"
    progress_percentage = total_file_size*100
    context = {
        "files":files,
        "storage":storage_size,
        "progress_bar":progress_percentage,
    }
    if file_size_gb >= 1:
            messages.error(request, f"You have exhausted 1 GB Space!!")
    else:
        print("You have memory left")
    if request.method == "POST":
        print(request.POST)
    return render(request, 'myapp/home.html', context)

@api_view(['GET', 'POST', 'DELETE'])
def files_list(request):    
    if request.method == "GET":
        files = Data.objects.all()
        serializer = DataSerializer(files, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=="POST":
        data = JSONParser().parse(request)
        serializer = DataSerializer(data=data)
        if serializer.is_valid():
            
            files = Data.objects.all()
            total_size = 0

            for file in files:
                file_size = file.file.size
                total_size += file_size
            file_size_gb = ((total_size/1024)/1024)/1024
            if file_size_gb >= 1:
                    messages.error(request, f"You have exhausted 1 GB Storage! To upload files please free up from space from this Storage.")
                    file = Data.objects.get(pk=request.data.file_id)
                    file.delete()
            else:
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def file_detail(request, pk):
    try: 
        file = Data.objects.get(pk=pk) 
    except Data.DoesNotExist: 
        return JsonResponse({'message': 'The file does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        data_serializer = DataSerializer(file) 
        return JsonResponse(data_serializer.data) 
 
    elif request.method == 'PUT': 
        file_data = JSONParser().parse(request) 
        file_serializer = DataSerializer(file, data=file_data) 
        if file_serializer.is_valid(): 
            file_serializer.save() 
            return JsonResponse(file_serializer.data) 
        return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        file.delete() 
        return JsonResponse({'message': 'File was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@login_required
def search(request):
    query = request.GET.get('q')
    object_list = Data.objects.filter(
        Q(file__icontains=query)
    )
    context = {
        "files":object_list,
        "query":query,
    }
    print(object_list)
    return render(request, 'myapp/search.html', context)