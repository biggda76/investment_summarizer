import os
import openai
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

# Klucz OpenAI - ChatGPT
openai.api_key = "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"

def extract_text_from_pdf(pdf_path):
    """Ekstraktuj tekst z pliku pdf."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text):
    """Podsumuj tekst zawarty w pliku za pomoca OpenAI API."""
    prompt = f"Podsumuj strategie inwestycyjna opisana w nastepujacym tekscie:\n\n{text}\n\nSummary:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jestes asystentem analizy finansowej."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']

def compare_summaries(summaries):
    """Porownaj strategie inwestycyjne przy uzyciu OpenAI API."""
    comparison_prompt = "Porownaj nastepujace strategie inwestycyjne:\n\n"
    for i, summary in enumerate(summaries):
        comparison_prompt += f"Strategia {i + 1}:\n{summary}\n\n"
    comparison_prompt += "Podaj dokladne porownanie miedzy strategiami inwestycyjnymi:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jestes asystentem analizy finansowej."},
            {"role": "user", "content": comparison_prompt}
        ],
        temperature=0.4,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

def process_pdfs(folder_path, output_text):
    """Przeanalizuj pliki PDF zawarte w wybranym folderze."""
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    summaries = []
    
    output_text.insert(tk.END, f"Przetwarzanie folderu: {folder_path}\n")
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        output_text.insert(tk.END, f"Przetwarzanie pliku: {pdf_file}\n")
        
        # Ekstrakcja tekstu
        text = extract_text_from_pdf(pdf_path)
        
        # Podsumowanie
        try:
            summary = summarize_text(text)
            summaries.append(summary)
            output_text.insert(tk.END, f"Podsumowanie dla {pdf_file}:\n{summary}\n\n")
        except Exception as e:
            output_text.insert(tk.END, f"Blad podczas przetwarzania {pdf_file}: {e}\n\n")
    
    if summaries:
        # Porownanie podsumowania
        try:
            comparison = compare_summaries(summaries)
            output_text.insert(tk.END, "Porownanie strategi inwestycyjnych:\n")
            output_text.insert(tk.END, f"{comparison}\n")
        except Exception as e:
            output_text.insert(tk.END, f"Blad podczas porownywania strategi inwestycyjnych: {e}\n")

def select_folder(output_text):
    """Otworz okno w celu wybrania folderu i analizy plikow PDF."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_text.delete(1.0, tk.END)  # Czyszczenie outputu
        process_pdfs(folder_path, output_text)

def main():
    """Stworz aplikacje GUI."""
    # Tworzenie glownego okna
    root = tk.Tk()
    root.title("Investment Summary App")
    root.geometry("800x600")

    # Tworzenie widetu tekstowego dla outputu
    output_text = tk.Text(root, wrap=tk.WORD, height=30, width=90)
    output_text.pack(padx=10, pady=10)

    # Tworzenie przycisku do wyboru folderu
    select_folder_button = tk.Button(root, text="Wybierz folder z dokumentami", command=lambda: select_folder(output_text))
    select_folder_button.pack(pady=10)

    # Loop
    root.mainloop()

if __name__ == "__main__":
    main()
