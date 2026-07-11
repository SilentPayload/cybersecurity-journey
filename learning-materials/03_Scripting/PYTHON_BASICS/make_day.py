import os
import sys

def create_day(day_num, module_name):
    folder_name = f"{module_name}/Day_{day_num:02d}"
    os.makedirs(folder_name, exist_ok=True)
    file_path = f"{folder_name}/Day_{day_num:02d}.md"
    
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(f"# Day {day_num}\n\n## 🎯 Learning Objectives\n\n## 🧠 Key Concepts\n\n## 🚀 Daily Git Practice\n`git commit -m \"Day {day_num}: ...\"`")
    print(f"✅ Created {file_path}")

# Check if the user provided enough arguments
if len(sys.argv) < 3:
    print("❌ Error: Missing arguments.")
    print("Usage: python make_day.py <day_number> <module_name>")
    print("Example: python make_day.py 1 03_Scripting")
else:
    create_day(int(sys.argv[1]), sys.argv[2])