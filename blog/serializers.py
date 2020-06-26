from rest_framework import serializers

class Result_Serializer(serializers.Serializer):
    edit1_model = serializers.CharField(max_length = 5)
    edit2_model = serializers.CharField(max_length = 5)
     
    edit_result_model = serializers.CharField(max_length = 5)
