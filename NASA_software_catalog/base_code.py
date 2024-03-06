import requests

# NASA Technology Transfer API의 소프트웨어 쿼리 URL 예시
url = "http://technology.nasa.gov/api/query/software/visualization"

# API 요청을 보내고 응답 받기
response = requests.get(url)

# 응답이 성공적인지 확인
if response.status_code == 200:
    # 응답에서 JSON 데이터 추출
    data = response.json()
    
    # 결과 출력
    print("Results Found:", data['total'])
    for result in data['results']:
        print("Hash:", result[0])
        print("SWCode:", result[1])
        print("Name:", result[2])
        print("Category:", result[5])
        print("SW Type:", result[6])
        print() # for \n
        print("Description:", result[3])
        # print("SWCode:", result[4])
        print("-------")
else:
    print("Failed to retrieve data, status code:", response.status_code)
