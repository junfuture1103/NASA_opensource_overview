import json

# 사용자가 검색하고 싶은 카테고리 지정
desired_category = "Data Servers Processing and Handling"

# 파일에서 JSON 데이터 로드
with open('catalog.json', 'r') as file:
    catalogjson = json.load(file)

# 해당 카테고리에 포함된 소프트웨어 찾기
matched_software = [item for item in catalogjson if desired_category in item["Categories"]]

# 결과 출력
print(f"Number of software in category '{desired_category}':", len(matched_software))

# 선택적으로, 해당 카테고리에 포함된 소프트웨어 목록 출력
for software in matched_software:
    print("Software:", software["Software"])
