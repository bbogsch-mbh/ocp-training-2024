OCP Training 2024

## Word Picker

To run the word-picker API:
```
cd word-picker
export FLASK_APP=word_picker.py
flask run
```

To build the Docker image:

```
docker build . -t word-picker:v*
```


To build the Docker image:

```
docker run -it --rm -p 5001:5000 -e OPTIONS_FILE=/tmp/missingfile.txt word-picker:v*
```