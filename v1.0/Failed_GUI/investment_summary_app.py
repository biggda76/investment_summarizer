import os
import openai
import PyPDF2

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
        messages=[{"role": "user", "content": prompt}],
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
        messages=[{"role": "user", "content": comparison_prompt}],
        temperature=0.4,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

def main(directory):
    """Glowna funkcja do przetwarzania plikow PDF oraz podsumowania strategi inwestycyjnych."""
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    summaries = []
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        print(f"Przetwarzanie pliku: {pdf_file}")
        
        # Ekstrakcja tekstu z PDF
        text = extract_text_from_pdf(pdf_path)
        
        # Podsumowanie
        summary = summarize_text(text)
        summaries.append(summary)
        print(f"Podsumowanie dla pliku {pdf_file}:\n{summary}\n")
    
    # Porownanie podsumowania
    comparison = compare_summaries(summaries)
    print("Porownanie strategii inwestycyjnych:\n")
    print(comparison)

if __name__ == "__main__":
    import sys
    # Sprawdzenie GUI
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        from investment_gui import run_gui
        run_gui()
    else:
    # Ustawienie sciezki zawierajacej dokumenty PDF
    pdf_directory = r"C:\Users\laszy\Desktop\Semestr 9\Inżynieria oprogramowania\Ćwiczenia\investment_summarizer\investment_summarizer"  # Sciezka zawierajaca dokumenty do porownania
    main(pdf_directory)
