from django.db import models

class Poll(models.Model):
    status_code = models.CharField(max_length=120)
    response_time = models.CharField(max_length=120)
    run_timedate = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.status_code
