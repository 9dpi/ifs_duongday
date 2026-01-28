import os
import re

# Configuration
target_dir = r"d:\Dropbox\Project\UX UI Thermal\Layouts\ifs_duongday"

# The new standard menu HTML structure
# Note: No 'active-link' classes here; they will be added dynamically.
MENU_HTML = """<nav class="navbar">
        <div style="display:flex; align-items:center">
            <button class="mobile-btn" onclick="toggleMobileMenu()">
                <svg width="24" height="24" viewBox="0 0 24 24">
                    <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" />
                </svg>
            </button>
            <a href="dashboard.html" class="brand" style="text-decoration:none">
                <div class="logo-box">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"
                        stroke-linejoin="round">
                        <path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"></path>
                    </svg>
                </div> IFS - ĐƯỜNG DÂY
            </a>
        </div>

        <div class="nav-menu" id="mainMenu">
            <div class="nav-wrapper"><a href="dashboard.html" class="nav-link">TRANG CHỦ</a></div>
            <div class="nav-wrapper"><a href="giamsattructiep.html" class="nav-link">GIÁM SÁT TRỰC TIẾP</a></div>
            <div class="nav-wrapper"><a href="giamsatsuco.html" class="nav-link">GIÁM SÁT SỰ CỐ</a></div>

            <div class="nav-wrapper">
                <div class="nav-link">QUẢN LÝ SỰ CỐ <svg class="nav-arrow" width="10" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z" /></svg></div>
                <div class="dropdown-menu">
                    <a href="quan_ly_su_co_doi_tuong.html" class="menu-link">Đối tượng xâm nhập vùng cấm</a>
                    <a href="quan_ly_su_co_chieu_cao_chay_khoi.htm" class="menu-link">Cháy khói</a>
                    <a href="quan_ly_su_co_do_nghieng.html" class="menu-link">Độ nghiêng vượt ngưỡng</a>
                    <a href="quan_ly_su_co_chieu_cao_an_toan.html" class="menu-link">Chiều cao an toàn phương tiện</a>
                    <a href="quan_ly_su_co_vat_the_la.html" class="menu-link">Vật thể lạ</a>
                    <a href="quan_ly_su_co_den_bao_hieu.html" class="menu-link">Đèn báo hiệu</a>
                </div>
            </div>

            <div class="nav-wrapper">
                <div class="nav-link">BÁO CÁO & HDSD <svg class="nav-arrow" width="10" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z" /></svg></div>
                <div class="dropdown-menu">
                    <a href="huong_dan_su_dung.html" class="menu-link">Hướng dẫn sử dụng</a>
                    <a href="danh_sach_su_co.html" class="menu-link">Báo cáo sự cố đường dây</a>
                    <a href="bao_cao_su_co_den_hieu.html" class="menu-link">Báo cáo sự cố đèn báo hiệu</a>
                </div>
            </div>

            <div class="nav-wrapper">
                <div class="nav-link">THIẾT LẬP CẢNH BÁO <svg class="nav-arrow" width="10" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z" /></svg></div>
                 <div class="dropdown-menu">
                    <a href="thietlapcanhbao_kenhcanhbao.html" class="menu-link">Kênh cảnh báo</a>
                    <a href="theodoidiemdo_bocanhbao.html" class="menu-link">Bộ cảnh báo</a>
                 </div>
            </div>
        </div>

        <div class="header-actions">
            <div class="theme-switch" onclick="toggleTheme()">
                <div class="switch-knob"></div>
            </div>
            <div
                style="width:32px; height:32px; background:#E5E7EB; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; color:#4B5563">
                A</div>
        </div>
    </nav>"""

def update_files():
    files = [f for f in os.listdir(target_dir) if f.endswith('.html') or f.endswith('.htm')]
    
    for filename in files:
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Prepare the menu for this specific file
        current_menu = MENU_HTML
        
        # 1. Activate the specific link
        # Regex to find href="CURRENT_FILENAME" in class="menu-link" or class="nav-link"
        # We replace class="menu-link" with class="menu-link active-link"
        # Or class="nav-link" with class="nav-link active-link"
        
        # Search for exact href match for sub-menu items
        pattern_sub = r'(<a href="{}" class="menu-link">)'.format(re.escape(filename))
        if re.search(pattern_sub, current_menu):
            current_menu = re.sub(pattern_sub, lambda m: m.group(1).replace('class="menu-link"', 'class="menu-link active-link"'), current_menu)
            
            # Simplified approach: Determine parent based on filename knowledge.
            # Parent: QUẢN LÝ SỰ CỐ
            if filename in ["quan_ly_su_co_doi_tuong.html", "quan_ly_su_co_chieu_cao_chay_khoi.htm", "quan_ly_su_co_do_nghieng.html", "quan_ly_su_co_chieu_cao_an_toan.html", "quan_ly_su_co_vat_the_la.html", "quan_ly_su_co_den_bao_hieu.html"]:
                current_menu = current_menu.replace('class="nav-link">QUẢN LÝ SỰ CỐ', 'class="nav-link active-link">QUẢN LÝ SỰ CỐ')
            
            # Parent: BÁO CÁO & HDSD
            elif filename in ["huong_dan_su_dung.html", "danh_sach_su_co.html", "bao_cao_su_co_den_hieu.html"]:
                 current_menu = current_menu.replace('class="nav-link">BÁO CÁO & HDSD', 'class="nav-link active-link">BÁO CÁO & HDSD')

            # Parent: THIẾT LẬP CẢNH BÁO
            elif filename in ["thietlapcanhbao_kenhcanhbao.html", "theodoidiemdo_bocanhbao.html"]:
                 current_menu = current_menu.replace('class="nav-link">THIẾT LẬP CẢNH BÁO', 'class="nav-link active-link">THIẾT LẬP CẢNH BÁO')

        else:
            # Search for top-level items
            pattern_top = r'(<a href="{}" class="nav-link">)'.format(re.escape(filename))
            if re.search(pattern_top, current_menu):
                 current_menu = re.sub(pattern_top, r'\1'.replace('class="nav-link"', 'class="nav-link active-link"'), current_menu)

        # 2. Replace the old nav block
        # Match <nav class="navbar"> ... </nav>
        # Use simple string replacement if possible, or regex with dotall
        new_content = re.sub(r'<nav class="navbar">.*?</nav>', current_menu, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename} (or nav not found/already matched)")

if __name__ == "__main__":
    update_files()
