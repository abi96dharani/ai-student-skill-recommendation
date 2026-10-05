from flask import Flask, request
import pandas as pd
import math
import os

app = Flask(__name__)

# =====================================================
# LOAD DATASET
# =====================================================

folder = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(
    folder,
    "dataset.csv"
)

data = pd.read_csv(dataset_path)

# =====================================================
# PREPARE AI MODEL
# =====================================================

X = data[
    [
        "Python",
        "Java",
        "C++",
        "Maths",
        "Communication"
    ]
]

y = data["Recommended_Skill"]

def predict_skill(student):

    python = student["Python"].iloc[0]
    java = student["Java"].iloc[0]
    cpp = student["C++"].iloc[0]
    maths = student["Maths"].iloc[0]
    communication = student["Communication"].iloc[0]

    if python >= 3 and maths >= 3:
        return "Machine Learning"

    elif python >= 3 and cpp >= 2:
        return "Advanced Python"

    elif maths >= 3 and communication >= 2:
        return "Data Science"

    else:
        return "Deep Learning"


print("Dataset loaded successfully")
print("AI Recommendation System ready")

# =====================================================
# ONLINE ASSESSMENT QUESTIONS
# =====================================================

questions = [

    {
        "subject": "Python",
        "question": "1. What is the output of print(2 + 3)?",
        "options": [
            "A. 4",
            "B. 5",
            "C. 6",
            "D. 23"
        ],
        "answer": "B"
    },

    {
        "subject": "Python",
        "question": "2. Which keyword is used to define a function in Python?",
        "options": [
            "A. function",
            "B. define",
            "C. def",
            "D. fun"
        ],
        "answer": "C"
    },

    {
        "subject": "Python",
        "question": "3. Which symbol is used to create a list in Python?",
        "options": [
            "A. ()",
            "B. {}",
            "C. []",
            "D. <>"
        ],
        "answer": "C"
    },

    {
        "subject": "Java",
        "question": "4. Which keyword is used to create a class in Java?",
        "options": [
            "A. class",
            "B. ClassName",
            "C. create",
            "D. object"
        ],
        "answer": "A"
    },

    {
        "subject": "Java",
        "question": "5. What is the correct main method in Java?",
        "options": [
            "A. public static void main(String[] args)",
            "B. public main()",
            "C. static main()",
            "D. void main()"
        ],
        "answer": "A"
    },

    {
        "subject": "Java",
        "question": "6. What is the output of System.out.println(10 / 2)?",
        "options": [
            "A. 2",
            "B. 5",
            "C. 10",
            "D. 20"
        ],
        "answer": "B"
    },

    {
        "subject": "C++",
        "question": "7. Which header file is commonly used for cout in C++?",
        "options": [
            "A. stdio.h",
            "B. iostream",
            "C. string.h",
            "D. math.h"
        ],
        "answer": "B"
    },

    {
        "subject": "C++",
        "question": "8. What is the output of cout << 2 + 3?",
        "options": [
            "A. 23",
            "B. 4",
            "C. 5",
            "D. 6"
        ],
        "answer": "C"
    },

    {
        "subject": "C++",
        "question": "9. Which keyword represents no return value in C++?",
        "options": [
            "A. null",
            "B. empty",
            "C. none",
            "D. void"
        ],
        "answer": "D"
    },

    {
        "subject": "Maths",
        "question": "10. What is 10% of 200?",
        "options": [
            "A. 10",
            "B. 20",
            "C. 30",
            "D. 40"
        ],
        "answer": "B"
    },

    {
        "subject": "Maths",
        "question": "11. What is the mean of 2, 4 and 6?",
        "options": [
            "A. 2",
            "B. 3",
            "C. 4",
            "D. 6"
        ],
        "answer": "C"
    },

    {
        "subject": "Maths",
        "question": "12. What is 3 squared?",
        "options": [
            "A. 6",
            "B. 9",
            "C. 12",
            "D. 15"
        ],
        "answer": "B"
    },

    {
        "subject": "Communication",
        "question": "13. Which is suitable for a professional email?",
        "options": [
            "A. Hey dude",
            "B. Dear Sir/Madam",
            "C. Yo",
            "D. What's up?"
        ],
        "answer": "B"
    },

    {
        "subject": "Communication",
        "question": "14. What does the word clarify mean?",
        "options": [
            "A. Make something clear",
            "B. Make something difficult",
            "C. Hide something",
            "D. Remove something"
        ],
        "answer": "A"
    },

    {
        "subject": "Communication",
        "question": "15. Which is important in an interview?",
        "options": [
            "A. Giving unrelated answers",
            "B. Speaking clearly and confidently",
            "C. Avoiding questions",
            "D. Not listening"
        ],
        "answer": "B"
    }
]
# =====================================================
# HOME PAGE
# =====================================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        # ---------------------------------------------
        # STUDENT DETAILS
        # ---------------------------------------------

        name = request.form.get("name")
        department = request.form.get("department")
        year = request.form.get("year")

        # ---------------------------------------------
        # SCORE VARIABLES
        # ---------------------------------------------

        subject_scores = {
            "Python": 0,
            "Java": 0,
            "C++": 0,
            "Maths": 0,
            "Communication": 0
        }

        subject_total = {
            "Python": 0,
            "Java": 0,
            "C++": 0,
            "Maths": 0,
            "Communication": 0
        }

        total_correct = 0

        # ---------------------------------------------
        # CHECK ANSWERS
        # ---------------------------------------------

        for index, question in enumerate(questions, start=1):

            subject = question["subject"]

            subject_total[subject] += 1

            user_answer = request.form.get(
                "q" + str(index)
            )

            if user_answer == question["answer"]:

                subject_scores[subject] += 1

                total_correct += 1

        # ---------------------------------------------
        # CALCULATE SUBJECT PERCENTAGE
        # ---------------------------------------------

        subject_percentage = {}

        for subject in subject_scores:

            percentage = (
                subject_scores[subject]
                / subject_total[subject]
            ) * 100

            subject_percentage[subject] = round(
                percentage
            )

        # ---------------------------------------------
        # OVERALL SCORE
        # ---------------------------------------------

        overall_score = round(
            (total_correct / len(questions)) * 100
        )

        # ---------------------------------------------
        # CONVERT SCORE TO AI LEVEL
        # ---------------------------------------------

        def get_level(score):

            if score < 40:
                return 1

            elif score < 70:
                return 2

            else:
                return 3

        python_level = get_level(
            subject_percentage["Python"]
        )

        java_level = get_level(
            subject_percentage["Java"]
        )

        cpp_level = get_level(
            subject_percentage["C++"]
        )

        maths_level = get_level(
            subject_percentage["Maths"]
        )

        communication_level = get_level(
            subject_percentage["Communication"]
        )

        # ---------------------------------------------
        # SEND AUTOMATIC SKILL LEVELS TO ML MODEL
        # ---------------------------------------------

        student = pd.DataFrame([{

            "Python": python_level,

            "Java": java_level,

            "C++": cpp_level,

            "Maths": maths_level,

            "Communication": communication_level

        }])

        # ---------------------------------------------
        # AI PREDICTION
        # ---------------------------------------------

        recommended = predict_skill(student)

        # ---------------------------------------------
        # STRONGEST AND WEAKEST SKILL
        # ---------------------------------------------

        strongest = max(
            subject_percentage,
            key=subject_percentage.get
        )

        improve = min(
            subject_percentage,
            key=subject_percentage.get
        )

        # ---------------------------------------------
        # IMPROVEMENT SUGGESTION
        # ---------------------------------------------

        if improve == "Python":

            suggestion = (
                "Practice Python basics, functions, "
                "OOP and small projects."
            )

        elif improve == "Java":

            suggestion = (
                "Practice Java programming, OOP concepts "
                "and problem solving."
            )

        elif improve == "C++":

            suggestion = (
                "Practice C++ syntax, OOP and "
                "data structures."
            )

        elif improve == "Maths":

            suggestion = (
                "Improve logical thinking, statistics "
                "and mathematical concepts."
            )

        else:

            suggestion = (
                "Practice communication, presentation "
                "and interview skills."
            )
            # ---------------------------------------------
        # AI RECOMMENDATION DETAILS
        # ---------------------------------------------

        if recommended == "Machine Learning":

            why = (
                "Your assessment performance shows a good "
                "foundation for Machine Learning."
            )

            priority = "HIGH"

            learning = (
                "Python → Pandas → NumPy → "
                "Scikit-learn → Machine Learning Projects"
            )

            career = (
                "Python → Data Handling → Machine Learning "
                "→ Projects → AI Engineer"
            )

        elif recommended == "Deep Learning":

            why = (
                "Your programming foundation can be "
                "developed further through Deep Learning."
            )

            priority = "HIGH"

            learning = (
                "Python → Machine Learning → "
                "Neural Networks → TensorFlow"
            )

            career = (
                "Python → ML → Deep Learning → "
                "AI Projects → AI Engineer"
            )

        elif recommended == "Data Science":

            why = (
                "Your programming and Maths assessment "
                "performance is useful for Data Science."
            )

            priority = "MEDIUM"

            learning = (
                "Python → Pandas → NumPy → "
                "Data Visualization → Data Science"
            )

            career = (
                "Python → Data Analysis → Data Science "
                "→ Projects → Data Scientist"
            )

        else:

            why = (
                "Improving your Python foundation will "
                "help you learn advanced programming."
            )

            priority = "MEDIUM"

            learning = (
                "Python Basics → Advanced Python → "
                "OOP → Problem Solving → Projects"
            )

            career = (
                "Python → Advanced Python → "
                "Projects → Software Developer"
            )


        # =============================================
        # RESULT HTML
        # =============================================

        result = f"""

        <div class="result">

            <h2>📊 Assessment Result</h2>

            <div class="student-info">

                <p>
                    <b>Student Name:</b> {name}
                </p>

                <p>
                    <b>Department:</b> {department}
                </p>

                <p>
                    <b>Year:</b> {year}
                </p>

            </div>


            <div class="score-box">

                <h2>🎯 Overall Assessment Score</h2>

                <div class="big-score">
                    {overall_score}%
                </div>

                <p>
                    Correct Answers:
                    <b>{total_correct}</b>
                    / {len(questions)}
                </p>

            </div>


            <h2>📚 Skill Analysis</h2>

            <div class="skills">

                <p>
                    🐍 Python:
                    <b>{subject_percentage["Python"]}%</b>
                </p>

                <p>
                    ☕ Java:
                    <b>{subject_percentage["Java"]}%</b>
                </p>

                <p>
                    💻 C++:
                    <b>{subject_percentage["C++"]}%</b>
                </p>

                <p>
                    📐 Maths:
                    <b>{subject_percentage["Maths"]}%</b>
                </p>

                <p>
                    🗣️ Communication:
                    <b>{subject_percentage["Communication"]}%</b>
                </p>

            </div>


            <div class="highlight">

                <h3>💪 Strongest Skill</h3>

                <p>
                    {strongest}
                </p>

            </div>


            <div class="improve">

                <h3>📈 Skill to Improve</h3>

                <p>
                    {improve}
                </p>

                <p>
                    {suggestion}
                </p>

            </div>


            <div class="recommendation">

                <h2>🤖 AI RECOMMENDATION</h2>

                <h1>
                    {recommended}
                </h1>

                <p>
                    {why}
                </p>

                <p>
                    <b>Learning Priority:</b>
                    {priority}
                </p>

            </div>


            <div class="learning">

                <h2>
                    🛣️ Personalized Learning Path
                </h2>

                <p>
                    {learning}
                </p>

            </div>


            <div class="career">

                <h2>
                    🚀 Career Roadmap
                </h2>

                <p>
                    {career}
                </p>

            </div>


            <div class="final">

                <h2>
                    💡 Final AI Suggestion
                </h2>

                <p>
                    Based on your online assessment
                    performance, the AI system analyzed
                    your skills and generated a
                    personalized learning recommendation.
                </p>

            </div>


            <h2 class="completed">
                ✅ ASSESSMENT COMPLETED
            </h2>

        </div>

        """
        # =================================================
    # HTML PAGE
    # =================================================

    html = f"""
<!DOCTYPE html>

<html>

<head>

    <title>AI Student Skill Assessment</title>

    <style>

        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(
                135deg,
                #667eea,
                #764ba2
            );
            margin: 0;
            padding: 30px;
        }}

        .container {{
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow:
                0 10px 30px
                rgba(0,0,0,0.25);
        }}

        h1 {{
            text-align: center;
            color: #333;
        }}

        .subtitle {{
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }}

        label {{
            font-weight: bold;
            display: block;
            margin-top: 15px;
            margin-bottom: 6px;
        }}

        input[type="text"],
        select {{
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-sizing: border-box;
        }}

        .question {{
            background: #f5f7ff;
            padding: 18px;
            margin-top: 20px;
            border-radius: 12px;
            border-left: 5px solid #667eea;
        }}

        .question-title {{
            font-weight: bold;
            margin-bottom: 12px;
        }}

        .option {{
            margin: 10px 0;
            font-weight: normal;
        }}

        .submit-btn {{
            width: 100%;
            padding: 15px;
            margin-top: 30px;
            border: none;
            border-radius: 10px;
            background: #667eea;
            color: white;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
        }}

        .submit-btn:hover {{
            background: #4f5edb;
        }}

        .result {{
            margin-top: 30px;
        }}

        .student-info,
        .score-box,
        .skills,
        .highlight,
        .improve,
        .recommendation,
        .learning,
        .career,
        .final {{
            padding: 20px;
            margin-top: 20px;
            border-radius: 15px;
        }}

        .student-info {{
            background: #eef2ff;
        }}

        .score-box {{
            text-align: center;
            background: #e8f8f5;
        }}

        .big-score {{
            font-size: 50px;
            font-weight: bold;
            color: #16a085;
        }}

        .skills {{
            background: #fff7e6;
        }}

        .highlight {{
            background: #e8f5e9;
        }}

        .improve {{
            background: #fff3e0;
        }}

        .recommendation {{
            text-align: center;
            background: #ede7f6;
        }}

        .recommendation h1 {{
            color: #673ab7;
        }}

        .learning {{
            background: #e3f2fd;
        }}

        .career {{
            background: #fce4ec;
        }}

        .final {{
            background: #e0f2f1;
        }}

        .completed {{
            text-align: center;
            color: #16a085;
            margin-top: 30px;
        }}

    </style>

</head>


<body>

<div class="container">

    <h1>
        🤖 AI-Based Student Skill Assessment
    </h1>

    <p class="subtitle">

        Online Assessment →
        Automatic Skill Analysis →
        AI Recommendation

    </p>


    <form method="POST">

        <h2>👨‍🎓 Student Details</h2>


        <label>Student Name</label>

        <input
            type="text"
            name="name"
            placeholder="Enter your name"
            required
        >


        <label>Department</label>

        <input
            type="text"
            name="department"
            placeholder="Enter your department"
            required
        >


        <label>Year</label>

        <select name="year" required>

            <option value="">
                Select Year
            </option>

            <option value="1st Year">
                1st Year
            </option>

            <option value="2nd Year">
                2nd Year
            </option>

            <option value="Final Year">
                Final Year
            </option>

        </select>


        <h2 style="margin-top:35px;">
            📝 Online Skill Assessment
        </h2>

        <p>
            Answer all questions. Your score will be
            automatically calculated by the system.
        </p>

"""

    # =================================================
    # DISPLAY ALL QUESTIONS
    # =================================================

    for index, question in enumerate(
        questions,
        start=1
    ):

        html += f"""

        <div class="question">

            <div class="question-title">

                {question["question"]}

            </div>

"""

        for option in question["options"]:

            letter = option[0]

            html += f"""

            <label class="option">

                <input
                    type="radio"
                    name="q{index}"
                    value="{letter}"
                    required
                >

                {option}

            </label>

"""

        html += """

        </div>

"""


    # =================================================
    # SUBMIT BUTTON
    # =================================================

    html += """

        <button
            type="submit"
            class="submit-btn"
        >

            🚀 Submit Assessment

        </button>

    </form>


"""


    # =================================================
    # SHOW RESULT
    # =================================================

    html += result


    html += """

</div>

</body>

</html>

"""


    return html


# =====================================================
# START FLASK APPLICATION
# =====================================================

if __name__ == "__main__":

    print("")
    print("==============================================")
    print("AI STUDENT SKILL ASSESSMENT SYSTEM")
    print("==============================================")
    print("Flask started successfully")
    print("Open: http://127.0.0.1:5002")
    print("")

    app.run(
        debug=False,
        use_reloader=False,
        port=5002
    )

