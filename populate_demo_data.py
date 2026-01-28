import os
import re
import random

target_dir = r"d:\Dropbox\Project\UX UI Thermal\Layouts\ifs_duongday"

def get_random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d} {day:02d}/{month:02d}/2026"

def get_random_cam():
    return f"CAM{random.randint(100, 999)}"

def generate_mix_items(count=9):
    grid_html = ""
    table_html = ""
    types = [
        {"type": "fire", "badge": "🔥 CHÁY", "class": "tag-fire", "title": "PHÁT HIỆN ĐỐM LỬA", "loc": "Cột"}, 
        {"type": "object", "badge": "📦 VẬT THỂ", "class": "tag-object", "title": "VẬT THỂ LẠ", "loc": "Cột"},
        {"type": "height", "badge": "📏 CHIỀU CAO", "class": "tag-height", "title": "VI PHẠM CHIỀU CAO", "loc": "Khoảng cột"}
    ]
    
    for i in range(1, count + 1):
        t = random.choice(types)
        col = random.randint(10, 50)
        loc = f"{t['loc']} {col} - Tuyến {random.randint(1, 3)}"
        time = get_random_date()
        img = random.randint(1, 3)
        status = random.choice(["Chờ xử lý", "Đang xử lý", "Đã xử lý"])
        status_color = "--warning" if status != "Đã xử lý" else "--success"
        
        # GRID
        grid_html += f"""
                <div class="card inc-card-new" style="padding: 15px;">
                    <div style="display:flex; justify-content:space-between; align-items:start">
                        <div class="inc-badge {t['class']}">{t['badge']}</div>
                        <div style="font-size:12px; color:var(--text-sub)">{time}</div>
                    </div>
                    <img src="images/cam-0{img}.png" class="inc-img" alt="Inc">
                    <div>
                        <div class="inc-title">{t['title']} {col}</div>
                        <div class="inc-info-row">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            {loc}
                        </div>
                    </div>
                    <div style="margin-top:auto; padding-top:10px; border-top:1px solid var(--border); display:flex; justify-content:space-between; align-items:center">
                        <span style="font-size:12px; color:var({status_color})">● {status}</span>
                        <div style="display:flex; gap:10px">
                            <button style="background:transparent; border:none; cursor:pointer">👁️</button>
                            <button style="background:transparent; border:none; cursor:pointer">✏️</button>
                        </div>
                    </div>
                </div>"""

        # TABLE
        table_html += f"""
                        <tr>
                            <td>{i}</td>
                            <td><img src="images/cam-0{img}.png" style="width:60px; height:40px; border-radius:4px"></td>
                            <td>#SC-{i:03d}</td>
                            <td>{time}</td>
                            <td>{t['badge']}</td>
                            <td>{loc}</td>
                            <td><span style="color:var({status_color})">● {status}</span></td>
                            <td style="text-align:center">
                                <button class="action-btn-circle">👁️</button>
                                <button class="action-btn-circle">✎</button>
                                <button class="action-btn-circle">🗑️</button>
                            </td>
                        </tr>"""
    return grid_html, table_html

def generate_object_items(count=9):
    grid_html = ""
    table_html = ""
    for i in range(1, count + 1):
        col = random.randint(10, 99)
        loc = f"Cột {col} - Tuyến Bắc Nam"
        time = get_random_date()
        img = 2
        status = random.choice(["Chờ xử lý", "Đã xử lý"])
        status_color = "--warning" if status != "Đã xử lý" else "--success"
        obj_name = random.choice(["Người leo trụ", "Thả diều", "Flycam", "Cành cây"])

        grid_html += f"""
                <div class="card inc-card-new" style="padding: 15px;">
                    <div style="display:flex; justify-content:space-between; align-items:start">
                        <div class="inc-badge tag-object">📦 {obj_name.upper()}</div>
                        <div style="font-size:12px; color:var(--text-sub)">{time}</div>
                    </div>
                    <img src="images/cam-0{img}.png" class="inc-img" alt="Inc">
                    <div>
                        <div class="inc-title">PHÁT HIỆN {obj_name.upper()}</div>
                         <div class="inc-info-row">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            {loc}
                        </div>
                         <div class="inc-info-row">CAMERA: {get_random_cam()}</div>
                    </div>
                    <div style="margin-top:auto; padding-top:10px; border-top:1px solid var(--border); display:flex; justify-content:space-between; align-items:center">
                        <span style="font-size:12px; color:var({status_color})">● {status}</span>
                        <div style="display:flex; gap:10px">
                             <button style="background:transparent; border:none; cursor:pointer">👁️</button>
                             <button style="background:transparent; border:none; cursor:pointer">✏️</button>
                        </div>
                    </div>
                </div>"""

        table_html += f"""
                        <tr>
                            <td>{i}</td>
                            <td><img src="images/cam-0{img}.png" style="width:60px; height:40px; border-radius:4px"></td>
                            <td>#OBJ-{i:03d}</td>
                            <td>{time}</td>
                            <td>{obj_name}</td>
                            <td>{loc}</td>
                            <td><span style="color:var({status_color})">● {status}</span></td>
                             <td style="text-align:center">
                                <button class="action-btn-circle">👁️</button>
                                <button class="action-btn-circle">✎</button>
                                <button class="action-btn-circle">🗑️</button>
                            </td>
                        </tr>"""
    return grid_html, table_html

def generate_fire_items(count=9):
    grid_html = ""
    table_html = ""
    for i in range(1, count + 1):
        col = random.randint(10, 99)
        loc = f"Rừng phòng hộ - Cột {col}"
        time = get_random_date()
        img = 1
        status = random.choice(["Đã dập tắt", "Đang cháy", "Cảnh báo khói"])
        status_color = "--danger" if status == "Đang cháy" else ("--warning" if status == "Cảnh báo khói" else "--success")
        
        grid_html += f"""
                <div class="card inc-card-new" style="padding: 15px;">
                    <div style="display:flex; justify-content:space-between; align-items:start">
                        <div class="inc-badge tag-fire">🔥 CHÁY RỪNG</div>
                        <div style="font-size:12px; color:var(--text-sub)">{time}</div>
                    </div>
                    <img src="images/cam-0{img}.png" class="inc-img" alt="Inc">
                    <div>
                        <div class="inc-title">CẢNH BÁO NHIỆT KHU VỰC CỘT {col}</div>
                         <div class="inc-info-row">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            {loc}
                        </div>
                    </div>
                    <div style="margin-top:auto; padding-top:10px; border-top:1px solid var(--border); display:flex; justify-content:space-between; align-items:center">
                        <span style="font-size:12px; color:var({status_color})">● {status}</span>
                        <div style="display:flex; gap:10px">
                             <button style="background:transparent; border:none; cursor:pointer">👁️</button>
                             <button style="background:transparent; border:none; cursor:pointer">✏️</button>
                        </div>
                    </div>
                </div>"""

        table_html += f"""
                        <tr>
                            <td>{i}</td>
                            <td><img src="images/cam-0{img}.png" style="width:60px; height:40px; border-radius:4px"></td>
                            <td>#FIRE-{i:03d}</td>
                            <td>{time}</td>
                            <td>Nhiệt độ cao</td>
                            <td>{loc}</td>
                            <td><span style="color:var({status_color})">● {status}</span></td>
                             <td style="text-align:center">
                                <button class="action-btn-circle">👁️</button>
                                <button class="action-btn-circle">✎</button>
                                <button class="action-btn-circle">🗑️</button>
                            </td>
                        </tr>"""
    return grid_html, table_html

def generate_tilt_items(count=9):
    grid_html = ""
    table_html = ""
    for i in range(1, count + 1):
        col = random.randint(10, 99)
        loc = f"Tuyến 500kV - Cột {col}"
        time = get_random_date()
        img = 2
        tilt_val = round(3.0 + random.random() * 5, 1) # 3.0 to 8.0
        status = "Nguy hiểm" if tilt_val > 5 else "Cảnh báo"
        badge_class = "alert-high" if tilt_val > 5 else "alert-med"
        
        grid_html += f"""
                <div class="card inc-card-new" style="padding: 15px;">
                    <div style="display:flex; justify-content:space-between; align-items:start">
                        <div class="inc-badge {badge_class}">Cảnh báo</div>
                        <div style="font-size:12px; color:var(--text-sub)">{time}</div>
                    </div>
                    <img src="images/cam-0{img}.png" class="inc-img" alt="Inc">
                    <div>
                        <div class="inc-title">Cột nghiêng - Cột {col}</div>
                        <div class="inc-info-row">
                             <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            {loc}
                        </div>
                        <div class="inc-info-row">CAM: {get_random_cam()}</div>
                    </div>
                    <div class="tilt-stat">
                        <div>Thực tế: <span class="tilt-val" style="color:var(--danger)">{tilt_val}°</span></div>
                        <div class="tilt-limit">Ngưỡng: 3.0°</div>
                    </div>
                    <div style="margin-top:auto; padding-top:10px; border-top:1px solid var(--border); display:flex; justify-content:flex-end; gap:10px">
                        <button style="background:transparent; border:none; cursor:pointer">👁️</button>
                        <button style="background:transparent; border:none; cursor:pointer">✏️</button>
                    </div>
                </div>"""

        table_html += f"""
                        <tr>
                            <td>{i}</td>
                            <td><img src="images/cam-0{img}.png" style="width:60px; height:40px; border-radius:4px"></td>
                            <td>{get_random_cam()}</td>
                            <td>{time}</td>
                            <td>Cột {col}</td>
                            <td>{tilt_val}°</td>
                            <td style="color:var(--text-sub)">3.0°</td>
                             <td style="color: orange; font-weight:700">Nghiêng</td>
                             <td style="text-align:right">
                                <button class="action-btn-circle">👁️</button>
                                <button class="action-btn-circle">✎</button>
                            </td>
                        </tr>"""
    return grid_html, table_html

def generate_height_items(count=9):
    grid_html = ""
    table_html = ""
    for i in range(1, count + 1):
        col = random.randint(20, 40)
        loc = f"Phú Quốc - Khoảng cột {col}-{col+1}"
        time = get_random_date()
        img = 3
        percent = random.randint(50, 150)
        status = "Vượt" if percent > 100 else "Cảnh báo"
        badge = f"Vượt {percent-100}%" if percent > 100 else f"Cao {percent}%"
        badge_class = "alert-high" if percent > 100 else "alert-med"
        
        grid_html += f"""
                <div class="card inc-card-new" style="padding: 15px;">
                    <div style="display:flex; justify-content:space-between; align-items:start">
                        <div class="inc-badge {badge_class}">{badge}</div>
                        <div style="font-size:12px; color:var(--text-sub)">{time}</div>
                    </div>
                    <img src="images/cam-0{img}.png" class="inc-img" alt="Inc">
                    <div>
                        <div class="inc-title">Xe cơ giới vi phạm chiều cao</div>
                        <div class="inc-info-row">
                             <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            {loc}
                        </div>
                        <div class="inc-info-row">BS: 29H-{random.randint(100,999)}.{random.randint(10,99)}</div>
                    </div>
                    <div style="margin-top:auto; padding-top:10px; border-top:1px solid var(--border); display:flex; justify-content:flex-end; gap:10px">
                        <button style="background:transparent; border:none; cursor:pointer">👁️</button>
                        <button style="background:transparent; border:none; cursor:pointer">✏️</button>
                    </div>
                </div>"""

        table_html += f"""
                        <tr>
                            <td>{i}</td>
                            <td><img src="images/cam-0{img}.png" class="evidence-thumb"></td>
                             <td><div style="font-size:12px; cursor:pointer">▶️ Xem</div></td>
                            <td>{time}</td>
                            <td>29H-{random.randint(100,999)}.{random.randint(10,99)}</td>
                            <td>Phú Quốc</td>
                             <td>{get_random_cam()}</td>
                            <td style="color: grey">100%</td>
                            <td style="color: #ef4444; font-weight:700">{percent}%</td>
                             <td style="text-align:right">
                                <button class="action-btn">👁️</button>
                                <button class="action-btn">✏️</button>
                            </td>
                        </tr>"""
    return grid_html, table_html

def generate_beacon_items(count=9):
    grid_html = ""
    table_html = ""
    types = ["Mất tín hiệu", "Pin yếu", "Lỗi bộ sạc", "Hỏng đèn"]
    
    for i in range(1, count + 1):
        t = random.choice(types)
        col = random.randint(1, 50)
        loc = f"Đèn Beacon Cột {col}"
        time = get_random_date()
        img = 1
        tag_class = "tag-signal" if "tín hiệu" in t else ("tag-battery" if "Pin" in t else "tag-power")
        
        grid_html += f"""
                <div class="card inc-card-new" style="padding: 15px;">
                    <div style="display:flex; justify-content:space-between; align-items:start">
                        <div class="inc-badge {tag_class}">🚨 {t.upper()}</div>
                        <div style="font-size:12px; color:var(--text-sub)">{time}</div>
                    </div>
                    <img src="images/cam-0{img}.png" class="inc-img" alt="Inc">
                    <div>
                        <div class="inc-title">{loc}</div>
                        <div class="inc-info-row">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            Phú Quốc
                        </div>
                         <div class="inc-info-row">
                             <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
                             {t}
                        </div>
                    </div>
                     <div style="margin-top:auto; padding-top:10px; border-top:1px solid var(--border); display:flex; justify-content:space-between; align-items:center">
                        <span style="font-size:12px; color:var(--warning)">● Đang theo dõi</span>
                         <div style="display:flex; gap:10px">
                             <button class="action-btn">👁️</button>
                             <button class="action-btn">✏️</button>
                        </div>
                    </div>
                </div>"""
        
        table_html += f"""
                        <tr>
                            <td>{i}</td>
                            <td><img src="images/cam-0{img}.png" class="evidence-thumb"></td>
                            <td>{time}</td>
                            <td>{loc}</td>
                            <td>Phú Quốc</td>
                             <td><span style="color:#ef4444; font-weight:700">{t}</span></td>
                            <td class="inc-actions">
                                <button class="action-btn">👁️</button>
                                <button class="action-btn">✏️</button>
                                <button class="action-btn">🗑️</button>
                            </td>
                        </tr>"""
    return grid_html, table_html

def update_file(filename, grid_content, table_content):
    filepath = os.path.join(target_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex Replacement
    # Grid
    new_content = re.sub(
        r'(<div id="cardView" class="incident-grid-new">)(.*?)(</div>\s*<!-- Table View -->)', 
        f'\\1\n{grid_content}\n\\3', 
        content, 
        flags=re.DOTALL
    )
    
    # Table (Find tbody)
    new_content = re.sub(
        r'(<tbody.*?>)(.*?)(</tbody>)', 
        f'\\1\n{table_content}\n\\3', 
        new_content, 
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename} with 9 Demo Items")

def main():
    # 1. danh_sach_su_co.html
    g, t = generate_mix_items(9)
    update_file("danh_sach_su_co.html", g, t)
    
    # 2. quan_ly_su_co_doi_tuong.html
    g, t = generate_object_items(9)
    update_file("quan_ly_su_co_doi_tuong.html", g, t)
    
    # 3. quan_ly_su_co_chieu_cao_chay_khoi.htm
    g, t = generate_fire_items(9)
    update_file("quan_ly_su_co_chieu_cao_chay_khoi.htm", g, t)
    
    # 4. quan_ly_su_co_do_nghieng.html
    g, t = generate_tilt_items(9)
    update_file("quan_ly_su_co_do_nghieng.html", g, t)
    
    # 5. quan_ly_su_co_chieu_cao_an_toan.html
    g, t = generate_height_items(9)
    update_file("quan_ly_su_co_chieu_cao_an_toan.html", g, t)
    
    # 6. bao_cao_su_co_den_hieu.html
    g, t = generate_beacon_items(9)
    update_file("bao_cao_su_co_den_hieu.html", g, t)

if __name__ == "__main__":
    main()
