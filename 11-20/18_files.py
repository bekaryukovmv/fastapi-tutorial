"""
Чтобы получать form-data вместо JSON надо использовать Form
Для этого необходимо импортировать pip install python-multipart
"""
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


# File это класс, который напрямую наследуется от Form
# Так, содержимое файла будет прочитано как байты и будет храниться в памяти
@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# А так - после превышения определенного размера - файл будет сохраняться на диск.
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


"""
UploadFile имеет следующие атрибуты:
- filename
- content_type
- file

UploadFile имеет следующие async методы:
- write(data)
- read(size)
- seek(offset)
- close()
"""

# Загрузка нескольких файлов одновременно
@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
