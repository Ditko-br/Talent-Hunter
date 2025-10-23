from models import db
from sqlalchemy import Column, Integer, String

class Jobs:
    # initial areas
    def __init__(self):
        self.areas = {
            # tech
            "technology": [
                "software engineering",
                "backend development",
                "frontend development",
                "fullstack development",
                "data science",
                "machine learning",
                "artificial intelligence",
                "cloud computing",
                "cybersecurity",
                "data engineering",
                "devops",
                "qa / testing",
                "mobile development",
                "it support",
                "network engineering"
            ],
            # design
            "design": [
                "graphic design",
                "ux design",
                "ui design",
                "product design",
                "motion design",
                "web design",
                "visual design",
                "interaction design",
                "illustration",
                "branding",
                "3d design"
            ],

            # sales
            "sales": [
                "b2b sales",
                "b2c sales",
                "inside sales",
                "sales operations",
                "sales representative",
                "account executive",
                "account manager",
                "business development",
                "customer success",
                "sales enablement",
                "lead generation"
            ],

            # marketing
            "marketing": [
                "digital marketing",
                "seo / sem",
                "content marketing",
                "social media",
                "email marketing",
                "branding",
                "paid ads",
                "influencer marketing",
                "growth marketing",
                "marketing analytics"
            ],

            # finance
            "finance": [
                "financial planning",
                "accounting",
                "audit",
                "tax management",
                "treasury",
                "investment analysis",
                "financial reporting",
                "controllership"
            ],

            # RH
            "human_resources": [
                "recruitment",
                "training and development",
                "people analytics",
                "organizational development",
                "benefits and compensation",
                "labor relations",
                "performance management"
            ],

            # operations / suppy chain
            "operations": [
                "logistics",
                "supply management",
                "inventory control",
                "distribution",
                "transportation",
                "warehouse management",
                "process optimization"
            ],

            # customers
            "customer_support": [
                "customer service",
                "technical support",
                "help desk",
                "customer success",
                "call center",
                "client relations"
            ],

            # product
            "product_management": [
                "product owner",
                "product manager",
                "agile methodologies",
                "roadmap planning",
                "market research",
                "feature prioritization"
            ],

            # databricks / business intelligence 
            "data_analytics": [
                "data analysis",
                "business intelligence",
                "data visualization",
                "data engineering",
                "statistics",
                "predictive modeling"
            ],

            # enginnering
            "engineering": [
                "civil engineering",
                "mechanical engineering",
                "electrical engineering",
                "production engineering",
                "chemical engineering",
                "industrial engineering",
                "maintenance engineering"
            ],

            # health
            "healthcare": [
                "nursing",
                "medicine",
                "biomedicine",
                "pharmacy",
                "physiotherapy",
                "nutrition",
                "psychology",
                "medical laboratory"
            ],

            # education
            "education": [
                "teaching",
                "pedagogy",
                "distance learning",
                "educational technology",
                "academic coordination",
                "research"
            ],

            #  legal 
            "legal": [
                "lawyer",
                "legal assistant",
                "compliance",
                "contracts",
                "corporate law",
                "labor law",
                "tax law"
            ],

            # administration
            "administration": [
                "office management",
                "executive assistance",
                "administrative support",
                "facility management",
                "secretary",
                "document control"
            ],

            # projects manager
            "project_management": [
                "project manager",
                "pmo",
                "scrum master",
                "agile coach",
                "kanban",
                "risk management",
                "project planning"
            ],

            # supply chain 
            "supply_chain": [
                "procurement",
                "purchasing",
                "supplier management",
                "demand planning",
                "inventory",
                "logistics",
                "import/export"
            ],

            # estate valuation
            "real_estate": [
                "real estate sales",
                "property management",
                "valuation",
                "brokerage",
                "leasing",
                "construction management"
            ],

            # manufacturing
            "manufacturing": [
                "production line",
                "industrial automation",
                "quality control",
                "maintenance",
                "safety engineering",
                "lean manufacturing"
            ],

            # comunication 
            "communications": [
                "public relations",
                "journalism",
                "content creation",
                "corporate communication",
                "press office",
                "copywriting",
                "storytelling"
            ]
        }

        # Aliases 
        self.aliases = {
            "tecnologia": "technology",
            "ti": "technology",
            "it": "technology",
            "vendas": "sales",
            "comercial": "sales",
            "recursos humanos": "human_resources",
            "rh": "human_resources",
            "finanças": "finance",
            "jurídico": "legal",
            "educação": "education",
            "administração": "administration",
            "projetos": "project_management"
        }


    # return all the areas
    def get_areas(self):
        return self.areas

