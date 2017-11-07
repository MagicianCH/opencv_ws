from aip import AipFace

APP_ID = "9865961"
API_KEY = "iM5PbNMlEAoYQOLj7jyRWwNK"
SECRET_KEY = "CLmVFow9bje90mqisNQQXVgonsPb4N34"

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()

option = {
    'max_face_num': 1,
    'face_fields': "age, beauty, expression, faceshape",
}

result = aipFace.detect(get_file_content('../img/paul1.jpg'), option)

print(result)
