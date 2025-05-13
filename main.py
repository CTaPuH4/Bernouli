import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


# ЗАДАЧА 1
def solve_task_1():
    try:
        m = float(entry1_m.get())
        r = float(entry1_r.get())
        T0 = float(entry1_T0.get())
        T = float(entry1_T.get())
        T_env = 0

        h = 20
        ε = 0.8
        c = 880
        σ = 5.67e-8

        A = 4 * np.pi * r**2
        k = (h + 4 * ε * σ * T_env**3) * A / (m * c)

        t_vals = np.linspace(0, 10000, 500)
        T_vals = T_env + (T0 - T_env) * np.exp(-k * t_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(t_vals, T_vals, label='Температура шара', color='orange')
        plt.axhline(
            T, color='gray', linestyle='--', label='Искомая температура'
        )
        plt.title('Задача 1')
        plt.xlabel('Время (с)')
        plt.ylabel('Температура (K)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror('Ошибка', f'Ошибка в задаче 1:\n{e}')


# ЗАДАЧА 2
def solve_task_2():
    try:
        P0 = float(entry2_P0.get())
        r = float(entry2_r.get())
        K = float(entry2_K.get())

        t_vals = np.linspace(0, 50, 500)
        P_vals = K / (1 + ((K - P0) / P0) * np.exp(-r * t_vals))

        plt.figure(figsize=(8, 5))
        plt.plot(t_vals, P_vals, label='Популяция', color='green')
        plt.title('Задача 2')
        plt.xlabel('Время (лет)')
        plt.ylabel('Численность (тыс. особей)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror('Ошибка', f'Ошибка в задаче 2:\n{e}')


# ЗАДАЧА 3
def solve_task_3():
    try:
        S = float(entry3_S.get())
        beta = float(entry3_beta.get())
        y0 = 30
        b = beta / S

        def bernoulli(t, a, b, y0):
            return 1 / ((b/a) + (1/y0 - b/a) * np.exp(-a * t))

        t_vals = np.linspace(0, 35, 400)
        model_vals = bernoulli(t_vals, beta, b, y0)

        days = np.array([0, 7, 9, 12, 14, 17, 20, 22, 25, 27, 30])
        real_cases = np.array([30, 400, 1208, 4349, 7417, 13748,
                               22942, 28985, 35982, 51591, 58016])

        plt.figure(figsize=(8, 5))
        plt.plot(t_vals, model_vals, label='Модель (Бернулли)', color='blue')
        plt.scatter(
            days, real_cases, color='red', label='Реальные данные', zorder=5
        )
        plt.title('Задача 3')
        plt.xlabel('Дни с 15 января 2020')
        plt.ylabel('Число активных случаев')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror('Ошибка', f'Ошибка в задаче 3:\n{e}')


# === GUI ===
root = tk.Tk()
root.title('Графики по задачам')
root.geometry('530x185')

# --- ЗАДАЧА 1 ---
frame1 = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame1.pack(fill=tk.X, padx=10, pady=5)

btn1 = tk.Button(frame1, text='Задача 1', command=solve_task_1)
btn1.grid(row=0, column=0, padx=5)

tk.Label(frame1, text='m (кг):').grid(row=0, column=1)
entry1_m = tk.Entry(frame1, width=10)
entry1_m.insert(0, '5')
entry1_m.grid(row=0, column=2)

tk.Label(frame1, text='r (м):').grid(row=0, column=3)
entry1_r = tk.Entry(frame1, width=10)
entry1_r.insert(0, '0.1')
entry1_r.grid(row=0, column=4)

tk.Label(frame1, text='T0 (K):').grid(row=0, column=5)
entry1_T0 = tk.Entry(frame1, width=10)
entry1_T0.insert(0, '500')
entry1_T0.grid(row=0, column=6)

tk.Label(frame1, text='T (K):').grid(row=0, column=7)
entry1_T = tk.Entry(frame1, width=10)
entry1_T.insert(0, '300')
entry1_T.grid(row=0, column=8)

# --- ЗАДАЧА 2 ---
frame2 = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame2.pack(fill=tk.X, padx=10, pady=5)

btn2 = tk.Button(frame2, text='Задача 2', command=solve_task_2)
btn2.grid(row=0, column=0, padx=5)

tk.Label(frame2, text='P0:').grid(row=0, column=1)
entry2_P0 = tk.Entry(frame2, width=10)
entry2_P0.insert(0, '50')
entry2_P0.grid(row=0, column=2)

tk.Label(frame2, text='r:').grid(row=0, column=3)
entry2_r = tk.Entry(frame2, width=10)
entry2_r.insert(0, '0.1')
entry2_r.grid(row=0, column=4)

tk.Label(frame2, text='K:').grid(row=0, column=5)
entry2_K = tk.Entry(frame2, width=10)
entry2_K.insert(0, '500')
entry2_K.grid(row=0, column=6)

# --- ЗАДАЧА 3 ---
frame3 = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame3.pack(fill=tk.X, padx=10, pady=5)

btn3 = tk.Button(frame3, text='Задача 3', command=solve_task_3)
btn3.grid(row=0, column=0, padx=5)

tk.Label(frame3, text='S:').grid(row=0, column=1)
entry3_S = tk.Entry(frame3, width=10)
entry3_S.insert(0, '60000')
entry3_S.grid(row=0, column=2)

tk.Label(frame3, text='β:').grid(row=0, column=3)
entry3_beta = tk.Entry(frame3, width=10)
entry3_beta.insert(0, '0.34')
entry3_beta.grid(row=0, column=4)

# --- Запуск ---
root.mainloop()
