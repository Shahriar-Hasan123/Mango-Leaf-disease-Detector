# Mango Leaf Disease Detection System

A Django-based web application that uses deep learning to detect and classify diseases in mango leaves. This system leverages a pre-trained deep learning model to identify various mango leaf diseases with high accuracy.

## Features

- **Disease Detection**: Upload mango leaf images to detect diseases using an AI model
- **Disease Classification**: Identifies 8 different mango leaf disease classes:
  - Anthracnose
  - Bacterial Canker
  - Cutting Weevil
  - Die Back
  - Gall Midge
  - Healthy
  - Powdery Mildew
  - Sooty Mould
- **Prediction History**: View past predictions and their confidence scores
- **Admin Dashboard**: Manage diseases and view prediction records
- **Web-based Interface**: Easy-to-use web UI for image uploads and results

## Tech Stack

- **Backend**: Django 6.0
- **Machine Learning**: TensorFlow/Keras
- **Database**: SQLite
- **Frontend**: HTML/CSS/JavaScript
- **Image Processing**: Pillow, OpenCV (via TensorFlow)

## Project Structure

```
Mango-Leaf-disease-Detector/
├── detector/                          # Main Django app
│   ├── migrations/                   # Database migrations
│   ├── templates/detector/           # HTML templates
│   ├── static/                       # Static files (CSS, JS)
│   ├── models.py                     # Database models (Disease, Prediction)
│   ├── views.py                      # View logic for upload and history
│   ├── ml_model.py                   # ML model loading and inference
│   ├── urls.py                       # URL routing
│   └── admin.py                      # Admin configuration
├── mango_leaf/                        # Django project settings
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Project URL configuration
│   ├── wsgi.py                       # WSGI configuration
│   └── asgi.py                       # ASGI configuration
├── media/                             # Uploaded images
├── static/                            # Static files
├── manage.py                          # Django management script
├── db.sqlite3                         # SQLite database
├── mango_leaf_disease_model.h5        # Pre-trained Keras model
└── requirements.txt                   # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Disease_Detection
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Web Interface: `http://localhost:8000`
   - Admin Panel: `http://localhost:8000/admin`

## Usage

### Uploading an Image for Disease Detection

1. Navigate to the home page (`http://localhost:8000`)
2. Click on the upload area or select an image file
3. Choose a mango leaf image (JPG, PNG, etc.)
4. Click "Upload" to analyze the image
5. View the prediction results including:
   - Detected disease name
   - Confidence score (0-1)
   - Disease description and treatment information

### Viewing Prediction History

1. Go to the "History" page (`http://localhost:8000/history`)
2. View all past predictions with:
   - Uploaded images
   - Disease classifications
   - Confidence scores
   - Upload timestamps

### Admin Panel

1. Access the admin panel at `http://localhost:8000/admin`
2. Log in with superuser credentials
3. Manage:
   - **Diseases**: Add/edit disease information with descriptions and treatments
   - **Predictions**: View and manage all prediction records

## Model Details

- **Model Type**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras
- **Input Size**: 224x224 pixels
- **Output**: 8 disease classes with confidence scores
- **File**: `mango_leaf_disease_model.h5`

## Dependencies

Key dependencies include:
- Django 6.0
- TensorFlow 2.20.0
- Keras 3.13.0
- NumPy 2.4.0
- Pillow 12.0.0
- h5py 3.15.1

See `requirements.txt` for the complete list.

## Database Models

### Disease Model
- `name` (CharField, unique)
- `description` (TextField)
- `treatment` (TextField)

### Prediction Model
- `image` (ImageField)
- `disease` (CharField)
- `confidence` (FloatField)
- `created_at` (DateTimeField, auto-set)

## API Endpoints

- `GET/POST /` - Upload image for disease detection
- `GET /history/` - View prediction history
- `GET /admin/` - Django admin panel

## Configuration

Edit `mango_leaf/settings.py` to configure:
- Database settings
- Allowed hosts
- Static/media file paths
- Debug mode

For production deployment, update `ALLOWED_HOSTS` and set `DEBUG = False`.

## Future Enhancements

- Real-time image preview before upload
- Batch image processing
- Export prediction reports
- Mobile app version
- Model performance metrics dashboard
- Multiple language support
- API endpoints for external integration

## Troubleshooting

**Model Not Found Error**:
Ensure `mango_leaf_disease_model.h5` is in the project root directory.

**Static Files Not Loading**:
Run `python manage.py collectstatic` for production.

**Database Issues**:
Delete `db.sqlite3` and run migrations again to reset the database.

## License

This project is provided as-is for educational and research purposes.

## Contributing

Contributions are welcome! Please feel free to:
- Report issues
- Submit pull requests
- Suggest improvements

## Contact

For questions or support, please contact the project maintainer.

---

**Note**: This is a demonstration project. For production use, ensure proper security configurations, model validation, and user input sanitization.
# Mango-Leaf-Disease-Detection
