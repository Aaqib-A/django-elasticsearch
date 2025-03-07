
# Resources

[Youtube video](https://www.youtube.com/watch?v=lKanpfkhxv0)
|
[Github](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2024/05/18/Getting%20Started%20With%20Elasticsearch%20in%20Django%20-%20Faster%20Text%20Search%20for%20Your%20Apps)


# Setup

#### Install ElasticSearch
```
sudo docker-compose -f docker/docker-compose-es.yml up -d
```

#### Goto django folder
```
cd django_elasticsearch
```

#### Create Virtual Environment
```
python -m venv es-venv

# Mac/Linux:
source venv/bin/activate

# Windows:
.\es-venv\Scripts\activate.bat
```

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

#### - Migrate database
```
python manage.py migrate
python manage.py createsuperuser
```

#### - Run application
```
python manage.py runserver
```
