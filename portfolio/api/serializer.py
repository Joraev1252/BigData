from rest_framework import serializers
from portfolio.models import PortfolioModel, ContactUsModel, AnyProblemsModel, AskedQuestionsModel, OurTeamModel, OurPartnersModel, PartnersLogoModel


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioModel
        fields = "__all__"


class AnyProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnyProblemsModel
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = "__all__"


class AskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskedQuestionsModel
        fields = "__all__"


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeamModel
        fields = "__all__"


class OurPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPartnersModel
        fields = "__all__"


class PartnersLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersLogoModel
        fields = "__all__"





