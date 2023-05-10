#4.0 APPS
# models.py, settings.py, apps.py 참고

""" 
# terminal
: python manage.py startapp houses
migrations / __init__.py, admin.py, apps.py, models.py, tests.py, views.py는 django에서는 필수 파일이다.

# models.py
: 모델을 명시해주는 파일

# settings.py에 application 등록하기
: houses라는 directory에 apps.py 내부에 class HousesConfig의 경로를 settings.py에 아래와 같이 추가한다.
# INSTALLED_APPS = [ 'houses.apps.HousesConfig' ]로 작성해 추가한다.


# Models.py
models.Model
: Model Class를 상속받을 때 사용

models.CharField()
: 글자 수를 제한주고자 할 때

max_length=숫자
: 최대 글자 수

models.PositiveIntegerField()
: 양수인 정수로만 값을 받을 때

models.TextField()
: 긴 글자를 가질 때

"""