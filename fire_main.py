from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from time import sleep
import random
from selenium.webdriver.support.ui import Select


# Gerar um número inteiro aleatório entre 5 e 20 (inclusive) com passo de 2
random_int_with_step = random.randrange(5, 21, 2)
print("Número inteiro aleatório com passo:", random_int_with_step)

# Definir o novo user-agent que você deseja utilizar
new_user_agent = "Mozilla/5.0 (Windows NT 11.0; Win34; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/80.0.3987.87 Safari/537.36"
# new_user_agent = ""

# Definir as opções do navegador Firefox com o user-agent personalizado
options = Options()
options.set_preference("general.useragent.override", new_user_agent)

# Inicializar o serviço do driver do Firefox
driver_service = FirefoxService(executable_path=GeckoDriverManager().install())

# Inicializar o navegador Firefox com as opções configuradas
driver = webdriver.Firefox(service=driver_service, options=options)


def create_new_user():

    # Acessando página, para criar um novo usuário
    driver.get("about:profiles")

    try:

        button_criandoNovo_Perfil = driver.find_element(By.CSS_SELECTOR, "#create-button")
        button_criandoNovo_Perfil.click()
        print("Realizou o click no btn Criar novo Perfil")

        # Aguardar a nova janela abrir (pode ser necessário ajustar o tempo)
        sleep(5)
        
        # Mudar o foco para a nova janela
        driver.switch_to.window(driver.window_handles[-1])
        
        # Agora você está na nova janela e pode interagir com seus elementos

        # Exemplo: interagir com um elemento na nova janela
        new_window_element = driver.find_element(By.ID, "element_id_in_new_window")
        new_window_element.click()
        
        # Após a interação, você pode retornar ao foco da janela original se necessário
        # driver.switch_to.window(driver.window_handles[0])
    
    except:

        print("Não encontrou o btn de Criar um novo Usuário")

def open_config():
        
    driver.get("about:config")

    try:
 
        # Verificação do Botao de Aceitar Risco do FireFox
        btn_AceitarRisco = driver.find_element(By.CSS_SELECTOR, "#warningButton")
        print("Botão de confirmação de risco, encontrado.")
        btn_AceitarRisco.click()
        sleep(2)

        btn_MostrarTudo = driver.find_element(By.CSS_SELECTOR, "#show-all")

        btn_MostrarTudo.click()

        sleep(5)

        # Necessário analisar todos as configuração para entender oque cada um faz.
        # E configurar somente as partes necessárias

    except:
        
        pass


# Iniciando Função de ajuste da pagina config
open_config()


# Encerrar o navegador
driver.quit()
