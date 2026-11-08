import json

try:
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("📥 تم استقبال البيانات بنجاح من reader.py:")
    print(f"الاسم: {data.get('name', 'غير متوفر')}")
    
    # استخدام .get يحمي الكود من التوقف إذا كان المفتاح غير موجود
    print(f"الوظيفة: {data.get('role', 'لا توجد وظيفة مسجلة')}")
    
    # التعامل مع المهارات بأمان
    skills = data.get('skills', [])
    if skills:
        print(f"أول مهارة: {skills[0]}")
    else:
        print("لا توجد مهارات مسجلة")

except FileNotFoundError:
    print("❌ خطأ: ملف data.json غير موجود. قم تشغيل writer.py أولاً.")