from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .ml_model import predict_image
from .models import Disease
from .models import Prediction



def upload_image(request):
    if request.method == "POST":
        image_file = request.FILES.get('image')
        if not image_file:
            return render(request, 'detector/upload.html', {'error': 'No image uploaded.'})
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_path = fs.path(filename)

        label, confidence = predict_image(image_path)

        label = label.replace("_", " ")  # optional
        disease = Disease.objects.filter(name__iexact=label).first()

        Prediction.objects.create(
            image=filename,
            disease=label,
            confidence=confidence
        )
        return render(request, 'detector/result.html', {
            'label': label,
            'confidence': round(confidence * 100, 2),
            'image_url': fs.url(filename),
            'disease': disease
        })

    return render(request, 'detector/upload.html')

def history(request):
    predictions = Prediction.objects.order_by('-created_at')
    return render(request, 'detector/history.html', {'predictions': predictions})
