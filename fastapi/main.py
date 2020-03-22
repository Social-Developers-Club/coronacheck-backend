from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/twitter_post/{url}")
def read_twitter(url: str, hash_tag: str =None):
    return {'url': url, 'hash_tag': hash_tag}



@app.get("/classification/")
def classification_result():
    return {'label': label, 'confidence': confidence}

@app.get("/evidence/")
def classification_result():
    return {'source_id': source_id, 'source_text': source_text}

@app.get("/classification/")
def classification_result():
    return {'hash_tag': hash_tag, 'geo': geo}
