
# Investment Summary App
For english please see below.

## Przegląd

**Investment Summary App** to przyjazna dla użytkownika aplikacja desktopowa, zaprojektowana do analizy i porównywania strategii inwestycyjnych opisanych w plikach PDF. Wykorzystując API GPT firmy OpenAI, aplikacja wydobywa tekst z PDF-ów, podsumowuje treści i dostarcza szczegółowe porównania między wieloma strategiami inwestycyjnymi.

To narzędzie jest idealne dla każdego, kto chce uprościć proces analizy inwestycji i szybko zdobyć wgląd w dokumenty.

---

## Funkcje

- **Analiza plików PDF**: Wydobywanie tekstu z plików PDF do dalszej analizy.
- **Podsumowanie strategii inwestycyjnych**: Generowanie zwięzłych podsumowań strategii inwestycyjnych za pomocą API GPT firmy OpenAI.
- **Porównanie strategii**: Dostarczanie szczegółowych porównań między strategiami.
- **Możliwość konfiguracji klucza API**: Wprowadzenie i bezpieczne zapisywanie klucza API OpenAI.
- **Eksport wyników**: Zapisywanie podsumowań i porównań do pliku `.txt`.
- **Intuicyjny interfejs GUI**: Prosty i łatwy w obsłudze interfejs zbudowany z użyciem `Tkinter`.

---

## Wymagania

### Wymagania programowe:
- Python 3.7 lub nowszy
- Wymagane biblioteki Pythona:
  - `openai`
  - `PyPDF2`
  - `python-dotenv`
  - `tkinter` (zainstalowany domyślnie z Pythonem)

Jeśli aplikacja nie działa, należy zainstalować wymagane biblioteki Pythona za pomocą poniższego polecenia:
```bash
pip install openai PyPDF2 python-dotenv
```

---

## Instalacja

1. **Pobierz aplikację**:
   - Pobierz plik `investment_sumary_app.exe` z sekcji [Releases](https://github.com/biggda76/investment_summarizer/releases)

2. **Uruchom aplikację**:
   - Kliknij dwukrotnie plik `investment_sumary_app.exe`, aby uruchomić aplikację.

3. **Pierwsza konfiguracja**:
   - Podczas pierwszego uruchomienia aplikacja poprosi o wprowadzenie klucza API OpenAI. Klucz zostanie bezpiecznie zapisany w pliku `.env` znajdującym się w tym samym katalogu co aplikacja, do przyszłego użytku.

---

## Instrukcja obsługi

1. **Uruchom aplikację**:
   Uruchom aplikację, klikając dwukrotnie plik `investment_sumary_app.exe` lub wykonaj skrypt:
   ```bash
   python investment_summary_app.py
   ```

2. **Wprowadź klucz API**:
   Jeśli nie podałeś jeszcze klucza API, aplikacja poprosi o jego wprowadzenie. Wpisz klucz API OpenAI, a zostanie on zapisany do przyszłego użytku.

3. **Wybierz folder**:
   Użyj przycisku "Wybierz folder z dokumentami", aby wybrać folder zawierający pliki PDF.

4. **Wyświetl podsumowania i porównania**:
   Po przetworzeniu plików podsumowania i porównania zostaną wyświetlone w oknie aplikacji.

5. **Eksport wyników**:
   Użyj przycisku "Eksportuj", aby zapisać wyniki w pliku `.txt`.

---

## Przykładowy przebieg pracy

1. Otwórz aplikację.
2. Wprowadź klucz API OpenAI.
3. Wybierz folder z plikami PDF.
4. Wyświetl podsumowania strategii inwestycyjnych.
5. Wyeksportuj wyniki do późniejszego wykorzystania.

---

## Funkcje aplikacji w skrócie

| Funkcja                | Opis                                                   |
|------------------------|--------------------------------------------------------|
| Analiza plików PDF     | Wydobywanie treści z dokumentów PDF.                   |
| Podsumowanie strategii | Tworzenie zrozumiałych podsumowań w języku polskim.    |
| Porównanie strategii   | Szczegółowe porównania strategii inwestycyjnych.       |
| Zapisywanie wyników    | Eksport wyników do pliku `.txt`.                       |
| Intuicyjna konfiguracja klucza API | Bezpieczne zapisywanie klucza OpenAI.      |

---

## Struktura plików

```plaintext
investment-summary-app/
├── investment_summary_app.py   # Główny skrypt aplikacji
├── .env                        # Automatycznie generowany plik środowiska dla klucza API
├── requirements.txt            # Lista zależności Pythona
└── README.md                   # Dokumentacja
```

---

## Wykorzystana technologia

| Technologia  | Cel                        | Wersja        |
|--------------|----------------------------|---------------|
| Python       | Backend, rozwój aplikacji  | 3.13.1        |
| OpenAI API   | Analiza danych dokumentów  | gpt-3.5-turbo |

---

## Znane problemy

- Przetwarzanie dużych plików PDF lub dokumentów z nadmiarem treści może być wolniejsze.
- Nieprawidłowe klucze API OpenAI spowodują błędy.
- W przypadku zbyt dużych plików aplikacja może nie być w stanie przetworzyć całości dokumentu.

---

## Przyszłe ulepszenia

- Dodanie obsługi pobierania plików z internetu.
- Poprawa obsługi błędów dla uszkodzonych lub zaszyfrowanych plików PDF.
- Wprowadzenie możliwości analizy danych finansowych historycznych oraz ich pobierania z internetu.
- Ustawienie limitu dziennej liczby uruchomień przetwarzania dla użytkownika.

---

## Współpraca

Współpraca jest mile widziana! Aby wnieść wkład:
1. Sforkuj repozytorium.
2. Utwórz gałąź funkcjonalności (`git checkout -b nazwa-funkcjonalnosci`).
3. Zatwierdź swoje zmiany (`git commit -m "Dodano funkcjonalność"`).
4. Wypchnij na gałąź (`git push origin nazwa-funkcjonalnosci`).
5. Otwórz Pull Request.

---

## Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT. Szczegóły znajdziesz w pliku [LICENSE](LICENSE).

---

## Autorzy

Aplikacja został wykonany przez Bogdan Łaszyn

---

## Wsparcie

W przypadku pytań lub problemów prosimy o kontakt na [b.laszyn.151@studms.ug.edu.pl] bądź [laszyn.2000@gmail.com] lub otwarcie zgłoszenia w serwisie GitHub.

---

## Podziękowania

- [OpenAI](https://openai.com) za API GPT.
- [PyPDF2](https://pypi.org/project/PyPDF2/) za wydobywanie tekstu z plików PDF.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) za interfejs graficzny.

---



-------------------------------------------------------------------------------------------------------------------------------------
# English Version
# Investment Summary App

## Overview

The **Investment Summary App** is a user-friendly desktop application designed to analyze and compare investment strategies described in PDF files. Powered by OpenAI's GPT API, the app extracts text from PDFs, summarizes the content and provides detailed comparisons between multiple investment strategies. 

This tool is perfect for anyone looking to simplify their investment analysis process and quickly gather insights from documents.

---

## Features

- **Analyze PDF Files**: Extract text from PDF files for further analysis.
- **Summarize Investment Strategies**: Generate concise summaries of investment strategies using OpenAI's GPT API.
- **Compare Strategies**: Provide detailed comparisons between multiple strategies.
- **Customizable API Key**: Input and save your OpenAI API key securely.
- **Export Results**: Save summarized and compared results to a `.txt` file.
- **Intuitive GUI**: Simple and easy-to-use interface built with `Tkinter`.

---

## Requirements

### Software Requirements:
- Python 3.7 or higher
- Required Python libraries:
  - `openai`
  - `PyPDF2`
  - `python-dotenv`
  - `tkinter` (pre-installed with Python)

In case software doesn't run, please install the necessary Python libraries, use the following command:
```bash
pip install openai PyPDF2 python-dotenv
```

---

## Installation

1. **Download the Application**:
   - Download the `investment_sumary_app.exe` file from the [Releases](https://github.com/biggda76/investment_summarizer/releases) section (replace with your GitHub link).

2. **Run the Application**:
   - Double-click the `investment_sumary_app.exe` file to launch the application.

3. **First-Time Setup**:
   - On the first run, the application will prompt you to input your OpenAI API key. The key will be securely saved in a `.env` file located in the same directory as the app for future use.

---

## Usage Instructions

1. **Launch the App**:
   Run the application by double-clicking the `investment_sumary_app.exe` file or executing the script:
   ```bash
   python investment_summary_app.py
   ```

2. **Enter API Key**:
   If you haven't provided an API key, the app will prompt you to enter one. Input your OpenAI API key, and it will be saved for future use.

3. **Select Folder**:
   Use the "Wybierz folder z dokumentami" button to select a folder containing PDF files.

4. **View Summaries and Comparisons**:
   Once the files are processed, summaries and comparisons will be displayed in the application window.

5. **Export Results**:
   Use the "Eksportuj" button to save the results as a `.txt` file.

---

## Example Workflow

1. Open the application.
2. Enter your OpenAI API key.
3. Select a folder with PDF files.
4. View the summarized investment strategies.
5. Export the results for later reference.

---

## Application Features at a Glance

| Feature                 | Description                                              |
|-------------------------|----------------------------------------------------------|
| Analyze PDFs            | Extracts text content from PDF documents.                |
| Summarize Strategies    | Generates brief, easy-to-understand summaries in Polish. |
| Compare Strategies      | Compares investment strategies in detail.                |
| Save Results            | Exports results to a `.txt` file.                        |
| Intuitive API Key Setup | Input and save your OpenAI API key securely.             |

---

## File Structure

```plaintext
investment-summary-app/
├── investment_summary_app.py   # Main application script
├── .env                        # Automatically generated environment file for the API key
├── requirements.txt            # List of Python dependencies
└── README.md                   # Documentation
```

---

## Techonology used

| Technology   | Purpose                    | Version       |
|--------------|----------------------------|---------------|
| Python       | Backend, app development   | 3.13.1        |
| OpenAI API   | Document analysis          | gpt-3.5-turbo |

---

## Known Issues

- Large PDF files or documents with excessive content may cause slower processing.
- Invalid OpenAI API keys will result in errors.
- If given too large files app may not be able to process the entirety of document.

---

## Future Enhancements

- Add support for being able to download files from the web.
- Enhance error handling for corrupted or encrypted PDFs.
- Add support for being able to analyze historical financial data and download it from the web.
- Set a limit of how many times per day a user can run the processing.

---

## Testing

Tests for all functionalities were performed and can be found in the [Testy] directory

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Authors

This app was created by Bogdan Łaszyn
---

## Support

For questions or issues, please contact [b.laszyn.151@studms.ug.edu.pl] or [laszyn.2000@gmail.com] or open an issue on GitHub.

---

## Acknowledgments

- [OpenAI](https://openai.com) for the GPT API.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for text extraction from PDF files.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical interface.

---
