import json

# 파일에서 JSON 데이터 로드
with open('catalog.json', 'r') as file:
    catalogjson = json.load(file)

# 카테고리별로 항목 수 및 소프트웨어 이름 추출
category_counts = {}
category_items = {}

for item in catalogjson:
    for category in item['Categories_NLP']:
    # for category in item['Categories']:
        if category not in category_counts:
            category_counts[category] = 0
            category_items[category] = []
        category_counts[category] += 1
        category_items[category].append(item['Software'])

# 카테고리별 항목 수를 기준으로 정렬 (가장 많은 항목을 가진 카테고리 순)
sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)


# 결과를 'result.txt' 파일에 저장
with open('result.txt', 'w') as file:
    for category, count in sorted_categories:
        file.write(f"Category: {category}, Count: {count}\n")
        file.write("Items:\n")
        for item_name in category_items[category]:
            file.write(f"{item_name}\n")
        file.write("\n\n")