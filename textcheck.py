import tkinter as tk
import re
from langdetect import detect
from pykakasi import kakasi
import hgtk


def check_text():
    output_field.delete("1.0", "end")  # clear the output field
    text = input_field.get("1.0", "end-1c")  # get text from input field
    lang = detect(text)  # detect language of text

    # apply language-specific corrections
    if lang == "en":
        text = correct_english(text)
    elif lang == "es":
        text = correct_spanish(text)
    elif lang == "fr":
        text = correct_french(text)
    elif lang == "ja":
        text = correct_japanese(text)
    elif lang == "ko":
        text = correct_korean(text)
    elif lang == "tr":
        text = correct_turkish(text)
    # add more language-specific corrections here

    output_field.insert("end", f"Language: {lang}\n\n{text}")  # display language and corrected text in output field


def clear_all():
    input_field.delete("1.0", "end")  # clear the input field
    output_field.delete("1.0", "end")  # clear the output field


def correct_english(text):
    # replace straight quotes with curly quotes
    text = re.sub(r'"([^"]+)"', r'“\1”', text)
    text = re.sub(r"'([^']+)'", r'‘\1’', text)

    # add spaces after punctuation marks
    text = re.sub(r'(?<=[^\s])([.,:;?!])', r' \1', text)

    # remove extra spaces
    text = re.sub(r'\s+', r' ', text)

    return text


def correct_spanish(text):
    # replace straight quotes with curly quotes
    text = re.sub(r'"([^"]+)"', r'“\1”', text)
    text = re.sub(r"'([^']+)'", r'‘\1’', text)

    # add spaces after punctuation marks
    text = re.sub(r'(?<=[^\s])([.,:;?!¿¡])', r' \1', text)

    # remove extra spaces
    text = re.sub(r'\s+', r' ', text)

    return text


def correct_french(text):
    # replace straight quotes with curly quotes
    text = re.sub(r'"([^"]+)"', r'« \1 »', text)
    text = re.sub(r"'([^']+)'", r'‘\1’', text)

    # add spaces after punctuation marks
    text = re.sub(r'(?<=[^\s])([.,:;?!])', r' \1', text)

    # remove extra spaces
    text = re.sub(r'\s+', r' ', text)

    # add non-breaking space before some punctuation marks
    text = re.sub(r' ([!?;:»%])', r' \1', text)

    return text


def correct_japanese(text):
    # convert hiragana to katakana
    # text = hgtk.text.text_to_kana(text)

    # convert katakana to romaji
    # kakasi_instance = kakasi()
    # kakasi_instance.setMode("H", "a")
    # kakasi_instance.setMode("K", "a")
    # kakasi_instance.setMode("J", "a")
    # conv = kakasi_instance.get
    # kakasi_instance.setMode("J", "a")
    # kakasi_instance.setMode("s", True)
    # conv.convert(text)
    # result = conv.result

    # add spaces after punctuation marks
    result = re.sub(r'(?<=[^\s])([。、！？])', r' \1', result)

    # remove extra spaces
    result = re.sub(r'\s+', r' ', result)

    return result
def correct_korean(text):

    # add spaces after punctuation marks
    text = re.sub(r'(?<=[^\s])([.?!])', r' \1', text)

    # remove extra spaces
    text = re.sub(r'\s+', r' ', text)

    return text
def correct_turkish(text):

    # replace straight quotes with curly quotes
    text = re.sub(r'"([^"]+)"', r'“\1”', text)
    text = re.sub(r"'([^']+)'", r'‘\1’', text)
    # add spaces after punctuation marks
    text = re.sub(r'(?<=[^\s])([.,:;?!])', r' \1', text)

    # remove extra spaces
    text = re.sub(r'\s+', r' ', text)

    # add non-breaking space after some words
    text = re.sub(r' (için|ile|ve|veya|ya da|gibi|göre|dolayı|ise|değil)', r' \1', text)

    return text

root = tk.Tk()
root.geometry("500x400")
root.title("Text Checker")

# set app icon and taskbar icon
icon_path = "ico.ico"
icon_taskbar_path = "ico_taskbar.bmp"
root.iconbitmap(default=icon_path)
root.wm_iconbitmap(bitmap=icon_taskbar_path)

input_field = tk.Text(root, height=10, width=60)
input_field.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

check_button = tk.Button(button_frame, text="Check text", command=check_text)
check_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear all", command=clear_all)
clear_button.pack(side=tk.LEFT, padx=5)

output_field = tk.Text(root, height=10, width=60)
output_field.pack(pady=10)

root.mainloop()
