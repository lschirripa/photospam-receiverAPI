from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.logger import logger
import os

app = FastAPI()

UPLOAD_DIRECTORY = "./uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@app.post("/upload")
async def upload_file(request: Request):
    try:
        # Read the raw image data from the request body
        image_data = await request.body()

        if not image_data:
            logger.error("No image data provided")
            raise HTTPException(status_code=400, detail="No image data provided")

        # Generate a unique filename
        file_location = os.path.join(UPLOAD_DIRECTORY, "image.jpg")
        with open(file_location, "wb") as buffer:
            buffer.write(image_data)
        logger.info(f"Saved file to {file_location}")

        return JSONResponse(content={"message": f"File uploaded successfully to {file_location}"})

    except Exception as e:
        logger.error(f"Error saving file: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
