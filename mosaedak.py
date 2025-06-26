import json
import os

def load_profile():
    if os.path.exists("profile.json"):
        with open("profile.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def load_faq():
    if os.path.exists("faq.json"):
        with open("faq.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_profile(profile):
    with open("profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

def save_faq(faq):
    with open("faq.json", "w", encoding="utf-8") as f:
        json.dump(faq, f, ensure_ascii=False, indent=2)

def onboarding():
    print("👋 أهلاً وسهلاً، أنا مساعدك الشخصي.
")

    name = input("1️⃣ تحب أقولك يا إيه؟
> ")
    role = input("2️⃣ تحب أساعدك في إيه؟
> ")
    welcome = input("3️⃣ تحب أقولك إيه كل مرة تفتحني؟
> ")

    profile = {
        "display_name": name,
        "role": role,
        "welcome_message": welcome
    }
    save_profile(profile)

    faq_list = []
    print("4️⃣ في أسئلة متكررة تحبني أرد عليها؟ (اكتب 'تم' للإنهاء)")
    while True:
        question = input("❓ السؤال:
> ")
        if question.strip().lower() == "تم":
            break
        answer = input("💬 الإجابة:
> ")
        faq_list.append({"question": question, "answer": answer})
    save_faq(faq_list)

    print(f"
✅ تم الحفظ، أنا في خدمتك يا {name}!")

def main():
    profile = load_profile()
    if profile:
        print(profile.get("welcome_message", "مرحبًا بك!"))
    else:
        onboarding()

if __name__ == "__main__":
    main()
