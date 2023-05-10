#3.4 Framwork vs Library

# 날짜와 한글로 바꾸기
# : admin site -- users -- manju --important dates에 시간(UTC) → 한국시간으로 바꾸기

# project -- config -- settings.py 에서
# TIME_ZONE : 'UTC' → TIME_ZONE : 'Asia/Seoul'로 바꾸기
# LANGUAGE_CODE : 'ko'로 바꾸기

# config -- urls.py
# : admin/ 경로도 변경할 수 있다.