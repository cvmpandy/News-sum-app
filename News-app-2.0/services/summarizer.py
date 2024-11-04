# services/summarizer.py
from transformers import pipeline

# Initialize the summarization pipeline
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize_text(text):
    if text:
        # Generate the summary using the pipeline
        summary = summarizer_pipeline(
            text, max_length=200, min_length=150, do_sample=False
        )

        # Prepare the result containing original text and summary

        # return {"original_text": text, "summary": summary[0]["summary_text"]}
        return summary[0]["summary_text"]

    return {"original_text": "No content to summarize", "summary": ""}
