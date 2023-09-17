# from django.shortcuts import render
# from core_apps.obreplace_app.models import Movie
# from django.http import JsonResponse  # TODO using json_response


# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {'movies': list(movies.values())}

#     return JsonResponse(data, safe=False)


# def movie_details(request, pk):
#     movie_detail = Movie.objects.get(pk=pk)
#     data = {
#         'id': movie_detail.id,
#         'name': movie_detail.name,
#         'description': movie_detail.description,
#         'active': movie_detail.active
#     }

#     return JsonResponse(data, safe=False)
