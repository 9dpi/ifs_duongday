import os
import re

target_dir = r"d:\Dropbox\Project\UX UI Thermal\Layouts\ifs_duongday"

# Mapping of filenames to Title and Breadcrumb/Header text
PAGE_INFO = {
    "quan_ly_su_co_vat_the_la.html": {
        "title": "Vật thể lạ",
        "crumb": "Vật thể lạ",
        "header": "VẬT THỂ LẠ"
    },
    "quan_ly_su_co_den_bao_hieu.html": {
        "title": "Đèn báo hiệu",
        "crumb": "Đèn báo hiệu",
        "header": "ĐÈN BÁO HIỆU"
    },
    "quan_ly_su_co_do_nghieng.html": {
        "title": "Độ nghiêng vượt ngưỡng",
        "crumb": "Độ nghiêng vượt ngưỡng",
        "header": "CẢNH BÁO ĐỘ NGHIÊNG"
    },
    "quan_ly_su_co_chieu_cao_an_toan.html": {
        "title": "Chiều cao an toàn",
        "crumb": "Chiều cao an toàn phương tiện",
        "header": "VI PHẠM CHIỀU CAO"
    },
    "quan_ly_su_co_chieu_cao_chay_khoi.htm": {
        "title": "Sự cố Cháy khói",
        "crumb": "Cháy khói",
        "header": "SỰ CỐ CHÁY KHÓI"
    },
    "quan_ly_su_co_doi_tuong.html": {
        "title": "Đối tượng xâm nhập",
        "crumb": "Đối tượng xâm nhập vùng cấm",
        "header": "SỰ CỐ ĐỐI TƯỢNG XÂM NHẬP"
    }
}

def fix_titles():
    for filename, info in PAGE_INFO.items():
        filepath = os.path.join(target_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update <title>
        content = re.sub(r'<title>.*?</title>', f'<title>IFS - ĐƯỜNG DÂY | {info["title"]}</title>', content)
        
        # 2. Update Breadcrumb <span>
        content = re.sub(r'<div class="bread-crumb">.*?<span>.*?</span></div>', 
                         f'<div class="bread-crumb">Quản lý sự cố / <span>{info["crumb"]}</span></div>', content)
        
        # 3. Update Header in table container
        # Pattern: <div style="font-size: 15px; font-weight: 700; color: var(--primary); text-transform: uppercase;"> ... </div>
        header_pattern = r'(<div style="font-size: 15px; font-weight: 700; color: var(--primary); text-transform: uppercase;">\s*)(.*?)(\s*</div>)'
        
        def header_repl(m):
            return f"{m.group(1)}{info['header']}{m.group(3)}"
            
        content = re.sub(header_pattern, header_repl, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated titles for {filename}")

if __name__ == "__main__":
    fix_titles()
