from rest_framework.decorators import api_view
from rest_framework.response import Response
from portfolio.models import PortfolioModel, AnyProblemsModel, ContactUsModel, AskedQuestionsModel, OurTeamModel, OurPartnersModel, PartnersLogoModel
from portfolio.api.serializer import PortfolioSerializer, AnyProblemsSerializer, ContactUsSerializer, AskedQuestionsSerializer, OurTeamSerializer, OurPartnersSerializer, PartnersLogoSerializer


@api_view(['GET', 'POST', ])
def portfolio_view(request):
    if request.method == 'GET':
        portfolio = PortfolioModel.objects.all()
        serializer = PortfolioSerializer(portfolio, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def any_problems_view(request):
    if request.method == 'GET':
        problems = AnyProblemsModel.objects.all()
        serializer = AnyProblemsSerializer(problems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnyProblemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def contact_us_view(request):
    if request.method == 'GET':
        problems = ContactUsModel.objects.all()
        serializer = ContactUsSerializer(problems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def asked_questions_view(request):
    if request.method == 'GET':
        problems = AskedQuestionsModel.objects.all()
        serializer = AskedQuestionsSerializer(problems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AskedQuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def our_team_view(request):
    if request.method == 'GET':
        problems = OurTeamModel.objects.all()
        serializer = OurTeamSerializer(problems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OurTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def partners_view(request):
    if request.method == 'GET':
        problems = OurPartnersModel.objects.all()
        serializer = OurPartnersSerializer(problems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OurPartnersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST', ])
def partners_logo_view(request):
    if request.method == 'GET':
        problems = PartnersLogoModel.objects.all()
        serializer = PartnersLogoSerializer(problems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PartnersLogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)