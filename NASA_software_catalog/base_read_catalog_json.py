import json

# 파일에서 JSON 데이터 로드
with open('catalog.json', 'r') as file:
    catalogjson = json.load(file)

# 항목 개수 출력
print("Number of items in the catalog:", len(catalogjson))

# 첫 번째 항목의 데이터 출력 예시
first_item = catalogjson[0]
print("Update Date:", first_item["Update_Date"])
print("Description:", first_item["Description"])
print("Public Code Repo:", first_item["Public Code Repo"])
print("NASA Center:", first_item["NASA Center"])
print("Contributors:", first_item["Contributors"])
print("Labor Hours:", first_item["Labor_Hours"])
print("Categories:", first_item["Categories"])
print("Categories NLP:", first_item["Categories_NLP"])
print("Languages:", first_item["Languages"])
print("Software:", first_item["Software"])
print("License:", first_item["License"])
print("External Link:", first_item["External Link"])
