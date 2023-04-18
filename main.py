from MyLogger import MyLogger

# Global attributes?
global_mode = "DEV"  # DEV ou PROD


# TODO : créer un fichier de config avec tous les param de l'application
if __name__ == "__main__":

    # Étape 1 - Setup file logger
    log_name = "myLog.log"
    logger = MyLogger(filename=log_name)

    logger.info("")
    logger.info("Démarrage de l'application")
    logger.info(f"Fichier log : {log_name}")
    logger.info(f'main.global_mode : {global_mode}')