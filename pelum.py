import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the CSV file containing resume data
file_path = 'UpdatedResumeDataSet.csv'
data = pd.read_csv(file_path)

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

# Display basic information about the dataset
print(data.head())
print(data.info())
print(data.describe(include='all'))
