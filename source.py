# تم انشأ السكربت من قبل فريق "Chayper Zero Team"
# هذا السكربت هو مزحة تهكير وهمية لا تستخدمه ل اغراض غير قانونية
# chayper zero لا تتحمل مسؤولية اي استخدام غير قانوني
# مع تحياتي ل فريق chayper zero و مستخدمين هاذ السكربت
import tkinter as tk
from tkinter import messagebox
import random
import threading
import pygame
import pyautogui
import sys
import time
import keyboard
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1

fake_alerts = [
    ("تحذير أمني!", "تم اكتشاف فيروس خطير في النظام!"),
    ("خطأ نظام!", "حدث خلل غير متوقع، يرجى إعادة التشغيل!"),
    ("تنبيه!", "جهازك سيتم إغلاقه خلال 10 ثواني!"),
    ("مكافحة فيروسات", "تم اكتشاف ملف مشبوه، هل تريد حذفه؟"),
    ("تأكيد الدخول", "يرجى إدخال كلمة السر لتأكيد هويتك."),
    ("خطأ فادح!", "تم حظر التطبيق بسبب نشاط غير آمن!"),
]

class PrankApp:
    def __init__(self):
        self.stop_event = threading.Event()
        self.keyboard_hook = None
        self.windows = []
        self.root = None
        self.sound_initialized = False
        self.active_threads = []
        self.main_window = None

    def exit_program(self):
        try:
            self.stop_event.set()

            if self.sound_initialized:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                self.sound_initialized = False

            self.close_all_windows()
            self.enable_input()

        except Exception as e:
            print("Error during exit:", e)
        finally:
            os._exit(0)

    def initialize_sound(self):
        try:
            pygame.mixer.init()
            self.sound_initialized = True
        except Exception as e:
            print("Sound initialization error:", e)
            self.sound_initialized = False

    def play_sound(self):
        if not self.sound_initialized:
            self.initialize_sound()

        try:
            pygame.mixer.music.load(resource_path("hacking.mp3"))
            pygame.mixer.music.play(-1)
        except Exception as e:
            print("Error playing sound:", e)

    def stop_sound(self):
        if not self.sound_initialized:
            return

        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            self.sound_initialized = False
        except Exception as e:
            print("Error stopping sound:", e)

    def prank_mouse(self):
        while not self.stop_event.is_set():
            try:
                x = random.randint(0, pyautogui.size().width - 1)
                y = random.randint(0, pyautogui.size().height - 1)
                pyautogui.moveTo(x, y, duration=0.3)
                time.sleep(0.5)
            except Exception as e:
                print("Mouse prank error:", e)
                break

    def disable_input(self):
        try:
            if self.keyboard_hook is None:
                self.keyboard_hook = keyboard.hook(lambda e: True)
        except Exception as e:
            print("Error disabling input:", e)

    def enable_input(self):
        try:
            if self.keyboard_hook:
                keyboard.unhook(self.keyboard_hook)
                self.keyboard_hook = None
        except Exception as e:
            print("Error enabling input:", e)

    def annoying_window(self):
        while not self.stop_event.is_set():
            try:
                title, msg = random.choice(fake_alerts)

                win = tk.Toplevel()
                win.title(title)
                win.attributes("-topmost", True)
                win.resizable(False, False)

                width = random.randint(250, 350)
                height = random.randint(120, 150)
                screen_w = win.winfo_screenwidth()
                screen_h = win.winfo_screenheight()
                x = random.randint(0, screen_w - width)
                y = random.randint(0, screen_h - height)
                win.geometry(f"{width}x{height}+{x}+{y}")

                win.protocol("WM_DELETE_WINDOW", lambda: None)

                label = tk.Label(win, text=msg, font=("Arial", 12), fg="red")
                label.pack(pady=15)

                btn = tk.Button(win, text="إغلاق", command=lambda w=win: w.destroy())
                btn.pack(pady=5)

                self.windows.append(win)

                def auto_close():
                    time.sleep(4)
                    if not self.stop_event.is_set():
                        try:
                            if win.winfo_exists():
                                win.destroy()
                        except:
                            pass

                threading.Thread(target=auto_close, daemon=True).start()

                start_time = time.time()
                while time.time() - start_time < 4:
                    if self.stop_event.is_set():
                        try:
                            if win.winfo_exists():
                                win.destroy()
                        except:
                            pass
                        return
                    try:
                        win.update()
                    except:
                        break
                    time.sleep(0.1)

                if not self.stop_event.is_set():
                    time.sleep(0.5)

            except Exception as e:
                print("Window creation error:", e)
                if not self.stop_event.is_set():
                    time.sleep(1)

    def matrix_screen(self, duration=10):
        try:
            matrix_stop_event = threading.Event()

            self.root = tk.Toplevel()
            self.root.attributes("-fullscreen", True)
            self.root.configure(bg="black")
            self.root.attributes("-topmost", True)
            self.root.protocol("WM_DELETE_WINDOW", lambda: None)

            canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
            canvas.pack(fill="both", expand=True)

            w = self.root.winfo_screenwidth()
            h = self.root.winfo_screenheight()

            streams = []
            for _ in range(80):
                x = random.randint(0, w)
                y = random.randint(-h, 0)
                speed = random.uniform(6, 12)
                streams.append({"x": x, "y": y, "speed": speed})

            def animate():
                if self.stop_event.is_set() or matrix_stop_event.is_set():
                    try:
                        self.root.destroy()
                    except:
                        pass
                    return

                canvas.delete("all")
                for stream in streams:
                    for i in range(15):
                        digit_y = stream["y"] - i * 15
                        if 0 <= digit_y <= h:
                            color = "white" if i == 0 else "green"
                            canvas.create_text(
                                stream["x"], digit_y,
                                text=random.choice(["0", "1"]),
                                fill=color, font=("Consolas", 12, "bold")
                            )
                    stream["y"] += stream["speed"]
                    if stream["y"] - 15 * 15 > h:
                        stream["y"] = random.randint(-h, 0)
                        stream["x"] = random.randint(0, w)
                        stream["speed"] = random.uniform(6, 12)

                self.root.after(30, animate)

            threading.Timer(duration, matrix_stop_event.set).start()
            animate()

            while not matrix_stop_event.is_set() and not self.stop_event.is_set():
                try:
                    self.root.update()
                    time.sleep(0.03)
                except tk.TclError:
                    break

            if not self.stop_event.is_set():
                canvas.delete("all")
                canvas.create_text(
                    w // 2, h // 2,
                    text="تم تهكيرك",
                    fill="red",
                    font=("Arial", 48, "bold")
                )
                self.root.update()
                time.sleep(3)

        except Exception as e:
            print("Matrix screen error:", e)
        finally:
            self.stop_sound()
            self.exit_program()

    def close_all_windows(self):
        for win in self.windows:
            try:
                if win.winfo_exists():
                    win.destroy()
            except:
                pass
        self.windows.clear()

        if self.root is not None:
            try:
                self.root.destroy()
            except:
                pass
            self.root = None

        if self.main_window is not None:
            try:
                self.main_window.destroy()
            except:
                pass
            self.main_window = None

    def run_prank(self, duration=30):
        self.disable_input()

        mouse_thread = threading.Thread(target=self.prank_mouse, daemon=True)
        mouse_thread.start()
        self.active_threads.append(mouse_thread)

        annoying_thread = threading.Thread(target=self.annoying_window, daemon=True)
        annoying_thread.start()
        self.active_threads.append(annoying_thread)

        def stop_and_exit():
            self.stop_event.set()
            time.sleep(0.5)
            self.exit_program()

        threading.Timer(duration, stop_and_exit).start()

    def run(self):
        try:
            self.play_sound()

            self.main_window = tk.Tk()
            self.main_window.withdraw()

            answer = messagebox.askquestion("تنبيه", "لديك بيسي جميل = )\nهل تريد تدميره = )؟", icon="warning")

            if answer == "yes":
                self.run_prank(duration=30)
                self.main_window.mainloop()
            else:
                self.matrix_screen(duration=10)

        except Exception as e:
            print("Main error:", e)
        finally:
            self.exit_program()


if __name__ == "__main__":
    app = PrankApp()
    app.run()
