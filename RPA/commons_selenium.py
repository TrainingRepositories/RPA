import subprocess 
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def init_driver(download_dir:str|None = None):
    chrome_options = webdriver.ChromeOptions()
    # Set printer options
    # chrome_options.add_argument("--kiosk-printing")
    # chrome_options.add_argument("--disable-print-preview")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')



    # Set preferences for the printer
    # prefs = {
    #     "printing.print_preview_sticky_settings.appState": json.dumps(
    #         {
    #             "recentDestinations": [
    #                 {
    #                     "id": "Save as PDF",
    #                     "origin": "local",
    #                     "account": "",
    #                 }
    #             ],
    #             "version": 2,
    #         }
    #     ),
    #     "savefile.default_directory": download_dir,  # Set the directory where PDFs will be saved
    #     "printing.default_destination_selection_rules": [
    #         {
    #             "kind": "local",
    #             "namePattern": "Save as PDF",
    #         }
    #     ],
    #     "printing.allowed_destinations": [
    #         {
    #             "id": "Save as PDF",
    #             "origin": "local",
    #             "account": "",
    #         }
    #     ],
    #     "savefile.saveAsType": "pdf",
    #     "browser.helperApps.alwaysAsk.force": False,
    #     "browser.helperApps.neverAsk.saveToDisk": "application/pdf",
    #     "printing.papersize": {
    #         "height_microns": 431800,
    #         "name": "Tabloid",
    #         "width_microns": 279400,
    #     },
    #     "printing.scaling": "custom",
    #     "printing.custom_scaling": 100,
    #     "print_preview": "always",
    #     "is_chrome_for_print": True,
    #     "printing.orientation": "landscape",
    # }

    # chrome_options.add_argument("--force-renderer-accessibility")
    
    prefs =  {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": False  # Set to False to open PDFs in Chrome
    } 
    chrome_options.add_experimental_option("prefs", prefs)

    
    driver = webdriver.Chrome(options=chrome_options) 

    return driver
 
def EC_presence_of_element(driver,logger,CSS_SELECTOR:str,ELEMENT_NAME:str,FirstOneOnly=True):
    try:
        temp =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))) if FirstOneOnly else  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR)))
        logger.info(f'{ELEMENT_NAME} Found ')  
        return temp
    except Exception as ex: 
        logger.error(f'{ELEMENT_NAME} Exception ') 
        logger.error(f'An error occurred: {traceback.format_exc()}')

def ELEMENT_CLICK(driver,logger,ELEMENT , ELEMENT_NAME:str):
    try: 
        ELEMENT = WebDriverWait(driver, 10).until( EC.element_to_be_clickable(ELEMENT) )
        ELEMENT.click()
        logger.info(f'{ELEMENT_NAME} CLICKED ')   
    except Exception as ex:  (logger.error(f'{ELEMENT_NAME} CLICKED Exception ') ,logger.error(f'An error occurred: {traceback.format_exc()}'))

def SEND_KEYS(logger,ELEMENT , ELEMENT_NAME:str,KEYS,CLEAR_BEFORE_TYPE=True):
    try:
        # clear elmnt 
        ELEMENT.clear() if CLEAR_BEFORE_TYPE else False
        # send keys
        ELEMENT.send_keys(KEYS) ;logger.info(f'{ELEMENT_NAME} send_keys pass : {str(KEYS)}')   
    except Exception as ex:  (logger.error(f'{ELEMENT_NAME} send_keys Exception ') ,logger.error(f'An error occurred: {traceback.format_exc()}'))

def Filter_Elmnt_By_TEXT(logger,ELEMENT , ELEMENT_NAME:str,TEXT_TO_FILTER,return_only_one=True):
    try:
        FILTERED_ELMNTS = [ x for x in ELEMENT if x.text == TEXT_TO_FILTER ]
        if return_only_one:
            if len(FILTERED_ELMNTS) == 1:
                logger.info(f'{ELEMENT_NAME}  filtered')
                return FILTERED_ELMNTS[0]
            else:
                logger.error(f'{ELEMENT_NAME} not filtered by using  {TEXT_TO_FILTER} len found {len(FILTERED_ELMNTS)} ')  
        else:
            if len(FILTERED_ELMNTS) >= 1:
                logger.info(f'{ELEMENT_NAME}  filtered by using  {TEXT_TO_FILTER}')
                return FILTERED_ELMNTS
            else:
                logger.error(f'{ELEMENT_NAME} not filtered by using  {TEXT_TO_FILTER} len found {len(FILTERED_ELMNTS)} ')  
    except Exception as ex:  (logger.error(f'{ELEMENT_NAME} filtered Exception ') ,logger.error(f'An error occurred: {traceback.format_exc()}'))

def is_TEXT_match(logger,ELEMENT , ELEMENT_NAME:str,TEXT_TO_match):
    try: 
        ELEMENT_text = ELEMENT.text
        
        try:
            ELEMENT_text =  str(ELEMENT_text.strip())
        except:  (logger.error(f'{ELEMENT_NAME} is_TEXT_match text Exception ') ,logger.error(f'An error occurred: {traceback.format_exc()}'))
              
        
        if ELEMENT_text == TEXT_TO_match.strip():
            logger.info(f'{ELEMENT_NAME}  match text ')
            return ELEMENT
        else:
            logger.info(f'{ELEMENT_NAME} not match text ')  
    except Exception as ex:  (logger.error(f'{ELEMENT_NAME} match text Exception ') ,logger.error(f'An error occurred: {traceback.format_exc()}'))






















