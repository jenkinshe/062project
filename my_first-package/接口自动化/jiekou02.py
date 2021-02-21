import requests
url_post_1='http://182.92.178.83:8081/login'
headers_post_1={'Cookie':'Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1603459843; SESSION=YjliNzgyOTktMWI4OS00ZTk0LThkZjktZGY0MDk5ZmQ0Nzgy; studentUserName=student; remember-me=YWRtaW46MTU5ODk3MTMxNzQwMzozMzQ3ZjJjZDZjZTdiY2M5OGU0YWVkZDczY2U5MmUyMA; adminUserName=admin; Hm_lpvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379426; JSESSIONID=E9F188922035FED9305115D744F17104'}
result_post_1=requests.post(url=url_post_1,headers=headers_post_1)
print(result_post_1.json())




