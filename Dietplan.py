from tkinter import *
from random import randint
import pickle

# Load ML model
model = pickle.load(open("diet_model.pkl", "rb"))

a = Tk()
a.title("AI Dietician")
a.configure(bg="#eaf4ff")

# ---------- VARIABLES ----------
v3 = StringVar()  # weight
v4 = StringVar()  # height
v5 = StringVar()  # age

# ---------- FUNCTION ----------
def generate_plan():

    protein = ['Yogurt','Cooked meat','Cooked fish','Egg whites','Tofu']
    fruit = ['Apple','Orange','Banana','Berries','Dry fruits','Juice']
    vegetable = ['Vegetables']
    grains = ['Rice','Brown bread','Potato','Oats','Corn']
    ps = ['Soy nuts','Milk','Hummus','Cottage cheese','Yogurt']

    w = float(v3.get())
    h = float(v4.get())
    age = float(v5.get())
    act = str(activity_list.get(ACTIVE))
    gender = gender_list.get(ACTIVE)

    gender_val = 1 if gender == "Male" else 0

    activity_map = {
        'Sedentary (little or no exercise)': 1.2,
        'Lightly active (1-3 days/week)': 1.375,
        'Moderately active (3-5 days/week)': 1.55,
        'Very active (6-7 days/week)': 1.725,
        'Super active (twice/day)': 1.9
    }

    act_val = activity_map[act]

    cal = model.predict([[w, h, age, gender_val, act_val]])[0]
    bmi = w / ((h/100)**2)

    if bmi < 18.5:
        goal = "Weight Gain"
        cal += 300
    elif bmi < 25:
        goal = "Maintain"
    elif bmi < 30:
        goal = "Fat Loss"
        cal -= 300
    else:
        goal = "Aggressive Fat Loss"
        cal -= 500

    protein_g = (cal * 0.3) / 4
    carb_g = (cal * 0.4) / 4
    fat_g = (cal * 0.3) / 9

    result_text = f"""
Goal: {goal}
BMI: {bmi:.1f}
Calories Needed: {int(cal)} kcal

Protein: {int(protein_g)} g
Carbs: {int(carb_g)} g
Fats: {int(fat_g)} g

Breakfast: {protein[randint(0,4)]} + {fruit[randint(0,5)]}
Lunch: {protein[randint(0,4)]} + {vegetable[0]} + {grains[randint(0,4)]}
Snack: {ps[randint(0,4)]}
Dinner: {protein[randint(0,4)]} + {vegetable[0]} + {grains[randint(0,4)]}
"""
    result_label.config(text=result_text)

# ---------- TITLE ----------
title = Label(a, text="AI Personalized Diet Planner",
              font=("Helvetica", 22, "bold"),
              bg="#eaf4ff", fg="#1f4e79")
title.grid(row=0, column=0, columnspan=2, pady=20)

# ---------- INPUT FRAME ----------
input_frame = Frame(a, bg="white", bd=2, relief=RIDGE, padx=15, pady=15)
input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")

Label(input_frame, text="Gender", font=("Arial", 11, "bold"), bg="white").grid(row=0, column=0, sticky="w")
Label(input_frame, text="Weight (kg)", font=("Arial", 11, "bold"), bg="white").grid(row=1, column=0, sticky="w")
Label(input_frame, text="Height (cm)", font=("Arial", 11, "bold"), bg="white").grid(row=2, column=0, sticky="w")
Label(input_frame, text="Age", font=("Arial", 11, "bold"), bg="white").grid(row=3, column=0, sticky="w")
Label(input_frame, text="Activity", font=("Arial", 11, "bold"), bg="white").grid(row=4, column=0, sticky="w")

Entry(input_frame, textvariable=v3, font=("Arial", 11)).grid(row=1, column=1, pady=5)
Entry(input_frame, textvariable=v4, font=("Arial", 11)).grid(row=2, column=1, pady=5)
Entry(input_frame, textvariable=v5, font=("Arial", 11)).grid(row=3, column=1, pady=5)

gender_list = Listbox(input_frame, height=2, width=18, font=("Arial", 10))
gender_list.insert(1,'Male')
gender_list.insert(2,'Female')
gender_list.grid(row=0, column=1, pady=5)

activity_list = Listbox(input_frame, height=5, width=35, font=("Arial", 10))
activity_list.insert(1,'Sedentary (little or no exercise)')
activity_list.insert(2,'Lightly active (1-3 days/week)')
activity_list.insert(3,'Moderately active (3-5 days/week)')
activity_list.insert(4,'Very active (6-7 days/week)')
activity_list.insert(5,'Super active (twice/day)')
activity_list.grid(row=4, column=1, pady=5)




# ---------- BUTTON ----------
generate_btn = Button(a, text="Generate AI Diet Plan",
                      font=("Arial", 12, "bold"),
                      bg="#1f4e79", fg="white",
                      activebackground="#163d5c",
                      activeforeground="white",
                      padx=15, pady=8, bd=0,
                      cursor="hand2",
                      command=generate_plan)
generate_btn.grid(row=2, column=0, pady=15)

# ---------- RESULT FRAME ----------
result_frame = Frame(a, bg="white", bd=2, relief=RIDGE, padx=20, pady=20)
result_frame.grid(row=1, column=1, padx=20, pady=10)

Label(result_frame, text="Your Personalized Plan",
      font=("Arial", 14, "bold"),
      bg="white", fg="#1f4e79").pack(pady=(0,10))

result_label = Label(result_frame,
                     text="Your AI Diet Plan will appear here",
                     justify=LEFT, bg="white",
                     font=("Calibri", 12),
                     wraplength=350)
result_label.pack()

# ---------- FOOTER ----------
footer = Label(a, text="AI Diet Recommendation System | Built with Machine Learning",
               font=("Arial", 9), bg="#eaf4ff", fg="gray")
footer.grid(row=3, column=0, columnspan=2, pady=10)

a.mainloop()
