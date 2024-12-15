#test_gestor_monedas.py Prueba unitaria
import pytest
from unittest.mock import MagicMock
from Modelo.gestor_monedas import Gestor_Monedas

@pytest.fixture
def gestor_monedas():
    # Creamos una instancia de Gestor_Monedas
    gestor = Gestor_Monedas()

    # Mockeamos el DAO para evitar llamadas reales a la base de datos
    gestor.monedas_DAO = MagicMock()
    
    return gestor

def test_recuperar_monedas(gestor_monedas):
    # Verificar que el evento "lista_monedas" se dispara correctamente
    gestor_monedas.trigger_event = MagicMock()
    gestor_monedas.recuperar_monedas()
    gestor_monedas.trigger_event.assert_called_once_with("lista_monedas")

def test_recuperar_monedas_activas(gestor_monedas):
    # Verificar que el evento "lista_monedas_activas" se dispara correctamente
    gestor_monedas.trigger_event = MagicMock()
    gestor_monedas.recuperar_monedas_activas()
    gestor_monedas.trigger_event.assert_called_once_with("lista_monedas_activas")

def test_desplegar_monedas(gestor_monedas):
    # Configuramos el mock para devolver un valor específico.
    lista_monedas_mock = [
        {"codigo": 1, "nombre": "USD", "tipo": 960.00},
        {"codigo": 2, "nombre": "EUR", "tipo": 1040.00}
    ]
    gestor_monedas.monedas_DAO.recuperar_listaMonedas.return_value = lista_monedas_mock

    # Verificamos que `desplegar_monedas` devuelve el valor esperado.
    resultado = gestor_monedas.desplegar_monedas()
    assert resultado == lista_monedas_mock
    gestor_monedas.monedas_DAO.recuperar_listaMonedas.assert_called_once()

def test_desplegar_monedas_activas(gestor_monedas):
    # Configuramos el mock para devolver un valor específico.
    lista_monedas_activas_mock = [
        {"codigo": "1", "nombre": "USD", "tipo": 960.00, "estado" : "1"},
        {"codigo": "2", "nombre": "EUR", "tipo": 1040.00, "estado" : "1"}
    ]
    gestor_monedas.monedas_DAO.recuperar_listaMonedas_activas.return_value = lista_monedas_activas_mock

    # Verificamos que `desplegar_monedas_activas` devuelve el valor esperado.
    resultado = gestor_monedas.desplegar_monedas_activas()
    assert resultado == lista_monedas_activas_mock
    gestor_monedas.monedas_DAO.recuperar_listaMonedas_activas.assert_called_once()
