class Keywords:
    def __init__(self):
        self.keywords_list = self.load_keywords()

    def define_keywords(self):
        self.keywords = {
            "technology": [
                "software", "dev", "programming", "cloud", "AI", "machine learning", "data", "cybersecurity", "backend", "frontend", "fullstack", "mobile", "network", "it", "support", "devops", "qa", "testing"
            ],
            "design": [
                "designer", "graphic", "ux", "ui", "visual", "product", "motion", "web", "interaction", "illustration", "branding", "3d"
            ],
            "sales": [
                "vendas", "comercial", "b2b", "b2c", "inside", "account", "business development", "lead", "customer", "representative", "executive", "manager"
            ],
            "marketing": [
                "marketing", "digital", "seo", "sem", "content", "social media", "email", "branding", "ads", "influencer", "growth", "analytics"
            ],
            "finance": [
                "finance", "financial", "accounting", "audit", "tax", "treasury", "investment", "reporting", "controllership"
            ],
            "human_resources": [
                "rh", "recursos humanos", "recruitment", "training", "people analytics", "organizational", "benefits", "compensation", "labor", "performance"
            ],
            "operations": [
                "operations", "logistics", "supply", "inventory", "distribution", "transportation", "warehouse", "process"
            ],
            "customer_support": [
                "customer", "support", "service", "technical", "help desk", "call center", "client"
            ],
            "product_management": [
                "product", "owner", "manager", "agile", "roadmap", "market research", "feature"
            ],
            "data_analytics": [
                "data", "analytics", "business intelligence", "visualization", "statistics", "predictive"
            ],
            "engineering": [
                "engineering", "civil", "mechanical", "electrical", "production", "chemical", "industrial", "maintenance"
            ],
            "healthcare": [
                "health", "nursing", "medicine", "biomedicine", "pharmacy", "physiotherapy", "nutrition", "psychology", "laboratory"
            ],
            "education": [
                "education", "teaching", "pedagogy", "distance learning", "technology", "coordination", "research"
            ],
            "legal": [
                "legal", "lawyer", "assistant", "compliance", "contracts", "corporate", "labor", "tax"
            ],
            "administration": [
                "administration", "office", "executive", "support", "facility", "secretary", "document"
            ],
            "project_management": [
                "project", "manager", "pmo", "scrum", "agile", "kanban", "risk", "planning"
            ],
            "supply_chain": [
                "supply", "procurement", "purchasing", "supplier", "demand", "inventory", "logistics", "import", "export"
            ],
            "real_estate": [
                "real estate", "sales", "property", "management", "valuation", "brokerage", "leasing", "construction"
            ],
            "manufacturing": [
                "manufacturing", "production", "automation", "quality", "maintenance", "safety", "lean"
            ],
            "communications": [
                "communications", "public relations", "journalism", "content", "corporate", "press", "copywriting", "storytelling"
            ]
        }

    def load_keywords(self):
        return self.define_keywords()