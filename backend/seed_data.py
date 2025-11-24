# backend/seed_data.py
from database import SessionLocal, engine, Base
from models import Rule

def ensure_seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Clear existing rules before adding fresh ones
        db.query(Rule).delete()
        db.commit()

        # Add updated rules
        rules = [

            # ---------------------
            # BASIC BOT INTERACTIONS
            # ---------------------
            Rule(
                keywords="hi,hello,hey,hi bot,hello bot",
                response=(
                    "Hi! I’m a PCOD information chatbot. You can ask me about PCOD symptoms, "
                    "causes, periods, diet, lifestyle, myths, and when to see a doctor."
                ),
                priority=100,
            ),
            Rule(
                keywords="thank you,thanks,bye,goodbye,see you",
                response=(
                    "Thank you! I'm glad I could help. Take care of your health!"
                ),
                priority=99,
            ),

            # ---------------------
            # PCOD INFORMATION RULES
            # ---------------------

            Rule(
                keywords="what is pcod,what is pcod in simple words,pcod basic,pcod definition,pcod?,",
                response=(
                    "Polycystic Ovarian Disease (PCOD) is a hormonal condition where the "
                    "ovaries produce higher-than-usual levels of certain hormones and may "
                    "develop many small fluid-filled follicles. This can lead to irregular periods, "
                    "symptoms like acne or excess hair, and sometimes difficulty with ovulation. "
                    "It is a long-term condition, but with awareness and lifestyle changes, many women manage it well."
                ),
                priority=95,
            ),

            Rule(
                keywords="why does pcod occur,main reasons pcod,happen cause of pcod,pcod causes,reasons pcod,Causes & Reasons: Why does PCOD occur",
                response=(
                    "PCOD does not have a single cause. It usually develops from a combination "
                    "of factors such as genetic tendency, insulin resistance, hormonal imbalance, "
                    "and lifestyle factors like physical inactivity or unhealthy eating patterns."
                ),
                priority=94,
            ),

            Rule(
                keywords="common symptoms of pcod,what are symptoms of pcod,pcod symptoms,symptoms of pcod,Symptoms and Diagnosis",
                response=(
                    "Common symptoms include irregular or skipped periods, acne, excess hair "
                    "growth (hirsutism), hair thinning on the scalp, weight gain around the "
                    "abdomen, and darkening of skin folds. Some women also experience mood "
                    "changes, tiredness, or heavy/very light periods."
                ),
                priority=93,
            ),

            Rule(
                keywords="how does pcod affect menstrual cycle,pcod menstrual cycle,pcod periods,periods and pcod,Menstrual Cycle and Periods",
                response=(
                    "PCOD can disturb ovulation, leading to irregular or missed periods. Some may "
                    "have cycles that are very far apart, while others may have prolonged or heavy "
                    "bleeding. These changes happen because the hormones controlling ovulation are not balanced."
                ),
                priority=92,
            ),

            Rule(
                keywords="can women with pcod get pregnant naturally,pcod pregnancy,fertility and pcod,conceive with pcod,Fertility and Pregnancy",
                response=(
                    "Yes, many women with PCOD do conceive naturally. Healthy habits and proper "
                    "medical guidance can support ovulation. PCOD may delay pregnancy, but it does not mean pregnancy is impossible."
                ),
                priority=92,
            ),

            Rule(
                keywords="what diet for pcod,pcod diet,food choices for pcod,diet and pcod,what to eat pcod,Diet and Food Choices",
                response=(
                    "A balanced diet with vegetables, fruits, whole grains, lean proteins, and "
                    "healthy fats supports better hormone balance. Limiting refined carbs, sugary "
                    "drinks, and processed foods can improve insulin sensitivity. Consistency is more "
                    "important than following any strict or extreme diet."
                ),
                priority=91,
            ),

            Rule(
                keywords="how does exercise help pcod,exercise and pcod,physical activity pcod,workout pcod,Exercise and Physical Activity",
                response=(
                    "Regular exercise helps improve insulin sensitivity, support weight "
                    "management, balance hormones, and improve energy and mood. Even moderate "
                    "activity can help improve menstrual patterns and long-term health."
                ),
                priority=91,
            ),

            Rule(
                keywords="why is sleep important for pcod,pcod sleep,importance of sleep pcod,lifestyle habits pcod,stress and pcod,Lifestyle Habits",
                response=(
                    "Good sleep helps regulate hormones linked with appetite, stress, and "
                    "metabolism. Poor sleep can worsen insulin resistance and mood, making PCOD "
                    "symptoms harder to manage. Aim for 7–9 hours of consistent sleep daily."
                ),
                priority=90,
            ),

            Rule(
                keywords="why is weight management discussed in pcod,weight and pcod,metabolic health pcod,weight management pcod,Weight & Metabolic Health",
                response=(
                    "Many women with PCOD have insulin resistance, making weight gain more common. "
                    "Extra weight can worsen hormone imbalance. Managing weight, when needed, can "
                    "help improve periods, ovulation, and overall metabolic health."
                ),
                priority=90,
            ),

            Rule(
                keywords="is pcod caused by eating chocolates,sweets cause pcod,myths pcod,chocolate pcod,pcod myths facts,Myths & Facts",
                response=(
                    "No single food directly causes PCOD. However, eating a lot of sweets and sugary "
                    "drinks can worsen insulin resistance and weight gain, which may make symptoms "
                    "more noticeable. What matters most is overall diet quality and moderation."
                ),
                priority=89,
            ),
        ]

        db.add_all(rules)
        db.commit()

    finally:
        db.close()


def get_response(question):
    db = SessionLocal()
    try:
        rules = db.query(Rule).all()
        for rule in rules:
            keywords = rule.keywords.split(',')
            if any(keyword.lower() in question.lower() for keyword in keywords):
                return rule.response
        return "Sorry, I couldn't find an answer to your question. Please try rephrasing it."
    finally:
        db.close()


if __name__ == "__main__":
    ensure_seed()
    while True:
        question = input("Ask a question: ")
        if question.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        response = get_response(question)
        print(response)
