import os
import re

target_dir = r"d:\Dropbox\Project\UX UI Thermal\Layouts\ifs_duongday"

def fix_pagination():
    files = [f for f in os.listdir(target_dir) if f.endswith('.html') or f.endswith('.htm')]
    
    for filename in files:
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace "Hiển thị từ 1 đến X" with "Hiển thị 1-9"
        # Regex to catch variations
        new_content = re.sub(r'Hiển thị từ 1 đến \d+', 'Hiển thị 1-9', content)
        
        # Also fix "Hiển thị 1-8" etc
        new_content = re.sub(r'Hiển thị 1-\d+', 'Hiển thị 1-9', new_content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed pagination text in {filename}")

if __name__ == "__main__":
    fix_pagination()
