from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass_url = ["/login/", "/captcha/"]

        if request.path_info in pass_url:
            return
        info_dict = request.session.get("info")
        if info_dict:
            return
        else:
            return redirect("/login/")

    def process_response(self, request, response):
        return response
