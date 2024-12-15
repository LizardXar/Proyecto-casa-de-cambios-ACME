import pytest
from Modelo.monedas_DAO import Monedas_DAO
from Modelo.conectorBD import ConectorBD

@pytest.fixture
def conectorBD():
    # Configuramos el conector con los parámetros de la base de datos
    return ConectorBD(hostdb="localhost", userdb="root", passwordb="", basedatosdb="casa_ACME")

@pytest.fixture
def monedas_dao(conectorBD):
    # Creamos una instancia de Monedas_DAO con el conectorBD
    return Monedas_DAO(conectorBD)

def test_recuperar_listaMonedas(monedas_dao):
    # Ejecutamos el método que interactúa con la base de datos
    estado, lista_monedas = monedas_dao.recuperar_listaMonedas()

    assert estado == 0  # Verificamos que la base de datos haya devuelto un estado de éxito (0)
    assert len(lista_monedas) > 0  # Verificamos que la lista de monedas no esté vacía
    assert lista_monedas[0]['codigo'] == 1  # Verificamos que la moneda primera fila devuelve el codigo '1'
    assert lista_monedas[0]['nombre'] == 'USD'  # Verificamos que la moneda primera fila sea 'USD'

def test_recuperar_listaMonedas_activas(monedas_dao):
    # Ejecutamos el método que interactúa con la base de datos
    estado, lista_monedas_activas = monedas_dao.recuperar_listaMonedas_activas()

    assert estado == 0 # Verificamos que la base de datos haya devuelto un estado de éxito (0)
    assert len(lista_monedas_activas) > 0 # Verificamos que la lista de monedas activas no esté vacía
    assert lista_monedas_activas[0]['estado'] == '1'  # Verificamos que la moneda 1 esté activa
    assert lista_monedas_activas[1]['estado'] != '2'  # Verificamos que la moneda 2 no este inactiva
