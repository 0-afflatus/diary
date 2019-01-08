from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Event(models.Model):
    
    # Event Details
    title = models.CharField('title', max_length=255, default='')
    details = models.TextField('details', blank=True, default='', null=True)
    featured_img = models.ImageField(upload_to = 'uploads/', blank = True, help_text = "600 * 800 pixel image.")
    space = models.CharField('space', max_length=255, default="Hall") # convert to drop-down list
    is_public = models.BooleanField('public?', default=True)
    
    # Date / timings
    start_date = models.DateField('start date')
    end_date = models.DateField('end date', blank=True, null=True)
    getin_time = models.TimeField('get-in time', blank=True, null=True)
    setup_time = models.TimeField('set-up time', blank=True, null=True)
    open_time = models.TimeField('opening time', default='20:00:00')
    end_time = models.TimeField('closing time', default='00:00:00')
    is_weekly = models.BooleanField('weekly event?', default=False)

    # Pricing
    adv_price = models.DecimalField('advance price', max_digits=5, decimal_places=2, blank=True, null=True)
    door_price = models.DecimalField('door price', max_digits=5, decimal_places=2, blank=True, null=True)
    conc_price = models.DecimalField('concession price', max_digits=5, decimal_places=2, blank=True, null=True)
    ticket_link = models.CharField('ticket link', max_length=255, blank=True, null=True)
    
    # Charges
    total_fee = models.DecimalField('TOTAL fee', max_digits=5, decimal_places=2, blank=True, null=True)
    percentage = models.IntegerField('percentage of door', blank=True, null=True)
    deposit = models.DecimalField('advance fee', max_digits=5, decimal_places=2, blank=True, null=True)
    balance_due = models.DecimalField('balance due', max_digits=5, decimal_places=2, blank=True, null=True)
    deposit_date = models.DateField('deposit received', blank=True, null=True)
    balance_date = models.DateField('balance due date', blank=True, null=True)
    
    # Hirer contact details
    hirer_name = models.CharField('contact', max_length=255, blank=True, null=True)
    hirer_address = models.CharField('address', max_length=255, blank=True, null=True)
    hirer_postcode = models.CharField('postcode', max_length=255, blank=True, null=True)
    hirer_email = models.CharField('email', max_length=255, blank=True, null=True)
    hirer_phone = models.CharField('phone', max_length=255, blank=True, null=True)
    hirer_mobile = models.CharField('mobile', max_length=255, blank=True, null=True)
    
    # Housekeeping
    event_slug = models.SlugField (max_length=52, verbose_name="URL slug", help_text = 'URL friendly name; lowercase, numbers and underscores only.', blank=True, null=True)
    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', blank=True, null=True)
    owner = models.ForeignKey(User, verbose_name='owner',
        related_name='events', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ['start_date']

    def publish(self):
        self.date_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title
