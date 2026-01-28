import os

target_dir = r"d:\Dropbox\Project\UX UI Thermal\Layouts\ifs_duongday"

def fix_files():
    files = [f for f in os.listdir(target_dir) if f.endswith('.html') or f.endswith('.htm')]
    
    for filename in files:
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix the specific broken class issue
        # The script generated: <div class="nav-link" active-link">
        # We want: <div class="nav-link active-link">
        
        new_content = content.replace('<div class="nav-link" active-link">', '<div class="nav-link active-link">')
        
        # Also fix the specific issue in huong_dan_su_dung.html regarding theme
        if filename == 'huong_dan_su_dung.html':
            if '<html lang="vi">' in new_content:
                new_content = new_content.replace('<html lang="vi">', '<html lang="vi" data-theme="dark">')

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename}")
        else:
            print(f"No repair needed for {filename}")

if __name__ == "__main__":
    fix_files()
