from warriors.models import Report, Soldier
from rest_framework.serializers import ModelSerializer


class ReportSerializer(ModelSerializer):
    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        instance = Report.objects.create(**validated_data)
        return instance

    class Meta:
        model = Report
        fields = '__all__'


class SoldierSerializer(ModelSerializer):
    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        instance = Soldier.objects.create(**validated_data)
        return instance

    class Meta:
        model = Soldier
        fields = '__all__'
