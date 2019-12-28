from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ttlru import TTLRU  #module for TTL

data=TTLRU(10000,ttl=300*1000000000)   #Create a dictionary Using TTLRU and set TTL 60*1000000000=1 minute
                                        #60*5=300*1000000000= 5 minute

#Get all the values of the store.
@api_view(['GET'])
def list(request):
    return Response(data,status=status.HTTP_200_OK)


@api_view(['GET'])
def with_keys(request,keys):  #Get one or more specific values from the store
    keys=keys.split(',')       #get all keys
    l={}                    #get a emty dictionary

    for key in keys:        #get single key from keys

        if key not in data.keys():  # if key not found found
            return Response({'message':'not found'},status=status.HTTP_204_NO_CONTENT)

        data.update({key: data[key]})   #date update with key, if we update then it will reset the TTL of those keys
        l[key]=data[key]                #add new items in 'l'

    return Response(l,status=status.HTTP_302_FOUND)


@api_view(['POST'])
def post(request):
    if request.method=='POST':
        for key,value in request.data.items():  # separate post data with key & value
            data[key]=value         #add new items in 'data' dictionary

        return Response(data,status=status.HTTP_201_CREATED)
    return Response(data,status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request):
    if request.method=="PUT":
        for key,value in request.data.items():  #get request updated data
            data.update({key: value})          #update data with key & value
        return Response(data,status=status.HTTP_205_RESET_CONTENT)
    return Response()

