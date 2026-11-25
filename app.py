import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 1. 색상 리스트 구성
color_list_1 = ["빨강", "주황", "노랑", "초록", "파랑", "남색", "보라", "검정", "하양", "회색"]
color_list_2 = ["하양", "검정", "베이지", "연두", "하늘", "분홍", "갈색", "금색", "은색", "네이비"]

# 2. 색 조합 평가 및 혼합 결과 함수 ('상', '하'로만 구분)
def evaluate_combo(c1, c2):
    # 맑음수치 '하' 기준 (별로인 조합)
    bad_combos = [
        ("빨강", "초록"), ("초록", "빨강"), ("파랑", "주황"), ("주황", "파랑"),
        ("보라", "노랑"), ("노랑", "보라"), ("빨강", "분홍"), ("검정", "갈색"),
        ("주황", "분홍"), ("파랑", "연두")
    ]
    
    combo = (c1, c2)
    
    # bad_combos에 포함되면 '하', 그 외 모든 조합은 무조건 '상'
    if combo in bad_combos:
        score = "하"
    else:
        score = "상"
        
    # 혼합된 결과 색상 유추 로직
    if c1 == c2:
        mixed_color = c1
    elif c2 == "하양" or c1 == "하양":
        mixed_color = f"연한 {c1 if c2 == '하양' else c2}"
    elif c2 == "검정" or c1 == "검정":
        mixed_color = f"어두운 {c1 if c2 == '검정' else c2}"
    elif (c1=="빨강" and c2=="파랑") or (c1=="파랑" and c2=="분홍"):
        mixed_color = "보라"
    elif (c1=="노랑" and c2=="하늘") or (c1=="파랑" and c2=="연두"):
        mixed_color = "초록"
    else:
        mixed_color = f"{c1}빛 {c2}"
        
    return score, mixed_color

# 3. GUI 시스템 구성
def on_combine_click():
    c1 = combo1.get()
    c2 = combo2.get()
    
    if not c1 or not c2:
        messagebox.showwarning("입력 오류", "두 가지 색상을 모두 선택해주세요!")
        return
        
    score, mixed_color = evaluate_combo(c1, c2)
    
    # 표(Treeview)의 맨 윗줄(0번째 인덱스)에 최신 결과 추가
    tree.insert("", "0", values=(c1, c2, mixed_color, score))

# 메인 윈도우 생성
root = tk.Tk()
root.title("🎨 색깔 조합 가이드 시스템")
root.geometry("500x400")
root.configure(padx=20, pady=20)

# 상단 입력부 프레임
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="리스트 1:").grid(row=0, column=0, padx=5)
combo1 = ttk.Combobox(input_frame, values=color_list_1, state="readonly", width=10)
combo1.grid(row=0, column=1, padx=5)
combo1.set("빨강")

tk.Label(input_frame, text=" + ").grid(row=0, column=2, padx=5)

tk.Label(input_frame, text="리스트 2:").grid(row=0, column=3, padx=5)
combo2 = ttk.Combobox(input_frame, values=color_list_2, state="readonly", width=10)
combo2.grid(row=0, column=4, padx=5)
combo2.set("하양")

# 조합하기 버튼
btn_combine = tk.Button(root, text="✨ 조합하기", command=on_combine_click, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black", pady=5)
btn_combine.pack(pady=15)

# 하단 결과 표(Treeview) 프레임
columns = ("color1", "color2", "mixed", "score")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

tree.heading("color1", text="선택 색상 1")
tree.heading("color2", text="선택 색상 2")
tree.heading("mixed", text="결과 색상")
tree.heading("score", text="맑음 수치")

tree.column("color1", width=80, anchor="center")
tree.column("color2", width=80, anchor="center")
tree.column("mixed", width=150, anchor="center")
tree.column("score", width=80, anchor="center")

tree.pack(fill="x")

root.mainloop()
