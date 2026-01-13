import os
from dotenv import load_dotenv

load_dotenv()

class AlmaConfig:
    """Configuración principal de Alma Labs"""
    
    # GitHub
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    
    # Supabase
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
    # Qdrant
    QDRANT_URL = os.getenv('QDRANT_URL', 'http://localhost:6333')
    QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
    
    # OpenAI
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Estructura de memoria
    MEMORY_COMMON_COLLECTION = "alma_common_memory"
    MEMORY_PRIVATE_PREFIX = "alma_agent_"
    
    # Roles con acceso de escritura
    WRITE_ACCESS_ROLES = ['ceo', 'cto', 'supervisor', 'portero']