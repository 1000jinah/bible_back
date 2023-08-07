from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from bible_data import bible_data

app = FastAPI()

# CORS 설정 (React 개발 서버와 통신을 위해 필요)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # React 개발 서버의 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/bible_data", response_model=list[dict])
async def get_bible_data(
    chapter: int = Query(None),
    paragraph: int = Query(None),
    sentence: str = Query(None),
    long_label: str = Query(None),
):
    filtered_data = bible_data

    if long_label  is not None:
        filtered_data = [item for item in filtered_data if  item["long_label"] == long_label]

    if chapter is not None:
        filtered_data = [item for item in filtered_data if item["chapter"] == chapter]

    if paragraph is not None:
        filtered_data = [item for item in filtered_data if item["paragraph"] == paragraph]

    if sentence:
        filtered_data = [item for item in filtered_data if sentence in item["sentence"]]


    return filtered_data
