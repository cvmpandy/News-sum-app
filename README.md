# News Summarization App

**News Summarization App** is a Python and Flask-based application that fetches, scrapes, analyzes, and summarizes news articles using advanced natural language processing (NLP) techniques. Built using NewsAPI and Hugging Face's BART model, it processes and condenses information across various categories, offering users clear and concise summaries.

## Features

*  **News Fetching & Scraping**: Integrates with NewsAPI and uses BeautifulSoup to extract news content.
*  **Abstractive Summarization**: Leverages Hugging Face’s BART model to generate high-quality summaries.
*  **Topic Modeling**: Implements Latent Dirichlet Allocation (LDA) using Gensim to identify dominant topics in articles.
*  **Category Filtering**: Processes over 50 articles across 6 different categories.
*  **Performance**: Achieves average summarization accuracy of 85%.
*  **Visualizations**: Generates topic distribution charts and word clouds for deeper insights.

##  Tech Stack

* **Python**
* **Flask**
* **BART (Hugging Face Transformers)**
* **Gensim**
* **BeautifulSoup**
* **Matplotlib / WordCloud / pyLDAvis**

##  Project Structure

```
News-sum-app2.0/
├── app.py                     # Flask backend application
├── templates/
│   └── index.html            # Frontend template
├── static/
│   ├── style.css             # Custom styles
├── requirements.txt          # List of dependencies
News_Summarization_App.ipynb  # Jupyter notebook for experimentation
```

##  Setup Instructions

### Prerequisites

* Python 3.x
* pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cvmpandy/News-sum-app.git
   cd News-sum-app
   ```
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:

   ```bash
   python app.py
   ```
5. Open your browser and go to `http://localhost:5000`

##  Usage

* Choose a category to fetch news articles.
* View summarized news with topic visualizations.
* Explore topic distributions and word clouds to analyze trends.


