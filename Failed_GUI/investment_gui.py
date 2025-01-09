import os
import tkinter as tk
from tkinter import filedialog
from investment_summary_app import extract_text_from_pdf, summarize_text, compare_summaries

def process_pdfs(folder_path, output_text):
    """Przetwarzaj pliki PDF zawarte w wybranych folderze."""
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    summaries = []

    output_text.insert(tk.END, f"Przetwarzanie folderu: {folder_path}\n")
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        output_text.insert(tk.END, f"Przetwarzanie pliku: {pdf_file}\n")
        
        # Ekstrakcja tekstu z PDF
        text = extract_text_from_pdf(pdf_path)
        
        # Podsumowanie tekstu
        try:
            summary = summarize_text(text)
            summaries.append(summary)
            output_text.insert(tk.END, f"Podsumowanie dla pliku {pdf_file}:\n{summary}\n\n")
        except Exception as e:
            output_text.insert(tk.END, f"Blad podczas przetwarzania {pdf_file}: {e}\n\n")
    
    if summaries:
        # Porownaj podsumowanie
        try:
            comparison = compare_summaries(summaries)
            output_text.insert(tk.END, "Porownanie strategii inwestycyjnych:\n")
            output_text.insert(tk.END, f"{comparison}\n")
        except Exception as e:
            output_text.insert(tk.END, f"Blad podczas porownania strategi: {e}\n")

def select_folder(output_text):
    """Otworz okno w celu wybrania folderu oraz przetworzeniu plikow PDF."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_text.delete(1.0, tk.END)  # Clear output
        process_pdfs(folder_path, output_text)

def run_gui():
    """Stworz aplikacje GUI."""
    # Tworzenie glownego okna
    root = tk.Tk()
    root.title("Investment Summary App")
    root.geometry("800x600")

    # Tworzenie widgetu tekstowego dla outputu
    output_text = tk.Text(root, wrap=tk.WORD, height=30, width=90)
    output_text.pack(padx=10, pady=10)

    # Wybor folderu za pomoca przycisku
    select_folder_button = tk.Button(root, text="Wybierz Folder", command=lambda: select_folder(output_text))
    select_folder_button.pack(pady=10)

    # Loop
    root.mainloop()
