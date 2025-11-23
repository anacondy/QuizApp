"""
Scheduler for automated question generation
Runs daily at midnight to fetch new questions
"""

import schedule
import time
from datetime import datetime
from question_generator import generate_and_store_questions

def run_scheduled_task():
    """Task to run at scheduled time"""
    print(f"\n{'='*60}")
    print(f"🕐 Scheduled Task Started at {datetime.now()}")
    print(f"{'='*60}")
    
    try:
        generate_and_store_questions()
        print(f"\n✅ Scheduled task completed successfully")
    except Exception as e:
        print(f"\n❌ Error in scheduled task: {e}")
    
    print(f"{'='*60}\n")

def start_scheduler():
    """Start the scheduler - runs daily at midnight"""
    # Schedule the task to run every day at midnight
    schedule.every().day.at("00:00").do(run_scheduled_task)
    
    print("\n" + "="*60)
    print("📅 Scheduler Started")
    print("⏰ Questions will be generated daily at midnight (00:00)")
    print("="*60 + "\n")
    
    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    # For testing, you can also run immediately
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--now':
        print("Running task immediately for testing...")
        run_scheduled_task()
    else:
        start_scheduler()
