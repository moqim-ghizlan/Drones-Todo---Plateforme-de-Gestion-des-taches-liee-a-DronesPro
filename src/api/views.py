from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Todo_serialized
from base.models import Todo



@api_view(['POST'])
def create(request):
    data = request.data
    try:
        todo = Todo.objects.create(
        created_by = request.user,
        title = data['title'],
        description = data['description'],
        )
        serialized = Todo_serialized(todo, many=False)
        return Response({
            'code' : 1,
            'message' : 'Todo created successfully',
            'data' : serialized.data
        })
    except:
        return Response({
            'code' : 0,
            'message' : 'Todo creation failed',
            'data' : {}
        })

@api_view(['GET'])
def get_all(request):
    todos = Todo.objects.filter(created_by=request.user)
    serialized = Todo_serialized(todos, many=True)
    return Response({
        'code' : 1,
        'message' : 'Todos fetched successfully',
        'data' : serialized.data,
        'data_count' : todos.count()
    })


@api_view(['POST'])
def delete(request, id):
    todo = Todo.objects.get(id=id)
    if not todo:
        return Response({
            'code' : 0,
            'message' : 'Todo not found',
        })
    todo.delete()
    return Response({
        'code' : 1,
        'message' : 'Todo deleted successfully',
        'data' : {}
    })


@api_view(['POST'])
def update(request, id):
    todo = Todo.objects.get(id=id)
    if not todo:
        return Response({
            'code' : 0,
            'message' : 'Todo not found',
        })
    data = request.data
    todo.title = data['title']
    todo.description = data['description']
    todo.save()
    serialized = Todo_serialized(todo, many=False)
    return Response({
        'code' : 1,
        'message' : 'Todo updated successfully',
        'data' : serialized.data
    })


@api_view(['POST'])
def complete(request, id):
    todo = Todo.objects.get(id=id)
    if not todo:
        return Response({
            'code' : 0,
            'message' : 'Todo not found',
        })
    todo.set_completed()
    return Response({
        'code' : 1,
        'message' : 'Todo completed successfully',
        'data' : {}
    })


@api_view(['POST'])
def pending(request, id):
    todo = Todo.objects.get(id=id)
    if not todo:
        return Response({
            'code' : 0,
            'message' : 'Todo not found',
        })
    todo.set_incomplete()
    return Response({
        'code' : 1,
        'message' : 'Todo marked pending successfully',
        'data' : {}
    })



