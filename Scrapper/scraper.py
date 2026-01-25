import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class BookScraper:
    def __init__(self):
        logging.info("Initializing WebDriver...")
        options = Options()                             # Objektas opcijų saugojimui
        options.add_argument("--headless")              # įjungiam opciją
        self.driver = webdriver.Chrome(options=options) # Draiverio sukurimas
        self.wait = WebDriverWait(self.driver, 10)      # Maksimalus laukimo laikas, kol atsiiras elementas
        self.base_url = "https://books.toscrape.com/"

    def scrape_books(self, num_pages=3):
        books = []                                      # Tuščio konteinerio inicializacija
        self.driver.get(self.base_url)                  # Metodas GET užkrauna URL

        for page in range(num_pages):                   # Iteracija puslapių
            logging.info(f"Scraping page {page + 1}")   # Kadangi skaičiuoja nuo 0 tai +1
            self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod"))) # Laukia kol atsitas elementai product_pod (knygos langelis)
            book_elements = self.driver.find_elements(By.CLASS_NAME, "product_pod")              # Suranda visus elementus product_pod 

            for book in book_elements:                          # Iteracija visų knygų viename puslapyje
                try:
                    data = self.scrape_book_details(book)       # Kviečiamas metodas kuris "parse" knygos detales ir išsaugoja į DICTIONARY 
                    books.append(data)                          # Papildome sąrašą books
                except Exception as e:                          # Klaidos atveju išsaugos ją į "e"
                    logging.error(f"Error scraping book: {e}")

            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, "li.next a") # Surandam "next" ir pereinam prie kito puslapio
                next_button.click()
            except:
                break

        return books

    def scrape_book_details(self, book_element):                                                                  # Parsing knygos
        title = book_element.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price_text = book_element.find_element(By.CLASS_NAME, "price_color").text                                 # Kaina kaip tekstas
        price = float(price_text.replace("£", ""))                                                                # Kaina kaip skaičius be ženkliuko 
        rating_text = book_element.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").split()[-1]  # Paimam paskutinę reitingo žvaigždutė kaip tekstą.
        rating = self.convert_rating(rating_text)                                                                 # Paverčiam žvaigdutės tekstą į skaičių
        availability = book_element.find_element(By.CLASS_NAME, "availability").text.strip()                      # Paimam "availability" tekstą ir pašainam nereikalingus tarpus

        book_element.find_element(By.CSS_SELECTOR, "h3 a").click()                                                # Tam kad surasti žanrą reikia paklikinti knygą
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "breadcrumb")))                            # Luktelsim kol užsikraus
        category = self.driver.find_element(By.CSS_SELECTOR, "ul.breadcrumb li:nth-child(3) a").text              # Pasiimam trečia žodį iš "breadcrumb"
        self.driver.back()

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "category": category
        }

    def convert_rating(self, rating_text):              # Konvertacija reitingo žodiš -> skaičius
        ratings = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        return ratings.get(rating_text, None)

    def close(self):                                    # Uždarom naršyklę
        logging.info("Closing browser...")
        self.driver.quit()
