from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import crime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CrimeAdmin(admin.ModelAdmin):
    list_display = ('crime_type', 'year')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.handle_upload_csv),]
        return new_urls + urls

    def handle_upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for line in csv_data:
                fields = line.split(",")
                # created = customer.objects.update_or_create(
                #     name = fields[0],
                #     balance = fields[1],
                #     )

            return HttpResponseRedirect("")

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(crime, CrimeAdmin)
