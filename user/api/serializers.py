from rest_framework import serializers

from ..models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        
        if not email:
            raise ValueError(_('Users must have Email'))
        if not first_name.isalpha():
            raise serializers.ValidationError('The firstname should contain alphabetic character only')
        if not last_name.isalpha():
            raise serializers.ValidationError('The lastname should contain alphabetic character only')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)