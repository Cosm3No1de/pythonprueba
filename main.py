import logging
import request

#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(treadName)s - %(processName)s - %(levelname)s - %(message)s",
                    filename="CosmeProyect.log",
                    filemode="a")


def get_current_price(id):
    logging.debug("Entramos a la funcion get_current_price.")


    response = request.get(f"http://coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd")

    if response.status_code ==200:
        logging.info("La respuesta fue exitosa.")

        return response.json()
    
    else:
        logging.warning("No fue posible obtener una respuesta.")

        return None
