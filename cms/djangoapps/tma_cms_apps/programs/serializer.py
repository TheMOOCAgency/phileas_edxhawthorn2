from rest_framework import serializers



class ProgramSerializer(serializers.Serializer):

    is_manager_only = serializers.BooleanField()
    is_mandatory = serializers.BooleanField()
    is_linear = serializers.BooleanField()
    invitation_only = serializers.BooleanField()
    program_start_date = serializers.DateTimeField()
    program_due_date = serializers.DateTimeField()
    program_name = serializers.CharField(max_length=50)
    email_url = serializers.CharField(max_length=100)
    statistics_url = serializers.CharField(max_length=100)
    program_courses = serializers.CharField(max_length=1000)