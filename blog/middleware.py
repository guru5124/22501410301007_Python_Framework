import datetime

class simpleloginmiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        now = datetime.datetime.now()
        print(f"Page Load Time : {now}")

        response = self.get_response(request)

        return response