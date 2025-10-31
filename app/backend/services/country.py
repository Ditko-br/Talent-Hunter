# ...existing code...
import requests
import difflib
import threading
import time

class JobCountry:
    """
    Serviço para países do mundo.
    - Prefere buscar dados na API https://restcountries.com
    - Mantém cache em memória e métodos para listagem, busca e autocomplete.
    """

    API_ALL = "https://restcountries.com/v3.1/all?fields=name,cca2,cca3,region,subregion,capital,population,area"
    _cache_lock = threading.RLock()

    def __init__(self, refresh_on_init: bool = True, cache_ttl: int = 24 * 3600):
        self._countries = []           # lista de dicts de países
        self._by_name = {}             # map name_lower -> country dict
        self._by_code = {}             # map cca2/cca3 -> country dict
        self._regions = {}             # map region -> [country dicts]
        self._subregions = {}          # map subregion -> [country dicts]
        self._updated_at = 0
        self.cache_ttl = cache_ttl
        if refresh_on_init:
            try:
                self.refresh_cache()
            except Exception:
                # não falhar na importação, cache ficará vazio e poderá ser preenchido depois
                pass

    # --- Cache / Fetch --------------------------------------------------------------------
    def refresh_cache(self, force: bool = False):
        """
        Recarrega dados da API se o cache expirou ou se force=True.
        """
        with self._cache_lock:
            now = time.time()
            if not force and (now - self._updated_at) < self.cache_ttl and self._countries:
                return
            resp = requests.get(self.API_ALL, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            self._build_indexes(data)
            self._updated_at = now

    def _build_indexes(self, raw_list):
        """
        Normaliza e indexa os lista de países retornada pela API.
        Cada country dict padronizado terá:
        {
          "name": "Brasil",
          "official": "República Federativa do Brasil",
          "cca2": "BR",
          "cca3": "BRA",
          "region": "Americas",
          "subregion": "South America",
          "capital": ["Brasília"],
          "population": 214000000,
          "area": 8515767.0
        }
        """
        countries = []
        by_name = {}
        by_code = {}
        regions = {}
        subregions = {}

        for item in raw_list:
            name_obj = item.get("name", {})
            common = name_obj.get("common") or ""
            official = name_obj.get("official") or ""
            cca2 = item.get("cca2", "") or ""
            cca3 = item.get("cca3", "") or ""
            region = item.get("region") or ""
            subregion = item.get("subregion") or ""
            capital = item.get("capital") or []
            population = item.get("population")
            area = item.get("area")

            country = {
                "name": common,
                "official": official,
                "cca2": cca2,
                "cca3": cca3,
                "region": region,
                "subregion": subregion,
                "capital": capital,
                "population": population,
                "area": area
            }

            countries.append(country)
            # keys for matching
            key = common.lower()
            by_name[key] = country
            if official:
                by_name[official.lower()] = country
            if cca2:
                by_code[cca2.upper()] = country
            if cca3:
                by_code[cca3.upper()] = country

            regions.setdefault(region or "Unknown", []).append(country)
            if subregion:
                subregions.setdefault(subregion, []).append(country)

        # sort lists by name
        countries.sort(key=lambda x: x["name"])
        for r in regions:
            regions[r].sort(key=lambda x: x["name"])
        for s in subregions:
            subregions[s].sort(key=lambda x: x["name"])

        self._countries = countries
        self._by_name = by_name
        self._by_code = by_code
        self._regions = regions
        self._subregions = subregions

    # --- Queries / Helpers ----------------------------------------------------------------
    def get_all_countries(self):
        """Retorna lista de nomes de todos os países."""
        if not self._countries:
            self.refresh_cache()
        return [c["name"] for c in self._countries]

    def get_country_details(self, name_or_code: str):
        """
        Retorna dicionário com detalhes do país.
        Aceita nome (case insensitive) ou código cca2/cca3.
        """
        if not name_or_code:
            return None
        key = name_or_code.strip()
        if not self._countries:
            self.refresh_cache()

        # try code lookup
        c = self._by_code.get(key.upper())
        if c:
            return c

        # try name exact
        c = self._by_name.get(key.lower())
        if c:
            return c

        # fuzzy match on names
        names = [c["name"] for c in self._countries]
        matches = difflib.get_close_matches(key, names, n=1, cutoff=0.7)
        if matches:
            return self._by_name.get(matches[0].lower())
        return None

    def get_regions(self):
        """Retorna lista de regiões conhecidas (ex: Africa, Americas, Asia, Europe, Oceania)."""
        if not self._regions:
            self.refresh_cache()
        return sorted([r for r in self._regions.keys() if r])

    def get_subregions(self):
        if not self._subregions:
            self.refresh_cache()
        return sorted([s for s in self._subregions.keys() if s])

    def get_countries_by_region(self, region: str):
        """Retorna lista de nomes para uma region (ex: 'Europe', 'Americas')."""
        if not self._regions:
            self.refresh_cache()
        return [c["name"] for c in self._regions.get(region, [])]

    def get_countries_by_subregion(self, subregion: str):
        """Ex: 'South America', 'Central America', 'Northern America'"""
        if not self._subregions:
            self.refresh_cache()
        return [c["name"] for c in self._subregions.get(subregion, [])]

    def search_countries(self, query: str, limit: int = 20):
        """
        Busca por nome (case-insensitive) usando substring e fuzzy fallback.
        Retorna lista de dicionários com nome e region.
        """
        if not query:
            return []
        q = query.strip().lower()
        if not self._countries:
            self.refresh_cache()

        results = []
        # substring match (nome, oficial, capital)
        for c in self._countries:
            if q in c["name"].lower() or q in (c["official"] or "").lower():
                results.append(c)
                if len(results) >= limit:
                    break
            else:
                # capital match
                capitals = " ".join(c.get("capital") or [])
                if q in capitals.lower():
                    results.append(c)
                    if len(results) >= limit:
                        break

        # fuzzy fallback
        if not results:
            names = [c["name"] for c in self._countries]
            close = difflib.get_close_matches(query, names, n=limit, cutoff=0.6)
            for nm in close:
                results.append(self._by_name.get(nm.lower()))
        return [{"name": r["name"], "region": r["region"], "subregion": r.get("subregion")} for r in results]

    def autocomplete(self, prefix: str, limit: int = 10):
        """Retorna sugestões que começam com o prefix (case-insensitive)."""
        if not prefix:
            return []
        p = prefix.strip().lower()
        if not self._countries:
            self.refresh_cache()

        starts = [c["name"] for c in self._countries if c["name"].lower().startswith(p)]
        if len(starts) >= limit:
            return starts[:limit]
        # complementar com substring matches
        subs = [c["name"] for c in self._countries if p in c["name"].lower() and not c["name"].lower().startswith(p)]
        combined = starts + subs
        return combined[:limit]

    def get_continent_for_country(self, country_name: str):
        """
        Retorna a região (continent) para o país informado.
        Exemplo: 'Brazil' -> 'Americas'
        """
        c = self.get_country_details(country_name)
        if not c:
            return None
        return c.get("region") or c.get("subregion")

    # --- Utility ----------------------------------------------------------------------------
    def refresh_if_stale(self):
        """Chama refresh automático se cache expirou."""
        if (time.time() - self._updated_at) > self.cache_ttl:
            try:
                self.refresh_cache()
            except Exception:
                pass