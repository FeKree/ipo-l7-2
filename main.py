import json
file = 'dump.json'  
num = str(input("Введите ключ профессии для егр нахождения: "))
skills = False
with open(file, 'r', encoding='utf-8') as file:
    data = json.load(file)
    for skill in data:
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == num:
                sk_code = skill["fields"].get("code")
                sk_title = skill["fields"].get("title")
                skills = True

                for prof in data:
                    if prof.get("model") == "data.specialty":
                        sp_code = prof["fields"].get("code")
                        if sp_code in num:
                            sp_title = prof["fields"].get("title")
                            sp_educate = prof["fields"].get("c_type")
                            break
                break        
if not skills:
    print("-------------------- Не найдено ------------------------")
else:
    print("---------------------------------- Найдено ------------------------------------") 
    print(f"{sp_code} >> Специальность {sp_title} , {sp_educate}")
    print(f"{sk_code} >> Квалификация {sk_title}")               