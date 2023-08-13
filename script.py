import os
import argparse
import csv
import joblib
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def categorize_resume(resume, model, vectorizer):
    features = vectorizer.transform([resume])
    return model.predict(features)[0]

def process_directory(dir_path, model, vectorizer):
    output_csv = os.path.join(dir_path, "categorized_resumes.csv")

    with open(output_csv, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['filename', 'category'])

        for filename in os.listdir(dir_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(dir_path, filename)
                content = extract_text_from_pdf(file_path)
                category = categorize_resume(content, model, vectorizer)
                csvwriter.writerow([filename, category])

                dest_dir = os.path.join(dir_path, category)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                os.rename(file_path, os.path.join(dest_dir, filename))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process and categorize resumes')
    parser.add_argument('dir_path', type=str, help='Path to the directory containing resumes')
    args = parser.parse_args()

    
    model = joblib.load('artifacts/logistic_regression_model.pkl')
    vectorizer = joblib.load('artifacts/vectorizer.pkl')

    process_directory(args.dir_path, model, vectorizer)
