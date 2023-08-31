from rest_framework.response import Response
from rest_framework.decorators import api_view
from myappone.models import Movie
from myappone.api.serializers import MovieSerializer


# ---------------------------------------------------------------------------------------------------------------------
# by default: set for 'GET' request
# 'many=True' is used because of extracting more than one object

@api_view(['GET','POST'])                                                 
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)         
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# ---------------------------------------------------------------------------------------------------------------------
# by default: set for 'GET' request

@api_view()                                                 
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

    if request.method == 'PUT':
        movie= Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
            pass