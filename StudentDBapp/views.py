import os
from django.http.response import Http404
from django.shortcuts import render
import csv
from datetime import datetime
# Create your views here.

def home(request):
    queryset = {}
    return render(request, "index.html",queryset)

def add(request):
    queryset = {}
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        dob = datetime.strptime(data['DateOfBirth'], '%Y-%m-%d')
        data['DateOfBirth'] = datetime.strftime(dob, '%d-%m-%Y')
        with open((os.path.dirname(os.path.realpath(__file__))) + '\students.csv', "a", newline='') as file:
            fieldnames = ['StudentId','Name','Gender','DateOfBirth','City','State','EmailId','Qualification','Stream']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            queryset['success'] = True
    return render(request, "add-student.html",queryset)

def search(request):
    results = list()
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        flag = False
        if data:
            with open((os.path.dirname(os.path.realpath(__file__))) + '\students.csv', "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    for key, value in zip(data.keys(), data.values()):          
                        if row[key] == value:
                            flag = True
                            results.append(row)  
        if flag==False:
            raise Http404                            
    return render(request, "search-student.html",{"results" : results})

def display(request):
    StudentList = list()
    with open((os.path.dirname(os.path.realpath(__file__))) + '\students.csv', "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            StudentList.append(row)
    return render(request, "display-student.html",{"StudentList" : StudentList})

