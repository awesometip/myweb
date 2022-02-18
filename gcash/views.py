from django.shortcuts import render

f = open("/srv/myweb/static/g.txt", 'r', encoding = 'cp949')
#f = open("/workspace/django_container/static/g.txt", 'r', encoding = 'cp949')
l=[]
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close()

data = l[1:500]



def index(request):
    return render(request, 'gcash/gcash_main.html')

def detail(request):
    context = {'data' : data}
    return render(request, 'gcash/gcash_detail.html',context)

def detailtest(request):
    context = {'data' : data}
    return render(request, 'gcash/gcash_detailtest.html',context)
