"""
Question Generator using Google Gemini API
This module generates high-quality government exam questions for SSC, Bank, and RRB exams.
"""

import os
import sqlite3
from datetime import datetime
try:
    import google.generativeai as genai
except ImportError:
    genai = None
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_FILE = 'quiz.db'

# Category and section configurations for government exams
EXAM_CATEGORIES = {
    'SSC': [
        'General Awareness',
        'Quantitative Aptitude',
        'English Comprehension',
        'General Intelligence & Reasoning'
    ],
    'BANK': [
        'Reasoning Ability',
        'Quantitative Aptitude',
        'English Language',
        'General / Financial Awareness'
    ],
    'RRB': [
        'Mathematics',
        'General Intelligence and Reasoning',
        'General Awareness'
    ]
}

def get_db_connection():
    """Create database connection"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def generate_questions_with_api(category, section, count=5):
    """
    Generate questions using Google Gemini API
    
    Args:
        category: Exam category (SSC, BANK, RRB)
        section: Subject section
        count: Number of questions to generate
    
    Returns:
        List of question dictionaries
    """
    if genai is None:
        print("⚠️  Google Generative AI package not installed")
        return []
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("⚠️  GEMINI_API_KEY not found in environment variables")
        return []
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""Generate {count} high-quality multiple-choice questions for {category} exam, {section} section.

Requirements:
1. Questions should be appropriate for Indian government competitive exams
2. Include 4 options (A, B, C, D) for each question
3. Clearly indicate the correct answer
4. Questions should test genuine knowledge and reasoning
5. Avoid ambiguous or trick questions
6. Use proper grammar and formatting

Format each question as:
Question: [question text]
A) [option 1]
B) [option 2]
C) [option 3]
D) [option 4]
Correct Answer: [exact option text]

Generate {count} questions following this format strictly."""

        response = model.generate_content(prompt)
        questions = parse_api_response(response.text, category, section)
        return questions
    
    except Exception as e:
        print(f"❌ Error generating questions with API: {e}")
        return []

def parse_api_response(response_text, category, section):
    """Parse API response and extract questions"""
    questions = []
    
    try:
        # Split by "Question:" to get individual questions
        question_blocks = response_text.split("Question:")
        
        for block in question_blocks[1:]:  # Skip first empty split
            try:
                lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
                
                if len(lines) < 6:  # Need at least question + 4 options + answer
                    continue
                
                question_text = lines[0].strip()
                
                # Extract options
                options = {}
                for line in lines[1:5]:
                    if ')' in line:
                        parts = line.split(')', 1)
                        key = parts[0].strip().upper()
                        value = parts[1].strip() if len(parts) > 1 else ''
                        options[key] = value
                
                # Extract correct answer
                correct_answer = None
                for line in lines:
                    if 'Correct Answer:' in line or 'Answer:' in line:
                        answer_text = line.split(':', 1)[1].strip()
                        # Try to match to one of the options
                        for opt_key, opt_val in options.items():
                            if answer_text in opt_val or opt_val in answer_text:
                                correct_answer = opt_val
                                break
                        if not correct_answer and len(answer_text) == 1:
                            # Answer is just a letter
                            correct_answer = options.get(answer_text.upper())
                        break
                
                if question_text and len(options) == 4 and correct_answer:
                    questions.append({
                        'category': category,
                        'section': section,
                        'question_text': question_text,
                        'option_a': options.get('A', ''),
                        'option_b': options.get('B', ''),
                        'option_c': options.get('C', ''),
                        'option_d': options.get('D', ''),
                        'correct_answer': correct_answer
                    })
            
            except Exception as e:
                print(f"⚠️  Error parsing question block: {e}")
                continue
    
    except Exception as e:
        print(f"❌ Error parsing API response: {e}")
    
    return questions

def add_questions_to_database(questions):
    """Add new questions to database without deleting existing ones"""
    if not questions:
        print("⚠️  No questions to add")
        return 0
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    added_count = 0
    for q in questions:
        try:
            # Check if question already exists (avoid duplicates)
            existing = cursor.execute(
                'SELECT id FROM questions WHERE question_text = ?',
                (q['question_text'],)
            ).fetchone()
            
            if not existing:
                cursor.execute('''
                    INSERT INTO questions (category, section, question_text, 
                                          option_a, option_b, option_c, option_d, 
                                          correct_answer)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    q['category'], q['section'], q['question_text'],
                    q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                    q['correct_answer']
                ))
                added_count += 1
        except Exception as e:
            print(f"⚠️  Error adding question: {e}")
    
    conn.commit()
    conn.close()
    
    return added_count

def generate_and_store_questions():
    """Main function to generate and store new questions for all categories"""
    print(f"\n🚀 Starting automated question generation - {datetime.now()}")
    
    total_added = 0
    
    for category, sections in EXAM_CATEGORIES.items():
        print(f"\n📚 Processing {category} category...")
        
        for section in sections:
            print(f"  ➤ Generating questions for: {section}")
            
            # Generate 3 questions per section
            questions = generate_questions_with_api(category, section, count=3)
            
            if questions:
                added = add_questions_to_database(questions)
                total_added += added
                print(f"    ✅ Added {added} new questions")
            else:
                print(f"    ⚠️  No questions generated")
    
    print(f"\n✨ Total questions added: {total_added}")
    print(f"⏰ Completed at: {datetime.now()}\n")
    
    return total_added

if __name__ == '__main__':
    # Test the question generator
    generate_and_store_questions()
