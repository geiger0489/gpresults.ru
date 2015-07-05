# -*- coding:utf-8 -*-

from django.db import models

class Tender(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    href = models.CharField(max_length=200)
    purchase_number = models.CharField(max_length=200)
    purchase_name = models.TextField()
    gpb_id = models.CharField(max_length=200)
    gpb_is_answer = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()
    date_announce_results = models.DateField()
    purchase_type_id = models.CharField(max_length=200)
    purchase_type_header= models.CharField(max_length=200)
    purchase_subject_type_id = models.CharField(max_length=200)
    purchase_subject_type_header = models.CharField(max_length=200)
    purchase_subject_type_parent_id = models.CharField(max_length=200)
    purchase_subject_type_parent_header = models.CharField(max_length=200)
    new_type_of_procurements_id = models.CharField(max_length=200)
    new_type_of_procurements_header = models.CharField(max_length=200)
    new_type_of_procurements_parent_id = models.CharField(max_length=200)
    new_type_of_procurements_parent_header = models.CharField(max_length=200)
    company_org_id = models.IntegerField()
    company_org_name_full = models.CharField(max_length=200)
    company_customer_id = models.CharField(max_length=200)
    company_customer_name_full = models.CharField(max_length=200)

    def __str__(self):
        return 'Tender %s, id %s' % (purchase_number, id)
    