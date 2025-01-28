import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Path to the unzipped CSV file
file_path = 'UpdatedResumeDataSet.csv'

# Load the dataset
data = pd.read_csv(file_path)

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stopwords and stemmer
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Function to preprocess text
def preprocess_text(text):
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords and apply stemming
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    # Join words back into a single string
    return ' '.join(words)

# Apply the preprocessing function to the Resume column
data['Cleaned_Resume'] = data['Resume'].apply(preprocess_text)

# Sample Job Description for testing
job_description = "Looking for a Data Scientist with expertise in Python, Machine Learning, and Data Analysis."

# Combine job description with the cleaned resumes for TF-IDF
documents = [job_description] + data['Cleaned_Resume'].tolist()

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Compute Cosine Similarity between the job description and all resumes
cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Add similarity scores to the DataFrame
data['Similarity_Score'] = cosine_similarities

# Sort resumes by similarity scores in descending order
ranked_resumes = data.sort_values(by='Similarity_Score', ascending=False)

# Display top 5 ranked resumes with category, cleaned resume, and similarity score
print(ranked_resumes[['Category', 'Cleaned_Resume', 'Similarity_Score']].head())

# Display the first few rows of the cleaned resumes
print(data[['Category', 'Cleaned_Resume']].head())
s