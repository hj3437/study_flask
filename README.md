# study_flask
 
## 소개 
가게 메뉴를 표시해주는 웹 사이트입니다.  
python 웹 프레임워크 Flask를 사용하였습니다.


## 화면 및 기능 
### 가게 목록화면
웹 서버 시작후 로컬주소로 이동시 맨 처음으로 가게 목록화면이 보여집니다.  
가게 목록화면에서는 가게 추가, 가게 삭제 가게 변경을 할 수 있습니다.

### 가게 상세화면
가게를 클릭하면 상세화면으로 가게의 메뉴를 볼 수 있습니다.  
가게 목록화면과 유사하게 메뉴 삭제, 메뉴 추가, 메뉴 변경을 할 수 있습니다.

### 데이터 제공기능 
html, css, js를 제외한, 가게목록 및 메뉴 데이터가 필요한 제공합니다.   
Restful API 방식중에 하나인 JSON 방식으로 데이터를 제공합니다.


## 기술
DB: sqlite3  
ORM: sqlalchemy  
Python & Flask   
Template : Jinja  

## 이미지

### 목록 이미지
<img src="https://github.com/hj3437/study_flask/blob/main/captures/place_list.png?raw=true" width="100%" height="">

### 상세 이미지
<img src="https://github.com/hj3437/study_flask/blob/main/captures/store_list.png?raw=true" width="100%" height="">

### JSON
<img src="https://github.com/hj3437/study_flask/blob/main/captures/json_main.png?raw=true" width="300" height="300">
<img src="https://github.com/hj3437/study_flask/blob/main/captures/json_detail.png?raw=true" width="300" height="300">