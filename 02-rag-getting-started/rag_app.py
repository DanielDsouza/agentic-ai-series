from google import genai
import numpy as np


#Entire your API key from Google AI Studio here
client = genai.Client(api_key="YOUR_API_KEY_HERE")

# Sample knowledge base
documents = [
    "Our company offers 24 days of paid annual leave per year. "
    "New employees are eligible for leave after completing their 90-day probation period.",
    
    "The refund policy allows customers to request a full refund within 30 days of purchase. "
    "After 30 days, only store credit is offered. Digital products are non-refundable.",
    
    "Employee work hours are from 9 AM to 6 PM, Monday through Friday. "
    "Flexible working arrangements can be requested through the HR portal after 6 months.",
    
    "The company provides health insurance coverage for all full-time employees. "
    "Coverage includes medical, dental, and vision. Family plans are available at a subsidized rate.",
    
    "Performance reviews are conducted twice a year, in June and December. "
    "Ratings are based on goal completion, peer feedback, and manager assessment.",
    
    "Remote work is allowed up to 3 days per week. Employees must be in-office on Tuesdays and Thursdays. "
    "Remote work from outside the country requires prior approval from HR and Legal."
]



# Convert the Above Knowledge Base Documents to Embeddings
def get_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )
    return response.embeddings[0].values

doc_embeddings = []
for doc in documents:
    embedding = get_embedding(doc)
    doc_embeddings.append(embedding)
    
print(f"Created {len(doc_embeddings)} embeddings")
print(f"Each embedding has {len(doc_embeddings[0])} dimensions")


#Build in the retrieval logic
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def retrieve(query, top_k=2):
    query_embedding = get_embedding(query)
    
    similarities = []
    for i, doc_emb in enumerate(doc_embeddings):
        score = cosine_similarity(query_embedding, doc_emb)
        similarities.append((score, i))
    
    similarities.sort(reverse=True)
    
    results = []
    for score, idx in similarities[:top_k]:
        results.append({
            "document": documents[idx],
            "score": round(score, 4)
        })
    
    return results


#Build the RAG Function & Try it Out
def rag(question):
    print(f"\n{'='*60}")
    print(f"Question: {question}")
    print(f"{'='*60}")
    
    retrieved = retrieve(question, top_k=2)
    
    print(f"\nRetrieved {len(retrieved)} relevant chunks:")
    for i, r in enumerate(retrieved):
        print(f"  [{i+1}] (score: {r['score']}) {r['document'][:80]}...")
    
    context = "\n\n".join([r["document"] for r in retrieved])
    
    prompt = f"""You are a helpful assistant. Answer the question based ONLY on the context provided below.
If the context doesn't contain enough information to answer, say "I don't have enough information to answer that."

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    print(f"\nAnswer: {response.text}")
    return response.text


# Test it
rag("How many days of annual leave do employees get?")
rag("Can I work from home on Wednesdays?")
rag("What's the refund policy for digital products?")
rag("What's the company's policy on bringing pets to office?")