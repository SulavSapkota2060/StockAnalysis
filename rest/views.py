from django.shortcuts import render, redirect
from .serializers import TodoSerializer, StockSerializer, StatSerializer
from .models import Todo, Just, UpStat, Stocks
from .scraper import scraper
import json
import pickle

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def allTodos(request):
 
    tasks= Todo.objects.all().order_by('-id')

    serializer = TodoSerializer(tasks, many= True)
 
    
    return Response(serializer.data)
    


@api_view(['POST'])
def createTodo(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateTodo(request,pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance = task,data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTodo(request,pk):
    task= Todo.objects.get(id=pk)

    task.delete()

    return redirect("All Todos")


@api_view(['GET'])
def stock_list(request):
    status = UpStat.objects.all()[0]
    stocks = Stocks.objects.all()
    jsonList = []
    file = 'todayData.pkl'
    if (status.stat == True):
        for i in stocks:
            x,y  = scraper(i.name)
            x = json.dumps(x)
            y = json.dumps(y)
            company = json.dumps(i.name)
            dic = '{' +'"name":' +company + ","+ '"details":' +'{' +'"date":' +str(y) +', "price": '+str(x)+'} }' 
            print(dic)
            dica = json.loads(dic)
            jsonList.append(dica)

        
        fileobj = open('todayData.pkl','wb')
        pickle.dump(jsonList,fileobj)
        fileobj.close()
        print('Pickled Created')
        
    else:
        fileobj = open('todayData.pkl','rb')
        jsonList = pickle.load(fileobj)
        print('Pickle Loaded')
    return Response(jsonList)



@api_view(['POST','GET'])
def upStatus(request):
    status = UpStat.objects.all()[0]

    ser = StatSerializer(status)

    return Response(ser.data)



@api_view(['POST'])
def updateStatus(request):
    status = UpStat.objects.get(id=1)
    serializer = StatSerializer(instance = status,data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)









# EXTRA FUNCTIONS:

