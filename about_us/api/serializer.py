from rest_framework import serializers
from about_us.models import AboutUsModel, OurCoursesModel, OurGeneralStatisticsModel


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsModel
        fields = "__all__"


class OurCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurCoursesModel
        fields = "__all__"


class OurGeneralStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurGeneralStatisticsModel
        fields = "__all__"




