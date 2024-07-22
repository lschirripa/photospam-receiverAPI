# photospam-receiverAPI

FastAPI application designed to receive HTTP requests from an ESP32-CAM every x seconds. The application stores the uploaded image files, which can be later used for real-time analysis and processing with AI.

API Endpoints
POST /upload
Endpoint to upload an image file.

- URL: /upload
- Method: POST
- Request Body: Raw image data
- Response:
  - 200 OK: When the file is successfully uploaded.
    
   ```bash
  {
    "message": "File uploaded successfully to ./uploads/image.jpg"
  }
   ```
   
  - 400 Bad Request: When no image data is provided.
   ```bash
  {
    "detail": "No image data provided"
  }
   ```

  - 500 Internal Server Error: When an error occurs while saving the file.
   ```bash
  {
    "detail": "Internal Server Error"
  }
   ```
