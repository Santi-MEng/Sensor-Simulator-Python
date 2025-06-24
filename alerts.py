import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename='alerts.log', #where to save
    level=logging.WARNING,  #what to save
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def alert(message):
    """Logs a warning message."""
    print("⚠️  ALERT:", message)
    logging.warning(message)

def info(message):
    """Optional: logs a regular info message."""
    print("ℹ️  INFO:", message)
    logging.info(message)

# Optional: test alert manually
if __name__ == "__main__":
    alert("Test alert: temperature too high")
    info("Test info: system running normally")