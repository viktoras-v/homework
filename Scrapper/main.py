import logging
from scraper import BookScraper
from database import BookDatabase

def main():
    logging.basicConfig(level=logging.INFO) # Severity level
    logger = logging.getLogger(__name__)    # Logeris vadinamas kaip modulis

    scraper = None                          # Inicializacija
    db = None                               # Inicializacija

    try:
        logger.info("Starting web scraper...")
        scraper = BookScraper()                     # Objekto sukurimas iš klasės
        books = scraper.scrape_books(num_pages=3)   # Metodo iškvietimas, t.y skraperio
        logger.info(f"Scraped {len(books)} books")  # Suskaičiojam "derlių"

        db = BookDatabase()                         # Objekto sukurimas iš klasės
        db.insert_books(books)                      # Metodo iškvietimas, patalpinimas knygų į DB
        logger.info("Data inserted into database")

        db.export_to_csv("books.csv")               # Metodo iškvietimas, patalpinimas knygų į CSV
        logger.info("Data exported to books.csv")

        stats = db.get_statistics()                 # Sukuriamas DICTIONARY su ataskaitą
        logger.info(f"Total books: {stats['total_books']}")
        logger.info(f"Average price: {stats['average_price']:.2f}")
        logger.info(f"Most common rating: {stats['most_common_rating']}")
        logger.info("Books per category:")
        for cat, count in stats["books_per_category"]: # Pretty print of array of tuples
            logger.info(f"  {cat}: {count}")

        logger.info("Scraping completed successfully!")

    except Exception as e:                          # Jeigu įvyks klaida - patalpinsim ją į "e"
        logger.error(f"Error occurred: {e}") 

    finally:
        if scraper:
            scraper.close()                         # Uždarom naršyklę, atlaisvinam visus resursus.
        if db:
            db.close()                              # Uždarom susijungimą su DB

if __name__ == "__main__":                          # Entry point. Programa paleidžiama ne kaip modulis
    main()
