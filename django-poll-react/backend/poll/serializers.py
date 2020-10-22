from rest_framework import serializers

from .models import Poll

class PollSerializer(serializers.ModelSerializer):
    run_timedate = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'status_code', 'response_time', 'run_timedate')
