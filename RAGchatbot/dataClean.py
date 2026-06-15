import re
import json

INPUT = "부서별업무현황.txt"
OUTPUT = "department_tasks.json"

PHONE = r'0\d{1,2}-\d{3,4}-\d{4}'

with open(INPUT, encoding="utf-8") as f:
    lines = [
        x.rstrip()
        for x in f.readlines()
        if x.strip()
    ]

results = []

current = None

for line in lines:

    cols = [c.strip() for c in line.split("\t") if c.strip()]

    if not cols:
        continue

    phone = re.search(PHONE, line)

    # 새 담당 시작 조건
    # (탭 2개 이상 + 전화번호 포함)
    if len(cols) >= 3 and phone:

        if current:
            results.append(current)

        department = cols[0]
        role = cols[1]

        department_name = (
            f"{department} {role}"
        )

        task = cols[2]

        task = (
            task
            .replace("-", "")
            .replace("·", "")
            .strip()
        )

        current = {
            "department": department_name,
            "tasks": [],
            "phone": phone.group()
        }

        if task:
            current["tasks"].append(task)

        continue

    # 이어지는 업무
    if current:

        clean = (
            line
            .replace("-", "")
            .replace("·", "")
            .strip()
        )

        clean = re.sub(
            PHONE,
            "",
            clean
        ).strip()

        if clean:
            current["tasks"].append(clean)

# 마지막 저장
if current:
    results.append(current)

# 후처리
for item in results:

    item["tasks"] = [
        x
        for x in item["tasks"]
        if x
    ]

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results,
        f,
        ensure_ascii=False,
        indent=2
    )

print(
    f"{len(results)}건 저장 완료"
)