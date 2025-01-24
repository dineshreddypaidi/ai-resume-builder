from rest_framework import serializers
from users import models as usermodels


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = usermodels.CustomUser
        fields = [
            'username', 'email', 'name', 'contact_number',
            'github', 'linkedin', 'personal_site','password'
            ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = usermodels.CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        return super().update(instance, validated_data)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.CustomUser
        fields = [
            'id', 'username', 'name', 'contact_number', 'password',
            'email', 'github', 'linkedin', 'personal_site', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password') 
        user = usermodels.CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
  
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        return super().update(instance, validated_data)

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.Education
        fields = '__all__'
        
        read_only_fields = ['id']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.Experience
        fields = '__all__'
        
        read_only_fields = ['id']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.Project
        fields = '__all__'
        
        read_only_fields = ['id']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.Skill
        fields = '__all__'
        
        read_only_fields = ['id']


class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.JobDescription
        fields = [
            'id', 'user', 'description'
        ]
        read_only_fields = ['id']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.Resume
        fields = [
            'id', 'user', 'generated_file', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class SimilarityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodels.SimilarityScore
        fields = [
            'id', 'user', 'job_description', 'field', 'score'
        ]
        read_only_fields = ['id']
