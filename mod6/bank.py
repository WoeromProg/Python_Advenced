import logging
import csv
from flask import Flask
from werkzeug.exceptions import InternalServerError
from typing import Optional

app = Flask("bank")


logger = logging.getLogger(__name__)


@app.route("/bank_api/<branch>/<int:person_id>")
def bank_api(branch: str, person_id: int):
    logger.debug(f"Request {person_id} from {branch}")

    branch_card_file_name = f"bank_data/{branch}.csv"

    with open(branch_card_file_name, "r") as fi:
        logger.debug(f"Successfully opened {branch} card")
        csv_reader = csv.DictReader(fi, delimiter=",")

        for record in csv_reader:
            if int(record['id']) == person_id:
                logger.debug(f"Successfully found card for {person_id}")
                return record["name"]
        else:
            logger.debug(f"Person with id={person_id} has not found in {branch}")
            return "Person not found", 400

@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    logger.error(f"Handled uncaught exception")
    original: Optional[Exception] = getattr(e, "original_exception", None)

    if isinstance(original, FileNotFoundError):
        logger.error(f"Tried to access {original.filename}. Exception info: {original.strerror}")

    elif isinstance(original, OSError):
        logger.error(f"Unable to access a card. Exception info: {original.strerror}")

    return "Internal server error", 500


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="banking.log", format='%(asctime)s - %(name)s - %(levelname)s - '
                                                                            '%(message)s')
    app.run()
