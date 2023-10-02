from django.db import models
# 웹사이트 본문에 해당하는 모델 정의
# 모델 수정 후 'python manage.py makemigrations' 입력
# 앱 처음 생성 시, setting.py에 앱 추가
# 'python manage.py migrate' : 실제 디비 모델에 적용
class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
