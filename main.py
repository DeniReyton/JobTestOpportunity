import telebot

bot = telebot.TeleBot("7110436265:AAGHNx2sOVrZxfVouBTRxTu4XqpT9Dcm_iI",
                      parse_mode=None)

import google.generativeai as genai

genai.configure(api_key="AIzaSyCOzVfY2CMGpjfbk8KX7MaDFDBEs_bADzE")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["You're an experienced driving instructor with a passion for teaching individuals how to drive various vehicles. Your specialty lies in teaching individuals how to drive the Toyota Camry 70 model.Your task is to create a comprehensive driving lesson plan for teaching someone how to drive the Camry 70. Include details like the key features of the vehicle, driving techniques specific to this model, common challenges learners may face, and any tips for mastering driving this specific car model.Ensure to provide clear and detailed instructions that are easy to understand for a beginner driver. Your goal is to equip the learner with all the necessary skills and knowledge to confidently drive the Camry 70.For example, you can include instructions on adjusting the seat and mirrors for optimal driving position, how to smoothly accelerate and brake using the vehicle's specific response, proper turning techniques, and tips on parking the Camry 70 efficiently in different scenarios"]
  },
  {
    "role": "model",
    "parts": ["## Comprehensive Driving Lesson Plan for the Toyota Camry 70\n\n**Instructor:** [Your Name]\n\n**Objective:** To equip learners with the necessary skills and knowledge to confidently drive the Toyota Camry 70.\n\n### Key Features of the Toyota Camry 70\n\n* 2.5-liter 4-cylinder or 3.5-liter V6 engine\n* 8-speed automatic transmission\n* Front- or all-wheel drive\n* Independent front and rear suspension\n* Advanced safety features (e.g., lane departure alert, automatic emergency braking)\n\n### Driving Techniques Specific to the Camry 70\n\n**1. Adjusting the Seat and Mirrors:**\n\n* Adjust the seat height and distance to allow for comfortable reach to the pedals and steering wheel.\n* Position the side mirrors to eliminate blind spots.\n* Adjust the rearview mirror for a clear view of the rear.\n\n**2. Smooth Acceleration and Braking:**\n\n* Start by pressing the gas pedal gently and increasing pressure gradually.\n* Use the brake pedal smoothly to avoid sudden stops.\n* Anticipate upcoming changes in speed and adjust acceleration or braking accordingly.\n\n**3. Proper Turning Techniques:**\n\n* Turn the steering wheel gradually when approaching turns.\n* Maintain a smooth and consistent turning radius.\n* Use the turn signals early to communicate your intentions.\n\n**4. Parking:**\n\n* **Parallel Parking:**\n    * Align the car parallel to the curb with the front wheels slightly turned towards the curb.\n    * Reverse slowly while turning the wheels towards the curb.\n    * Once the car is parallel, straighten the wheels and complete the reverse.\n* **Perpendicular Parking:**\n    * Position the car behind the parking space, parallel to the curb.\n    * Reverse slowly while turning the wheels towards the curb.\n    * Once the car is perpendicular, straighten the wheels and complete the reverse.\n\n### Common Challenges Learners May Face\n\n* Getting accustomed to the size and weight of the vehicle.\n* Mastering smooth acceleration and braking techniques.\n* Navigating tight turns and parking in confined spaces.\n* Recognizing and responding to advanced safety features.\n\n### Tips for Mastering Driving the Camry 70\n\n* Practice regularly in different driving conditions.\n* Seek feedback from an experienced driver or instructor.\n* Use the advanced safety features to enhance your driving experience.\n* Learn the specific handling characteristics of the Camry 70, such as its responsive steering and comfortable ride.\n* Remain alert and anticipate potential hazards to ensure a safe driving experience.\n\n### Conclusion\n\nBy following this comprehensive lesson plan and practicing diligently, learners can develop the skills and confidence necessary to safely and confidently drive the Toyota Camry 70. Remember, becoming a proficient driver requires time, patience, and a commitment to safe driving practices."]
  },
])

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    response = (convo.last.text)
    bot.reply_to(message,response)

bot.infinity_polling()
