import requests
from django import forms
from django.views.generic import FormView
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from .models import UploadedFile


class IndexForm(forms.Form):
    file = forms.FileField(label="PDF")


class IndexView(FormView):
    form_class = IndexForm
    template_name = "core/index.html"

    def form_valid(self, form):
        file = form.files['file']
        text = self.extract_text(file)

        UploadedFile.objects.create(file=file, text=text)

        return render(
            self.request,
            template_name=self.template_name,
            context={"text": text, "form": form},
        )

    def extract_text(self, file: InMemoryUploadedFile):
        response = requests.post(f"{settings.PDF_MINER_API_URL}/extract-pdf/", files={"file": file})
        response.raise_for_status()
        return response.json()["text"]
