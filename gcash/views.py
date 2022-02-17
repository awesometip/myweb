from django.shortcuts import render

#f = open("/workspace/django_container/static/gj.txt", 'r', encoding = 'cp949')
f = open("/static/gj.txt", 'r', encoding = 'cp949')
l=[]
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close()

data = l[1:2000]



def index(request):
    return render(request, 'gcash/gcash_main.html')

def detail(request):
    context = {'data' : data}
    return render(request, 'gcash/gcash_detail.html',context)
