from django.db import models


class Contact(models.Model):
    """Saves a contact model in database."""

    class Meta:
        verbose_name_plural = 'Contact Form Submissions'

    first_name = models.CharField(
        max_length=50, null=False,
        blank=False)
    last_name = models.CharField(
        max_length=50, null=False,
        blank=False)
    email = models.EmailField(
        max_length=254, null=False,
        blank=False)
    phone_number = models.CharField(
        max_length=20, null=True,
        blank=True)
    subject = models.CharField(
        max_length=50, null=False,
        blank=False)
    your_message = models.TextField(
        max_length=1000, null=False,
        blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject