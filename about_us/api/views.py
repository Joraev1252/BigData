from rest_framework.decorators import api_view
from rest_framework.response import Response
from about_us.models import AboutUsModel, OurGeneralStatisticsModel, OurCoursesModel
from about_us.api.serializer import AboutUsSerializer, OurCoursesSerializer, OurGeneralStatisticsSerializer


@api_view(['GET', 'POST', ])
def about_us_view(request):
    if request.method == 'GET':
        about = AboutUsModel.objects.all()
        serializer = AboutUsSerializer(about, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def our_courses_view(request):
    if request.method == 'GET':
        courses = OurCoursesModel.objects.all()
        serializer = OurCoursesSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OurCoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def our_statics_view(request):
    if request.method == 'GET':
        courses = OurGeneralStatisticsModel.objects.all()
        serializer = OurGeneralStatisticsSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OurGeneralStatisticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)