import os
import openai
import PyPDF2

# Set your OpenAI API key
openai.api_key = "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"

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text):
    """Summarize text using OpenAI API."""
    prompt = f"Summarize the investment strategy described in the following text:\n\n{text}\n\nSummary:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']

def compare_summaries(summaries):
    """Compare investment strategies using OpenAI API."""
    comparison_prompt = "Compare the following investment strategies:\n\n"
    for i, summary in enumerate(summaries):
        comparison_prompt += f"Strategy {i + 1}:\n{summary}\n\n"
    comparison_prompt += "Provide a detailed comparison:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": comparison_prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

def main(directory):
    """Main function to process PDFs and summarize investment strategies."""
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    summaries = []
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        print(f"Processing file: {pdf_file}")
        
        # Extract text
        text = extract_text_from_pdf(pdf_path)
        
        # Summarize
        summary = summarize_text(text)
        summaries.append(summary)
        print(f"Summary for {pdf_file}:\n{summary}\n")
    
    # Compare summaries
    comparison = compare_summaries(summaries)
    print("Comparison of Investment Strategies:\n")
    print(comparison)

if __name__ == "__main__":
    # Set the directory containing PDF files
    pdf_directory = r"C:\Users\laszy\Desktop\Semestr 9\Inżynieria oprogramowania\Ćwiczenia\test"  # Replace with your PDF directory path
    main(pdf_directory)
