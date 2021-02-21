import requests

# 打印nickname中元素
url_get_1='http://182.92.178.83:8081/admin/user?nickname='
headers_get_1={'Cookie': 'Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379245; studentUserName=student; remember-me=YWRtaW46MTU5ODk3MTMxNzQwMzozMzQ3ZjJjZDZjZTdiY2M5OGU0YWVkZDczY2U5MmUyMA; adminUserName=admin; JSESSIONID=0852F33E8AEC48B52587024A148C5DC2'}
result_get_1=requests.get(url=url_get_1,headers=headers_get_1)
print(type(result_get_1.json()))
print(result_get_1.json())



# url_get_1='http://182.92.178.83:8081/admin/user'
# headers_get_1={'Cookie':'Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379245; SESSION=YjliNzgyOTktMWI4OS00ZTk0LThkZjktZGY0MDk5ZmQ0Nzgy; studentUserName=student; remember-me=YWRtaW46MTU5ODk3MTMxNzQwMzozMzQ3ZjJjZDZjZTdiY2M5OGU0YWVkZDczY2U5MmUyMA; adminUserName=admin; Hm_lpvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379426; JSESSIONID=E9F188922035FED9305115D744F17104'}
# # params_get_1={'nickname':'乔'}
# # 打印指定nickname中含乔的元素
# result_get_1=requests.get(url=url_get_1,headers=headers_get_1)
# print(result_get_1.json())
# # 打印result_get_1.json中的email元素
# print(result_get_1.json()[0]['email'])

# url_get_1='http://182.92.178.83:8081/admin/user'
# params_get_1={'nickname':'乔'}
# headers_get_1={'Cookie':'Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379245; SESSION=YjliNzgyOTktMWI4OS00ZTk0LThkZjktZGY0MDk5ZmQ0Nzgy; studentUserName=student; remember-me=YWRtaW46MTU5ODk3MTMxNzQwMzozMzQ3ZjJjZDZjZTdiY2M5OGU0YWVkZDczY2U5MmUyMA; adminUserName=admin; Hm_lpvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379426; JSESSIONID=E9F188922035FED9305115D744F17104'}
# result_get_1=requests.get(url_get_1,headers=headers_get_1,params=params_get_1)
# print(result_get_1.json())
# print(result_get_1.json(),type(result_get_1.json()))
# print(result_get_1.url)
# print(result_get_1.text)


#
# url_get_1='http://182.92.178.83:8081/admin/user'
# params_get_1={'nickname':'sui'}
# nicknames=['乔','楚','陈','段']
# for nickname in nicknames:
#     params_get_1['nickname']=nickname
#     headers_get_1={'Cookie':'Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379245; SESSION=YjliNzgyOTktMWI4OS00ZTk0LThkZjktZGY0MDk5ZmQ0Nzgy; studentUserName=student; remember-me=YWRtaW46MTU5ODk3MTMxNzQwMzozMzQ3ZjJjZDZjZTdiY2M5OGU0YWVkZDczY2U5MmUyMA; adminUserName=admin; Hm_lpvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379426; JSESSIONID=E9F188922035FED9305115D744F17104'}
#     result_get_1=requests.get(url=url_get_1,headers=headers_get_1,params=params_get_1)
#     print(type(result_get_1.json()))
#     print(result_get_1.json())
#     rel_nick=result_get_1.json()[0]['nickname']
#     print(rel_nick)
#     if nickname in rel_nick:
#         print('pass,测试通过')
#         # 或者
#         print(rel_nick.find(nickname))
#     if rel_nick.find(nickname) >=0:
#         print('pass测试通过')

# # 绝对路径with open()

# url_get_1='http://182.92.178.83:8081/admin/user'
# params_get_1={'nickname':'sui'}
# # nicknames=['陈','楚','乔']
# with open(r'C:\Users\小Q\PycharmProjects\0626初试project\my_first-package\接口自动化\jiekou.csv','r',encoding='utf-8') as nicknames_file:
#     for line in nicknames_file:
#         nicknames=line.split(',')
#         print(nicknames)
#
# for nickname in nicknames:
#     params_get_1['nickname']=nickname
#     headers_get_1={'Cookie':'Hm_lvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379245; SESSION=YjliNzgyOTktMWI4OS00ZTk0LThkZjktZGY0MDk5ZmQ0Nzgy; studentUserName=student; remember-me=YWRtaW46MTU5ODk3MTMxNzQwMzozMzQ3ZjJjZDZjZTdiY2M5OGU0YWVkZDczY2U5MmUyMA; adminUserName=admin; Hm_lpvt_cd8218cd51f800ed2b73e5751cb3f4f9=1596379426; JSESSIONID=E9F188922035FED9305115D744F17104'}
#     result_get_1=requests.get(url=url_get_1,headers=headers_get_1,params=params_get_1)
#     rel_nick = result_get_1.json()[0]['nickname']
#     print(rel_nick)
#     # if nickname in rel_nick:
#     #     print('pass,测试通过')
#     #     # 或者
#     #     print(rel_nick.find(nickname))
#     if rel_nick.find(nickname) >= 0:
#         print('pass测试通过')
#     print(result_get_1.json())



# 超时限制try
# try:
#     result_get_1=requests.get(url='',headers=headers_get_1,params=params_get_1,timeout=0.01)
#     print(result_get_1.json())
#     print('没有异常，一遍过')
# except:
#     result_get_1=requests.get(url='',headers=headers_get_1,params=params_get_1,timeout=0.01)
#     print(result_get_1.json())
#     print('有异常，调整后过')
