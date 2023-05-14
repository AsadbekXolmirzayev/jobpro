from rest_framework import response, generics, views
from account.utils import SendEmail


class ConsultViewSet(views.APIView):

    def post(self, request, *args, **kwargs):
        for i in self.request.data['email']:
            data = {
                "email": i,
                "subject": 'Asadbek',
                "body": 'Hello'
            }
            SendEmail.send_email(data)
        return response.Response('as')
