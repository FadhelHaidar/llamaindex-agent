from llama_index.core import Settings as LlamaIndexSettings
from llama_index.llms.groq import Groq
from src.settings import settings

# ---- Setup Groq LLM ----
def init_llm():
    """
    Initialize Groq LLM and set it as the global LLM in LlamaIndex.
    """
    LlamaIndexSettings.llm = Groq(
        model=settings.groq_model, 
        api_key=settings.groq_api_key,
        is_chat_model=True
    )
    
    return LlamaIndexSettings.llm

# ---- Tiny city database ----
GAZETTEER = {
    "jakarta":  {"lat": -6.2088, "lon": 106.8456, "country": "Indonesia"},
    "bandung":  {"lat": -6.9175, "lon": 107.6191, "country": "Indonesia"},
    "yogyakarta":{"lat": -7.7956, "lon": 110.3695, "country": "Indonesia"},
    "singapore":{"lat":  1.3521, "lon": 103.8198, "country": "Singapore"},
    "tokyo":    {"lat": 35.6762, "lon": 139.6503, "country": "Japan"},
    "paris":    {"lat": 48.8566, "lon":   2.3522, "country": "France"},
    "new york": {"lat": 40.7128, "lon": -74.0060, "country": "USA"},
}
