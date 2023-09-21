from django.conf import settings
from django.utils import timezone
import datetime
from django.utils.deprecation import MiddlewareMixin
from .log import logger

class ViewExecutionTimeMiddleware2(MiddlewareMixin):
    def process_request(self,request):
        request.start_time = timezone.now()
        
    def process_response(self,request, response):
        total_time = timezone.now() - request.start_time
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        msg = f"EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"
        
        ok_time = datetime.timedelta(seconds = 0.05)         
        warning_time = datetime.timedelta(seconds = 1)
        
        if total_time < ok_time:
            logger.info(msg)
        elif total_time < warning_time:
            logger.warning(msg)
        else:
            logger.critical(msg)
        
        return response
    