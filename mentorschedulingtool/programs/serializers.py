from rest_framework import serializers
from .models import Program

from sess.serializers import SessionSerializer
from sess.models import Session



# i can simplify JSON file to just id of sessions if required. Let me know
class ProgramSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    class Meta:
        model = Program
        fields = [
            'id',
            'program_name',
            'start_date',
            'end_date',
            'city',
            'program_type',
            'sessions'
        ]
        read_only_fields = ['id']

class ProgramDetailSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    mentors_assigned = serializers.ReadOnlyField()
    mentors_required = serializers.ReadOnlyField()
    class Meta:
        model = Program
        fields = [
            'id',
            'program_name',
            'start_date',
            'end_date',
            'city',
            'program_type',
            'mentors_required',
            'mentors_assigned',
            'sessions'
        ]
        read_only_fields = ['id']

# from rest_framework import serializers
# from .models import Program

# from sess.serializers import SessionSerializer
# from sess.models import Session

# class ProgramSerializer(serializers.ModelSerializer):
#     sessions = SessionSerializer(many=True, read_only=True)
#     total_mentors_required = serializers.ReadOnlyField()
#     total_mentors_assigned = serializers.ReadOnlyField()
#     class Meta:
#         model = Program
#         fields = [
#             'id',
#             'program_name',
#             'total_mentors_required',
#             'total_mentors_assigned',
#             'start_date',
#             'end_date',
#             'city',
#             'program_type',
#             'sessions'

#         ]
#         read_only_fields = ['id', 'total_mentors_required', 'total_mentors_assigned']

# class ProgramDetailSerializer(ProgramSerializer):
#     class Meta:
#         model = Program
#         fields = [
#             'id',
#             'program_name',
#             'total_junior_mentors_required',
#             'total_industry_mentors_required',
#             'total_lead_mentors_required',
#             'total_mentors_required',
#             'total_mentors_assigned',
#             'start_date',
#             'end_date',
#             'city',
#             'program_type',
#             'sessions'

#         ]
#         read_only_fields = ['id', 'total_mentors_required', 'total_mentors_assigned', 'total_junior_mentors_required', 'total_industry_mentors_required', 'total_lead_mentors_required']