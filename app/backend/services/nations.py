class JobCountry:
    def __init__(self):
        self.south_america = self.south_america_countries()
        self.central_america = self.central_america_countries()
        self.north_america = self.north_america_countries()
        self.latin_america = self.south_america + self.central_america
        self.all_americas = self.south_america + self.central_america + self.north_america
        self.europe = self.europe_countries()
        self.asia = self.asia_countries()

    def south_america_countries(self):
        return [
            "Argentina",
            "Bolivia",
            "Brazil",
            "Chile",
            "Colombia",
            "Ecuador",
            "Paraguay",
            "Peru",
            "Uruguay",
            "Venezuela"
        ]

    def central_america_countries(self):
        return [
            "Belize",
            "Costa Rica",
            "El Salvador",
            "Guatemala",
            "Honduras",
            "Nicaragua",
            "Panama"
        ]

    def north_america_countries(self):
        return [
            "Canada",
            "United States",
            "Mexico"
        ]

    def europe_countries(self):
        return [
            "Albania",
            "Andorra",
            "Armenia",
            "Austria",
            "Azerbaijan",
            "Belarus",
            "Belgium",
            "Bosnia and Herzegovina",
            "Bulgaria",
            "Croatia",
            "Cyprus",
            "Czech Republic",
            "Denmark",
            "Estonia",
            "Finland",
            "France",
            "Georgia",
            "Germany",
            "Greece",
            "Hungary",
            "Iceland",
            "Ireland",
            "Italy",
            "Kazakhstan",
            "Kosovo",
            "Latvia",
            "Liechtenstein",
            "Lithuania",
            "Luxembourg",
            "Malta",
            "Moldova",
            "Monaco",
            "Montenegro",
            "Netherlands",
            "North Macedonia",
            "Norway",
            "Poland",
            "Portugal",
            "Romania",
            "Russia",
            "San Marino",
            "Serbia",
            "Slovakia",
            "Slovenia",
            "Spain",
            "Sweden",
            "Switzerland",
            "Turkey",
            "Ukraine",
            "United Kingdom",
            "Vatican City"
        ]

    def asia_countries(self):
        return [
            "Afghanistan",
            "Armenia",
            "Azerbaijan",
            "Bahrain",
            "Bangladesh",
            "Bhutan",
            "Brunei",
            "Cambodia",
            "China",
            "Cyprus",
            "East Timor",
            "Georgia",
            "India",
            "Indonesia",
            "Iran",
            "Iraq",
            "Israel",
            "Japan",
            "Jordan",
            "Kazakhstan",
            "Kuwait",
            "Kyrgyzstan",
            "Laos",
            "Lebanon",
            "Malaysia",
            "Maldives",
            "Mongolia",
            "Myanmar",
            "Nepal",
            "North Korea",
            "Oman",
            "Pakistan",
            "Palestine",
            "Philippines",
            "Qatar",
            "Russia",
            "Saudi Arabia",
            "Singapore",
            "South Korea",
            "Sri Lanka",
            "Syria",
            "Taiwan",
            "Tajikistan",
            "Thailand",
            "Turkey",
            "Turkmenistan",
            "United Arab Emirates",
            "Uzbekistan",
            "Vietnam",
            "Yemen"
        ]

    def get_latin_america_countries(self):
        return self.latin_america

    def get_all_americas(self):
        return self.all_americas

    def get_europe_countries(self):
        return self.europe

    def get_asia_countries(self):
        return self.asia
