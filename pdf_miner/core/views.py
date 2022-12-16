import io
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from pdfminer.high_level import extract_text

class ExtractPDF(APIView):
    def post(self, request, *args, **kwargs):
        pdf_file = request.FILES.get('file')
        
        if not pdf_file:
            raise ValidationError("Missing a PDF file")

        text = extract_text(io.BytesIO(pdf_file.read()))
        return Response({"text": text})
