import sqlite3
import os

DB_FILE = 'quiz.db'

# --- Clean Start: Remove old DB if exists ---
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"✅ Removed old database file: {DB_FILE}")

# --- Connect to SQLite & Create Table ---
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

print("🔧 Creating new database and tables with 'section' column...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    section TEXT NOT NULL, 
    question_text TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# --- COMBINED SAMPLE QUESTIONS (Original 60 + New 60 = 120) ---

sample_questions = [
    # --- ORIGINAL SSC Questions (20) ---
    ('SSC', 'General Awareness', "Who is known as the 'Father of the Indian Constitution'?", 'Mahatma Gandhi',
     'Jawaharlal Nehru', 'Dr. B. R. Ambedkar', 'Sardar Vallabhbhai Patel', 'Dr. B. R. Ambedkar'),
    ('SSC', 'General Awareness', 'The "Dandia" is a popular dance form of which state?', 'Punjab', 'Gujarat',
     'Maharashtra', 'Rajasthan', 'Gujarat'),
    ('SSC', 'General Awareness', 'Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Venus',
     'Mars'),
    ('SSC', 'General Awareness', 'What is the capital of Japan?', 'Beijing', 'Seoul', 'Tokyo', 'Bangkok', 'Tokyo'),
    ('SSC', 'General Awareness', 'Who wrote the national anthem of India?', 'Rabindranath Tagore',
     'Bankim Chandra Chatterjee', 'Sarojini Naidu', 'Swami Vivekananda', 'Rabindranath Tagore'),

    ('SSC', 'Quantitative Aptitude', 'If a car travels 60 km in 1 hour, how far will it travel in 15 minutes?', '15 km',
     '20 km', '25 km', '30 km', '15 km'),
    ('SSC', 'Quantitative Aptitude', 'What is 20% of 200?', '20', '40', '60', '80', '40'),
    ('SSC', 'Quantitative Aptitude', 'If the price of 5 pens is $10, what is the price of 8 pens?', '$12', '$14', '$16',
     '$18', '$16'),
    ('SSC', 'Quantitative Aptitude', 'The sum of angles in a triangle is always:', '90 degrees', '180 degrees',
     '270 degrees', '360 degrees', '180 degrees'),
    ('SSC', 'Quantitative Aptitude', 'Find the average of 4, 6, and 8.', '5', '6', '7', '8', '6'),

    ('SSC', 'English Comprehension', 'Choose the synonym for "Ephemeral".', 'Eternal', 'Transient', 'Permanent',
     'Beautiful', 'Transient'),
    ('SSC', 'English Comprehension', 'Choose the antonym for "Brave".', 'Courageous', 'Bold', 'Timid', 'Strong',
     'Timid'),
    ('SSC', 'English Comprehension', 'Which of the following is a vowel?', 'B', 'C', 'D', 'E', 'E'),
    ('SSC', 'English Comprehension', 'Complete the proverb: "An apple a day keeps the ______ away."', 'Sorrow',
     'Doctor', 'Trouble', 'Friends', 'Doctor'),
    ('SSC', 'English Comprehension', 'What is the past tense of "run"?', 'Ran', 'Runned', 'Ranning', 'Rune', 'Ran'),

    ('SSC', 'General Intelligence & Reasoning', 'Which number should come next in the series: 2, 5, 10, 17, __?', '26',
     '25', '24', '28', '26'),
    ('SSC', 'General Intelligence & Reasoning', 'If CAT is to KITTEN, then DOG is to ______?', 'PUPPY', 'CUB', 'CALF',
     'JOEY', 'PUPPY'),
    ('SSC', 'General Intelligence & Reasoning', 'Which one does not belong to the group? (Apple, Banana, Rose, Orange)',
     'Apple', 'Banana', 'Rose', 'Orange', 'Rose'),
    ('SSC', 'General Intelligence & Reasoning',
     'Pointing to a photograph, a man said, "I have no brother, but that man\'s father is my father\'s son." Whose photograph was it?',
     'His own', 'His Son', 'His Father', 'His Nephew', 'His Son'),
    ('SSC', 'General Intelligence & Reasoning',
     'Arrange the words: (1) Police, (2) Punishment, (3) Crime, (4) Judge, (5) Judgment', '3,1,2,4,5', '3,1,4,5,2',
     '3,1,4,2,5', '1,2,3,4,5', '3,1,4,5,2'),

    # --- ORIGINAL BANK Questions (20) ---
    ('BANK', 'Reasoning Ability', 'If FRIEND is coded as HUMJTK, how is CANDLE written in that code?', 'DEQJQM',
     'ESJFME', 'EDRIRL', 'FYOBOC', 'EDRIRL'),
    ('BANK', 'Reasoning Ability', 'Which is the odd one out? (Lion, Tiger, Leopard, Cow)', 'Lion', 'Tiger', 'Leopard',
     'Cow', 'Cow'),
    ('BANK', 'Reasoning Ability', 'Statement: All pens are pencils. Conclusion: Some pencils are pens.', 'True',
     'False', 'Cannot Say', 'None', 'True'),
    ('BANK', 'Reasoning Ability', 'Find the missing number: 8, 27, 64, ?, 216', '100', '125', '150', '175', '125'),
    ('BANK', 'Reasoning Ability',
     'A man is facing North. He turns 90 degrees clockwise. Which direction is he facing now?', 'East', 'West', 'South',
     'North', 'East'),

    ('BANK', 'Quantitative Aptitude', 'A man buys a toy for Rs. 25 and sells it for Rs. 28. Find his gain percent.',
     '10%', '12%', '15%', '18%', '12%'),
    ('BANK', 'Quantitative Aptitude', 'What is the Simple Interest on $500 for 2 years at 5% per annum?', '$25', '$50',
     '$75', '$100', '$50'),
    ('BANK', 'Quantitative Aptitude',
     'The ratio of boys to girls in a class is 3:2. If there are 30 students, how many are boys?', '12', '15', '18',
     '20', '18'),
    ('BANK', 'Quantitative Aptitude',
     'A train 100m long is running at 30 km/hr. How long will it take to cross a pole?', '10 sec', '12 sec', '14 sec',
     '16 sec', '12 sec'),
    ('BANK', 'Quantitative Aptitude', 'What is the square root of 625?', '15', '25', '35', '45', '25'),

    ('BANK', 'English Language',
     'Identify the part of the sentence with an error: "He is one of the tallest boy in the class."', 'He is one of',
     'the tallest boy', 'in the class', 'No error', 'the tallest boy'),
    ('BANK', 'English Language', 'Choose the correct spelling.', 'Acomodation', 'Accomodation', 'Acommodation',
     'Accommodation', 'Accommodation'),
    ('BANK', 'English Language', 'Fill in the blank: He is afraid ___ spiders.', 'of', 'from', 'with', 'about', 'of'),
    ('BANK', 'English Language', 'The phrase "a piece of cake" means:', 'Something difficult', 'Something delicious',
     'Something very easy', 'A type of dessert', 'Something very easy'),
    ('BANK', 'English Language', 'What is the plural of "mouse"?', 'Mouses', 'Mice', 'Mouse', 'Mooses', 'Mice'),

    ('BANK', 'General / Financial Awareness', 'What does "M" stand for in the banking term "IMPS"?', 'Money', 'Mobile',
     'Immediate', 'Mutual', 'Immediate'),
    ('BANK', 'General / Financial Awareness', 'What is the full form of "KYC" in the banking sector?',
     'Know Your Customer', 'Know Your Cash', 'Keep Your Customer', 'Keep Your Cash', 'Know Your Customer'),
    ('BANK', 'General / Financial Awareness', 'Which body regulates the insurance sector in India?', 'RBI', 'SEBI',
     'IRDAI', 'PFRDA', 'IRDAI'),
    ('BANK', 'General / Financial Awareness', 'NEFT and RTGS are primarily used for:', 'Cash withdrawal',
     'Fund transfer', 'Loan application', 'Opening accounts', 'Fund transfer'),
    ('BANK', 'General / Financial Awareness', 'What is the currency of the USA?', 'Pound', 'Euro', 'Yen', 'Dollar',
     'Dollar'),

    # --- ORIGINAL RRB Questions (20) ---
    ('RRB', 'Mathematics', 'What is the value of pi (π) up to two decimal places?', '3.12', '3.14', '3.16', '3.18',
     '3.14'),
    ('RRB', 'Mathematics', 'If the area of a square is 64 sq. cm, what is the length of its side?', '4 cm', '6 cm',
     '8 cm', '10 cm', '8 cm'),
    ('RRB', 'Mathematics', 'Solve for x: 2x + 5 = 15', '3', '4', '5', '6', '5'),
    ('RRB', 'Mathematics', 'What is 7 multiplied by 8?', '49', '54', '56', '63', '56'),
    ('RRB', 'Mathematics',
     'A man\'s age is 3 times his son\'s age. If the son is 10 years old, what is the man\'s age?', '20', '30', '40',
     '25', '30'),

    ('RRB', 'General Intelligence and Reasoning', 'Water is to Pipe as Electricity is to ______?', 'Bulb', 'Wire',
     'Current', 'Switch', 'Wire'),
    ('RRB', 'General Intelligence and Reasoning', 'If Monday is the first day of the month, which is the fourth day?',
     'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Thursday'),
    ('RRB', 'General Intelligence and Reasoning',
     'Which is the heaviest animal? (Elephant, Blue Whale, Giraffe, Rhino)', 'Elephant', 'Blue Whale', 'Giraffe',
     'Rhino', 'Blue Whale'),
    ('RRB', 'General Intelligence and Reasoning', 'A doctor is to a patient as a teacher is to a ______?', 'School',
     'Book', 'Student', 'Class', 'Student'),
    ('RRB', 'General Intelligence and Reasoning', 'Complete the sequence: A, C, E, G, ?', 'H', 'I', 'J', 'K', 'I'),

    ('RRB', 'General Awareness', 'What is the name of the first semi-high-speed train in India?', 'Tejas Express',
     'Vande Bharat Express', 'Gatimaan Express', 'Shatabdi Express', 'Vande Bharat Express'),
    ('RRB', 'General Awareness', 'Which is the longest railway platform in the world?', 'Gorakhpur, India',
     'Kollam Junction, India', 'Kharagpur, India', 'Hubballi, India', 'Hubballi, India'),
    ('RRB', 'General Awareness', 'What is the name of the mascot of Indian Railways?', 'Appu the Elephant',
     'Sheru the Tiger', 'Bholu the Guard Elephant', 'Chintu the Cheetah', 'Bholu the Guard Elephant'),
    ('RRB', 'General Awareness', 'In which city is the Golden Temple located?', 'New Delhi', 'Agra', 'Amritsar',
     'Jaipur', 'Amritsar'),
    ('RRB', 'General Awareness', 'The first passenger train in India ran between which two stations in 1853?',
     'Bombay to Pune', 'Howrah to Hooghly', 'Bombay to Thane', 'Madras to Arcot', 'Bombay to Thane'),

    # --- NEWLY GENERATED SSC Questions (20) ---
    ('SSC', 'General Awareness', 'Which river is known as the "Sorrow of Bihar"?', 'Ganga', 'Yamuna', 'Kosi', 'Narmada', 'Kosi'),
    ('SSC', 'General Awareness', 'Who was the first woman Prime Minister of India?', 'Sonia Gandhi', 'Pratibha Patil', 'Indira Gandhi', 'Jayalalithaa', 'Indira Gandhi'),
    ('SSC', 'General Awareness', 'The Battle of Plassey was fought in which year?', '1757', '1857', '1764', '1803', '1757'),
    ('SSC', 'General Awareness', 'Which state is known as the "Land of Five Rivers"?', 'Punjab', 'Haryana', 'Uttar Pradesh', 'Rajasthan', 'Punjab'),
    ('SSC', 'General Awareness', 'The famous Sun Temple is located in which state?', 'Odisha', 'Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Odisha'),

    ('SSC', 'Quantitative Aptitude', 'If 3x + 7 = 22, what is the value of x?', '3', '4', '5', '6', '5'),
    ('SSC', 'Quantitative Aptitude', 'What is the LCM of 12 and 18?', '24', '36', '48', '72', '36'),
    ('SSC', 'Quantitative Aptitude', 'A shopkeeper gives 10% discount on a shirt marked at ₹1000. What is the selling price?', '₹800', '₹900', '₹950', '₹850', '₹900'),
    ('SSC', 'Quantitative Aptitude', 'The perimeter of a square is 40 cm. What is its area?', '80 sq cm', '100 sq cm', '120 sq cm', '160 sq cm', '100 sq cm'),
    ('SSC', 'Quantitative Aptitude', 'If 15% of a number is 45, what is the number?', '200', '250', '300', '350', '300'),

    ('SSC', 'English Comprehension', 'Choose the correct passive form: "She writes a letter."', 'A letter is written by her.', 'A letter was written by her.', 'A letter is being written by her.', 'A letter has been written by her.', 'A letter is written by her.'),
    ('SSC', 'English Comprehension', 'Identify the error: "Neither he nor his friends is coming."', 'Neither he', 'nor his friends', 'is coming', 'No error', 'is coming'),
    ('SSC', 'English Comprehension', 'What is the meaning of "Altruistic"?', 'Selfish', 'Selfless', 'Ambitious', 'Cruel', 'Selfless'),
    ('SSC', 'English Comprehension', 'Fill in the blank: "He is good ___ Mathematics."', 'in', 'at', 'on', 'with', 'at'),
    ('SSC', 'English Comprehension', 'Which sentence is grammatically correct?', 'He go to school daily.', 'He goes to school daily.', 'He going to school daily.', 'He gone to school daily.', 'He goes to school daily.'),

    ('SSC', 'General Intelligence & Reasoning', 'Find the odd one out: (Square, Circle, Triangle, Rectangle)', 'Square', 'Circle', 'Triangle', 'Rectangle', 'Circle'),
    ('SSC', 'General Intelligence & Reasoning', 'If DOG = 4157, CAT = 3120, then RAT = ?', '18120', '1812', '1820', '1720', '18120'),
    ('SSC', 'General Intelligence & Reasoning', 'Complete the series: Z, X, V, T, ?', 'R', 'S', 'Q', 'P', 'R'),
    ('SSC', 'General Intelligence & Reasoning', 'If P is the brother of Q, and Q is the sister of R, then what is P to R?', 'Brother', 'Sister', 'Father', 'Cannot be determined', 'Brother'),
    ('SSC', 'General Intelligence & Reasoning', 'In a certain code, "TEACHER" is written as "VGCEJGT". How is "STUDENT" written in that code?', 'UVWFGPV', 'UVWFDPV', 'UVWFDPU', 'UVWEDPV', 'UVWFDPU'),

    # --- NEWLY GENERATED BANK Questions (20) ---
    ('BANK', 'Reasoning Ability', 'If "PENCIL" is coded as "RGPENK", how is "ERASER" coded?', 'GTCTGT', 'GTCUGT', 'GTCTGU', 'GUCTGT', 'GTCTGT'),
    ('BANK', 'Reasoning Ability', 'Which word does not belong? (January, March, Friday, August)', 'January', 'March', 'Friday', 'August', 'Friday'),
    ('BANK', 'Reasoning Ability', 'Statement: All roses are flowers. Some flowers fade quickly. Conclusion: Some roses fade quickly.', 'True', 'False', 'Cannot Say', 'None', 'Cannot Say'),
    ('BANK', 'Reasoning Ability', 'Find the next term: 5, 11, 19, 29, ?', '39', '41', '43', '45', '41'),
    ('BANK', 'Reasoning Ability', 'Pointing to a girl, Arun said, "She is the daughter of my mother’s only son." How is Arun related to the girl?', 'Father', 'Brother', 'Uncle', 'Grandfather', 'Father'),

    ('BANK', 'Quantitative Aptitude', 'A sum of money doubles itself in 8 years at simple interest. What is the rate percent per annum?', '10%', '12.5%', '15%', '20%', '12.5%'),
    ('BANK', 'Quantitative Aptitude', 'The average of five numbers is 27. If one number is excluded, the average becomes 25. What is the excluded number?', '35', '30', '25', '20', '35'),
    ('BANK', 'Quantitative Aptitude', 'A man sold two chairs at ₹500 each. On one he gained 20% and on the other he lost 20%. What is his overall result?', 'No loss no gain', '4% gain', '4% loss', '10% loss', '4% loss'),
    ('BANK', 'Quantitative Aptitude', 'What is 35% of 200 + 25% of 300?', '145', '150', '155', '160', '145'),
    ('BANK', 'Quantitative Aptitude', 'The HCF of two numbers is 12 and their LCM is 72. If one number is 24, what is the other?', '18', '36', '48', '60', '36'),

    ('BANK', 'English Language', 'Choose the correctly spelt word.', 'Definately', 'Definitely', 'Definetly', 'Definatly', 'Definitely'),
    ('BANK', 'English Language', 'Fill in the blank: "She has been working here ___ 2020."', 'since', 'for', 'from', 'by', 'since'),
    ('BANK', 'English Language', 'What is the antonym of "Generous"?', 'Kind', 'Selfish', 'Helpful', 'Polite', 'Selfish'),
    ('BANK', 'English Language', 'Identify the part with error: "Each of the boys are intelligent."', 'Each of', 'the boys', 'are intelligent', 'No error', 'are intelligent'),
    ('BANK', 'English Language', 'What does "Break the ice" mean?', 'To end a relationship', 'To start a conversation in a social setting', 'To break something literally', 'To feel cold', 'To start a conversation in a social setting'),

    ('BANK', 'General / Financial Awareness', 'What does "RTGS" stand for?', 'Real Time Gross Settlement', 'Real Time General System', 'Rapid Transfer Gross System', 'Regular Transfer Gross Settlement', 'Real Time Gross Settlement'),
    ('BANK', 'General / Financial Awareness', 'Which of these is NOT a public sector bank?', 'SBI', 'PNB', 'HDFC Bank', 'Bank of Baroda', 'HDFC Bank'),
    ('BANK', 'General / Financial Awareness', 'What is the minimum amount that can be transferred via RTGS?', '₹1 lakh', '₹2 lakh', '₹50,000', 'No minimum', '₹2 lakh'),
    ('BANK', 'General / Financial Awareness', 'What does "UPI" stand for?', 'Unified Payment Interface', 'Universal Payment Interface', 'Unique Payment Identifier', 'United Payment Integration', 'Unified Payment Interface'),
    ('BANK', 'General / Financial Awareness', 'Which institution issues currency notes in India?', 'SEBI', 'Ministry of Finance', 'RBI', 'SBI', 'RBI'),

    # --- NEWLY GENERATED RRB Questions (20) ---
    ('RRB', 'Mathematics', 'What is the cube root of 729?', '7', '8', '9', '10', '9'),
    ('RRB', 'Mathematics', 'If the radius of a circle is 7 cm, what is its circumference? (Use π = 22/7)', '44 cm', '88 cm', '154 cm', '308 cm', '44 cm'),
    ('RRB', 'Mathematics', 'What is the value of (12)^2 - (8)^2?', '80', '90', '100', '110', '80'),
    ('RRB', 'Mathematics', 'A train covers 120 km in 2 hours. What is its speed in km/h?', '40', '50', '60', '70', '60'),
    ('RRB', 'Mathematics', 'If 20% of a number is 50, what is 50% of that number?', '100', '125', '150', '200', '125'),

    ('RRB', 'General Intelligence and Reasoning', 'Pen is to Write as Knife is to ______?', 'Cut', 'Eat', 'Sharp', 'Steel', 'Cut'),
    ('RRB', 'General Intelligence and Reasoning', 'Which number is missing? 3, 6, 12, 24, ?', '36', '48', '30', '42', '48'),
    ('RRB', 'General Intelligence and Reasoning', 'If BOOK is coded as 43, then PEN is coded as?', '35', '36', '37', '38', '35'),
    ('RRB', 'General Intelligence and Reasoning', 'Arrange in logical order: (1) Birth, (2) Education, (3) Job, (4) Marriage, (5) Death', '1,2,3,4,5', '1,3,2,4,5', '2,1,3,4,5', '1,2,4,3,5', '1,2,3,4,5'),
    ('RRB', 'General Intelligence and Reasoning', 'Which word comes first alphabetically?', 'Apple', 'Ant', 'Ape', 'Apricot', 'Ant'),

    ('RRB', 'General Awareness', 'Who is known as the "Missile Man of India"?', 'Dr. APJ Abdul Kalam', 'Dr. Vikram Sarabhai', 'Dr. Homi Bhabha', 'Dr. C.V. Raman', 'Dr. APJ Abdul Kalam'),
    ('RRB', 'General Awareness', 'What is the full form of "IRCTC"?', 'Indian Railway Catering and Tourism Corporation', 'Indian Rail Transport and Cargo Corporation', 'Indian Railway Catering and Transport Company', 'Indian Railways Catering and Tourism Council', 'Indian Railway Catering and Tourism Corporation'),
    ('RRB', 'General Awareness', 'Which is the fastest train in India as of 2024?', 'Rajdhani Express', 'Shatabdi Express', 'Vande Bharat Express', 'Duronto Express', 'Vande Bharat Express'),
    ('RRB', 'General Awareness', 'How many zones are there in Indian Railways?', '12', '15', '17', '18', '18'),
    ('RRB', 'General Awareness', 'Where is the headquarters of Indian Railways located?', 'Mumbai', 'Kolkata', 'Chennai', 'New Delhi', 'New Delhi'),
    # --- EXTRA 10 QUESTIONS FOR TESTING COMPLETION FLOW ---
    ('SSC', 'General Awareness', 'Who was the first Indian to win a Nobel Prize?', 'C.V. Raman', 'Rabindranath Tagore',
     'Mother Teresa', 'Amartya Sen', 'Rabindranath Tagore'),
    ('BANK', 'Quantitative Aptitude',
     'If the cost price of 10 articles is equal to the selling price of 8 articles, what is the gain percent?', '20%',
     '25%', '30%', '40%', '25%'),
    ('RRB', 'General Awareness', 'Which city is known as the Silicon Valley of India?', 'Hyderabad', 'Pune',
     'Bangalore', 'Chennai', 'Bangalore'),
    ('SSC', 'English Comprehension', 'Choose the correct sentence.', 'She don’t like apples.',
     'She doesn’t likes apples.', 'She doesn’t like apples.', 'She not like apples.', 'She doesn’t like apples.'),
    ('BANK', 'Reasoning Ability', 'Find the next letter: A, D, G, J, ?', 'K', 'L', 'M', 'N', 'M'),
    ('RRB', 'Mathematics', 'What is 15% of 300?', '30', '35', '45', '50', '45'),
    ('SSC', 'General Intelligence & Reasoning', 'If 5th March, 2024 is Tuesday, what day will 5th April, 2024 be?',
     'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Friday'),
    ('BANK', 'General / Financial Awareness', 'What does "PIN" stand for in ATM context?', 'Personal Index Number',
     'Private Identification Number', 'Personal Identification Number', 'Public Identity Number',
     'Personal Identification Number'),
    ('RRB', 'General Intelligence and Reasoning',
     'Which word is the odd one out? (Square, Triangle, Rectangle, Sphere)', 'Square', 'Triangle', 'Rectangle',
     'Sphere', 'Sphere'),
    ('SSC', 'Quantitative Aptitude',
     'The average of three numbers is 20. If two numbers are 15 and 25, what is the third number?', '10', '20', '30',
     '40', '20')


    ('RRB', 'General Awareness', 'Which festival is known as the "Festival of Colors"?', 'Diwali', 'Holi', 'Dussehra', 'Eid', 'Holi'),
    ('RRB', 'General Awareness', 'Who invented the telephone?', 'Thomas Edison', 'Alexander Graham Bell', 'Nikola Tesla', 'Guglielmo Marconi', 'Alexander Graham Bell'),
    ('RRB', 'General Awareness', 'Which planet is closest to the Sun?', 'Venus', 'Earth', 'Mercury', 'Mars', 'Mercury'),
    ('RRB', 'General Awareness', 'The largest desert in the world is?', 'Gobi Desert', 'Kalahari Desert', 'Sahara Desert', 'Thar Desert', 'Sahara Desert'),
    ('RRB', 'General Awareness', 'What is the national animal of India?', 'Lion', 'Elephant', 'Tiger', 'Peacock', 'Tiger')
]

# --- Insert All Questions ---
print(f"📥 Inserting {len(sample_questions)} questions into the database...")
cursor.executemany(
    'INSERT INTO questions (category, section, question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
    sample_questions)

# --- Finalize ---
connection.commit()
connection.close()
print(f"✅ Database '{DB_FILE}' successfully created with {len(sample_questions)} questions!")