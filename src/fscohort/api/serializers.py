from rest_framework import serializers
from fscohort.models import Student, Course



class CourseSerializer(serializers.ModelSerializer):
    
    students = serializers.StringRelatedField(many=True)
    student_counts = serializers.SerializerMethodField()

    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # students = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="detail",
    #     lookup_field="id"
    # )

    class Meta:
        model = Course
        # fields = "__all__"
        fields = ["id", "title", "student_counts", "students"]   
        
    def get_student_counts(self, obj):        
        return obj.students.count()




class StudentSerializer(serializers.ModelSerializer):

    # course = CourseSerializer()     # bunu course tarafında yapmak için courseSe. clası bu clasın aşağısında olmalı
    course = serializers.StringRelatedField()    # read_only
    course_id = serializers.IntegerField()       # course_id yi ezdik yoksa strrelatedfield ile create edemiyorduk
    
    # course = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        # fields = ["id", "first_name", "last_name", "number", "course", "course_id", "student_course"]
        







#!-----------------------------------------


# class StudentSerializer(serializers.HyperlinkedModelSerializer):
    
#     # url = serializers.HyperlinkedIdentityField(
#     # view_name='detail',
#     # lookup_field='id'
#     # )
#     class Meta:
#         model = Student
#         fields = '__all__'
#         extra_kwargs = {
#             'url': {'view_name': 'detail', 'lookup_field': 'id'},
#         }
        
        
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'       
        