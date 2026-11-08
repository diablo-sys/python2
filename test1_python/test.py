import json

# 1. تحديد اسم ملف JSON الذي سيتم إنشاؤه
file_name = "data.json"

# 2. إنشاء البيانات التي نريد حفظها (عبارة عن Dictionary في بايثون)
user_data = {
    "name": "عمر",
    "age": 21,
    "skills": ["Python", "Networking", "Flutter"],
    "is_student": True
}

# --- الخطوة الأولى: إنشاء الملف وحفظ البيانات فيه (Write) ---
with open(file_name, "w", encoding="utf-8") as file:
    # indent=4 تجعل الملف مرتباً وسهل القراءة
    # ensure_ascii=False لتسهيل دعم اللغة العربية
    json.dump(user_data, file, indent=4, ensure_ascii=False)

print("✅ تم إنشاء ملف data.json وحفظ البيانات بنجاح!\n")

# --- الخطوة الثانية: قراءة البيانات واستقبالها من الملف (Read) ---
with open(file_name, "r", encoding="utf-8") as file:
    # قراءة وتفكيك محتوى JSON إلى متغير
    loaded_data = json.load(file)

# --- الخطوة الثالثة: طباعة واستخدام البيانات التي استقبلناها ---
print("📥 البيانات التي تم استقبالها من الملف:")
print(f"الاسم: {loaded_data['name']}")
print(f"العمر: {loaded_data['age']}")
print(f"المهارات: {', '.join(loaded_data['skills'])}")