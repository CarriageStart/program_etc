import tkinter as tk
from tkinter import ttk
import pandas as pd

# 데이터프레임 초기화
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# 데이터프레임을 업데이트하는 함수
def update_table():
    for i in tree.get_children():
        tree.delete(i)
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

# 데이터 추가 함수
def add_data():
    global df
    new_data = {'Name': name_var.get(), 'Age': age_var.get(), 'City': city_var.get()}
    df = df.append(new_data, ignore_index=True)
    update_table()

# 데이터 삭제 함수
def delete_data():
    global df
    selected_item = tree.selection()[0]
    df = df.drop(tree.index(selected_item)).reset_index(drop=True)
    update_table()

# GUI 설정
root = tk.Tk()
root.title("Real-time Table Editor")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# 테이블 설정
tree = ttk.Treeview(frame, columns=("Name", "Age", "City"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("City", text="City")
tree.pack(fill="x", expand=True)

# 입력 필드 설정
name_var = tk.StringVar()
age_var = tk.IntVar()
city_var = tk.StringVar()

ttk.Label(frame, text="Name:").pack(fill="x", expand=True)
ttk.Entry(frame, textvariable=name_var).pack(fill="x", expand=True)
ttk.Label(frame, text="Age:").pack(fill="x", expand=True)
ttk.Entry(frame, textvariable=age_var).pack(fill="x", expand=True)
ttk.Label(frame, text="City:").pack(fill="x", expand=True)
ttk.Entry(frame, textvariable=city_var).pack(fill="x", expand=True)

# 버튼 설정
ttk.Button(frame, text="Add", command=add_data).pack(fill="x", expand=True, pady=5)
ttk.Button(frame, text="Delete", command=delete_data).pack(fill="x", expand=True, pady=5)

# 초기 테이블 업데이트
update_table()

root.mainloop()

