import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from nudenet import NudeDetector
import uuid
import os
from PIL import Image 

from utils.image_tools import split_image

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"code": 200, "message": "NO_ELO_API"}

BAN1 = [
    "FEMALE_GENITALIA_COVERED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_BREAST_EXPOSED",
    "ANUS_EXPOSED",
    "MALE_GENITALIA_EXPOSED", 
    "ANUS_COVERED",
]

detector = NudeDetector()
@app.post("/predict")
async def detect_nudity(file: UploadFile = File(...)):
    file_name = os.path.join("tmp", f"{uuid.uuid4()}-{file.filename}")
    with open(file_name, "wb") as f:
        f.write(file.file.read())
    res_list = []
    # 传入图片对象
    blocks = split_image(Image.open(file_name), 3, 3)
    # 检测每一块图片
    for index, block in enumerate(blocks):
        bf = os.path.join("tmp", f"blobk-{uuid.uuid4()}-{index}.jpg")
        if block.mode == "RGBA":
            block = block.convert("RGB")
        block.save(bf)
        result = detector.detect(bf)
        for res in result:
            if res["class"] in BAN1:
                res_list.append(res)
        os.remove(bf)
    os.remove(file_name)
    return res_list


if __name__ == "__main__":
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    uvicorn.run(app, host="127.0.0.1", port=2005)