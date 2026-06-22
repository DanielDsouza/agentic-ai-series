# 02 — Building a RAG Application

**Make Your AI Answer Questions About YOUR Data**

📖 [Read the full article on Substack](#)

## What You'll Learn

- Why LLMs hallucinate on data they weren't trained on — and how RAG fixes it
- The 4 steps of any RAG pipeline: Chunk, Embed, Retrieve, Generate
- How vector embeddings turn text into searchable numbers
- How cosine similarity finds the most relevant documents for a query
- How to build a RAG application from scratch using Python and Google Gemini (no frameworks)

## How to Run

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey)

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Add your API key in `rag_app.py` (replace the placeholder)

4. Run it:
```bash
   python rag_app.py
```

## What the Code Does

This is a bare-bones RAG pipeline that:
- Holds a small knowledge base of company policy documents (the data)
- Converts each document into a **vector embedding** using Google Gemini 
- Takes your question, converts it to an embedding, and finds the closest matching documents using **cosine similarity** (retrieval)
- Passes the retrieved documents + your question to the LLM, which generates a grounded answer (generation)
- Refuses to answer when the knowledge base doesn't contain relevant information — instead of making something up

That retrieve-before-you-generate pattern is the foundation of every RAG system.

## Try It Out

```bash
# Question answered from the knowledge base
python rag_app.py
# Change the last line to: rag_app("How many days of annual leave do employees get?")

# Question with no relevant data — agent says it doesn't know
python rag_app.py
# Change to: rag_app("What's the company's policy on bringing pets to the office?")
```

## Requirements

- Python 3.10+
- `google-genai` — for embeddings and answer generation
- `numpy` — for cosine similarity calculations