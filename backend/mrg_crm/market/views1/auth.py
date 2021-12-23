# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import serializers, viewsets, permissions
# from drf_yasg.utils import swagger_auto_schema

# class CommonResponseSerializer(serializers.Serializer):
#     status = serializers.IntegerField()
#     message = serializers.CharField()

# class LoginRequestSerilizer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

# class AuthView(APIView):

#     """ 
#     User login
#     """
#     @swagger_auto_schema(
#         response = {200:CommonResponseSerializer},
#         request_body = LoginRequestSerilizer
#     )
#     def post(self, request):
#         return Response(CommonResponseSerializer({
#             'status':0,
#             'message':'Goood'
#         }))