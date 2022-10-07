from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from event_api.models import SalesTeam, SupportTeam, ManageTeam


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password','password2', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def log(self, log_error):
        raise serializers.ValidationError({'Exception': str(log_error)})


class UserMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class ManageTeamSerializer(serializers.ModelSerializer):

    user = User

    class Meta:
        model = ManageTeam
        fields = '__all__'


class ManageTeamDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = ManageTeam
        fields = '__all__'


class SalesTeamSerializer(serializers.ModelSerializer):

    user = User

    class Meta:
        model = SalesTeam
        fields = '__all__'


class SalesTeamDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = SalesTeam
        fields = '__all__'


class SupportTeamSerializer(serializers.ModelSerializer):

    user = ManageTeam

    class Meta:
        model = SupportTeam
        fields = '__all__'


class SupportTeamDetailSerializer(serializers.ModelSerializer):

    class EmbeddedManageTeamSerializer(serializers.ModelSerializer):

        user = UserMinimalSerializer()

        class Meta:
            model = ManageTeam
            fields = '__all__'


    user = EmbeddedManageTeamSerializer()

    class Meta:
        model = SupportTeam
        fields = '__all__'
