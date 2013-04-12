# -*- coding: utf-8 -*-
from django.db import models
from django.core.mail import send_mail
from django.conf import settings

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        settings.SEND_ALERT_EMAIL)

class Subscribe(models.Model):
    email = models.EmailField(verbose_name=u'мыло')
    time = models.DateTimeField(auto_now=True, verbose_name=u'время')
    from_page = models.CharField(max_length=255, verbose_name=u'со страницы')
    
    def save(self, *args, **kwargs):
        super(Subscribe, self).save(*args, **kwargs)
        subject=u'SVP8.ru: Новая подписка с сайта',
        body=u"%s со страницы %s"% (self.email, self.from_page)
        sendmail(subject, body)
    
    class Meta:
        verbose_name = u'подписка'
        verbose_name_plural = u'подписки'
        
    def __unicode__(self):
        return self.email