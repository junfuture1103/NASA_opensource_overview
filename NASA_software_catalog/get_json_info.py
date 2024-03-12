import json

# 파일에서 JSON 데이터 로드
with open('catalog.json', 'r') as file:
    catalog_json = json.load(file)

# JSON에 총 몇 개의 item이 있는지
total_items = len(catalog_json)

# 카테고리별로 항목 수 및 소프트웨어 이름 추출
category_counts = {}
category_items = {}

for item in catalog_json:
    # for category in item['Categories']:
    for category in item['Categories_NLP']:
        if category not in category_counts:
            category_counts[category] = 0
            category_items[category] = []
        category_counts[category] += 1
        category_items[category].append(item['Software'])

# JSON에 중복되지 않는 몇 개의 category가 있는지
unique_categories = len(category_counts)

# 카테고리별로 가장 갯수가 많은 카테고리를 상위 10개 카테고리 이름만 출력
sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(f"Total items: {total_items}")
print(f"Unique categories: {unique_categories}")
print("Top 10 Categories by Number of Items:")
for category, count in sorted_categories:
    print(f"- {category} ({count} items)")
