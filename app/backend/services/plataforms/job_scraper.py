import time
import random
import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional
import requests
from bs4 import BeautifulSoup
from flask import current_app

@dataclass
class JobItem:
    title: str
    company: str
    url: str
    location: Optional[str] = None
    country: Optional[str] = None
    area: Optional[str] = None
    description: Optional[str] = None

class BaseScraper:
    headers: Dict[str, str]

    def __init__(self):
        ua = current_app.config.get("SCRAPER_USER_AGENT", "TalentHunterBot/1.0")
        self.headers = {"User-Agent": ua}
        self.timeout = int(current_app.config.get("SCRAPER_TIMEOUT", 15))

    def _get(self, url: str, params: Optional[dict] = None) -> requests.Response:
        resp = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
        resp.raise_for_status()
        # respeitar o site
        time.sleep(random.uniform(0.5, 1.2))
        return resp

    def normalize(self, item: JobItem) -> JobItem:
        # padronizações simples
        item.title = item.title.strip()
        item.company = item.company.strip()
        return item

class GupyScraper(BaseScraper):
    BASE = "https://portal.gupy.io"

    def search(self, q: str = "", limit: int = 50) -> List[JobItem]:
        # A página da Gupy é dinâmica; aqui usamos resultados públicos de listagem
        url = f"{self.BASE}/job-search"
        resp = self._get(url, params={"q": q} if q else None)
        soup = BeautifulSoup(resp.text, "lxml")
        jobs: List[JobItem] = []
        for a in soup.select("a[href*='/job/']"):
            href = a.get("href", "")
            title = a.get_text(strip=True)
            if not title or not href:
                continue
            if href.startswith("/"):
                href = f"{self.BASE}{href}"
            # heurística para extrair companhia/local se presente em elementos próximos
            parent = a.find_parent("div")
            company = ""
            location = None
            if parent:
                comp = parent.find(string=re.compile(r"(?i)empresa|company|companhia"))
                if comp:
                    company = comp.strip()
                loc_el = parent.find(string=re.compile(r"(?i)remoto|remote|\w+ - [A-Z]{2}"))
                if loc_el:
                    location = loc_el.strip()
            jobs.append(self.normalize(JobItem(title=title, company=company or "Gupy", url=href, location=location)))
            if len(jobs) >= limit:
                break
        return jobs

class GenericScraper(BaseScraper):
    def search(self, base_url: str, item_selector: str, title_selector: str, link_selector: str,
               company_selector: Optional[str] = None, limit: int = 50) -> List[JobItem]:
        resp = self._get(base_url)
        soup = BeautifulSoup(resp.text, "lxml")
        jobs: List[JobItem] = []
        for el in soup.select(item_selector):
            title_el = el.select_one(title_selector)
            link_el = el.select_one(link_selector)
            if not title_el or not link_el:
                continue
            title = title_el.get_text(strip=True)
            href = link_el.get("href", "")
            if href and href.startswith("/"):
                # tenta resolver relativo com base_url
                from urllib.parse import urljoin
                href = urljoin(base_url, href)
            company = ""
            if company_selector:
                comp_el = el.select_one(company_selector)
                if comp_el:
                    company = comp_el.get_text(strip=True)
            jobs.append(self.normalize(JobItem(title=title, company=company or "Company", url=href)))
            if len(jobs) >= limit:
                break
        return jobs

class JobScraperService:
    def __init__(self):
        self.gupy = GupyScraper()
        self.generic = GenericScraper()

    def search_all(self, query: str = "", limit_per_source: int = 30) -> List[dict]:
        results: List[JobItem] = []
        try:
            results.extend(self.gupy.search(q=query, limit=limit_per_source))
        except Exception:
            pass
        # Adicione aqui outras fontes (LinkedIn requer automação com Selenium/API)
        # results.extend(...)

        # dedup por url
        seen = set()
        unique: List[dict] = []
        for j in results:
            if j.url in seen:
                continue
            seen.add(j.url)
            unique.append({
                "title": j.title,
                "company": j.company,
                "url": j.url,
                "location": j.location,
                "country": j.country,
                "area": j.area,
                "description": j.description,
            })
        return unique

# Instância pronta
job_scraper_service = JobScraperService()

