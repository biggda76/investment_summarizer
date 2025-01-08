import os
import openai
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
from dotenv import load_dotenv, set_key

# Dopasowanie sciezki gdzie plik .env zostanie zapisany w sciezce z aplikacja
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, ".env")

# Wczytanie srodowiska z kluczem
load_dotenv(env_path)


def get_api_key(root):
    """Popup aby zapytac uzytkownika o jego klucz OpenAI API."""
    def save_key():
        api_key = api_key_entry.get().strip()
        if not api_key:
            messagebox.showerror("Błąd", "Klucz API nie może być pusty!")
            return
        try:
            # Zapis klucza do srodowiska
            set_key(env_path, "OPENAI_API_KEY", api_key)
            openai.api_key = api_key
            popup.destroy()
            initialize_app(root)  # Uruchomienie ponowne aplikacji po zapisaniu klucza
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać klucza API: {str(e)}")

    # Utworzenie okienka na wprowadzenie klucza
    popup = tk.Toplevel(root)
    popup.title("Wprowadź klucz API")
    popup.geometry("400x200")
    tk.Label(popup, text="Wprowadź swój OpenAI API Key:", font=("Arial", 12)).pack(pady=10)

    api_key_entry = tk.Entry(popup, width=40, show="*")
    api_key_entry.pack(pady=5)

    save_button = tk.Button(popup, text="Zapisz", command=save_key)
    save_button.pack(pady=10)

    popup.transient(root)  # Integracja popup z root
    popup.grab_set()
    popup.protocol("WM_DELETE_WINDOW", lambda: root.destroy())  # Zamkniecie protkolu jesli okno bedzie zamkniete


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
    prompt = f"Podsumuj po polsku strategie inwestycyjna opisana w nastepujacym tekscie:\n\n{text}\n\nSummary:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jestes asystentem analizy finansowej."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=2000
    )
    return response['choices'][0]['message']['content']


def compare_summaries(summaries):
    """Porownaj strategie inwestycyjne przy uzyciu OpenAI API."""
    comparison_prompt = "Porownaj po polsku nastepujace strategie inwestycyjne:\n\n"
    for i, summary in enumerate(summaries):
        comparison_prompt += f"Strategia {i + 1}:\n{summary}\n\n"
    comparison_prompt += "Podaj po polsku dokladne porownanie miedzy strategiami inwestycyjnymi:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jestes asystentem analizy finansowej."},
            {"role": "user", "content": comparison_prompt}
        ],
        temperature=0.1,
        max_tokens=2000
    )
    return response['choices'][0]['message']['content']


def process_pdfs(folder_path, output_text, processing_label):
    """Przeanalizuj pliki PDF zawarte w wybranym folderze."""
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    summaries = []

    # Wyswietlanie informacji "Przetwarzanie..."
    processing_label.config(text="Przetwarzanie w toku...")
    processing_label.update_idletasks()

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
            output_text.insert(tk.END, "Porownanie strategii inwestycyjnych:\n")
            output_text.insert(tk.END, f"{comparison}\n")
        except Exception as e:
            output_text.insert(tk.END, f"Blad podczas porownywania strategii inwestycyjnych: {e}\n")

    processing_label.config(text="Przetwarzanie zakończone.")

   # Usun wiadomosc "Przetwarzanie..." po zakonczeniu
    processing_label.config(text="")

def export_to_txt(output_text):
    """Eksportuj tekst outputu do pliku TXT."""
    # Zbieranie tekstu z calego widoku outputu
    output = output_text.get(1.0, tk.END).strip()
    if not output:
        messagebox.showerror("Błąd", "Brak danych do eksportu.")  # Wyswietl blad jesli nie ma danych
        return

    # Otworz sciezke gdzie zapisac plik txt
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Zapisz jako plik TXT"
    )
    if not file_path:
        return

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output)
        messagebox.showinfo("Sukces", f"Dane zostały zapisane jako plik TXT: {file_path}")
    except Exception as e:
        # Pokaz bledy jesli wystapia przy procesie zapisywania pliku
        messagebox.showerror("Błąd", f"Wystąpił problem podczas eksportu: {str(e)}")


def select_folder(output_text, processing_label):
    """Otworz okno w celu wybrania folderu i analizy plikow PDF."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_text.delete(1.0, tk.END)
        process_pdfs(folder_path, output_text, processing_label)


def initialize_app(root):
    """Uruchom glowna aplikacje."""
    output_text = tk.Text(root, wrap=tk.WORD, height=30, width=90)
    output_text.pack(padx=10, pady=10)

    # Tworzenie napisu "Przetwarzanie..."
    processing_label = tk.Label(root, text="", fg="red")
    processing_label.pack(pady=5)

    # Tworzenie przycisku do wyboru folderu
    select_folder_button = tk.Button(root, text="Wybierz folder z dokumentami", command=lambda: select_folder(output_text, processing_label))
    select_folder_button.pack(pady=10)

    # Tworzenie przycisku do eksportu tekstu do pliku TXT
    export_button = tk.Button(root, text="Eksportuj", command=lambda: export_to_txt(output_text))
    export_button.pack(pady=10)


def main():
    """Stworz aplikacje GUI."""
    global root
    root = tk.Tk()
    root.title("Investment Summary App")
    root.geometry("800x650")

    # Sprawdzenie klucza
    if not os.getenv("OPENAI_API_KEY"):
        get_api_key(root)
    else:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        initialize_app(root)

    root.mainloop()


if __name__ == "__main__":
    main()
