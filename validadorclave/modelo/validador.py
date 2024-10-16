from abc import ABC, abstractmethod


class MayusculaInvalidaError(Exception):
    pass


class MinusculaInvalidaError(Exception):
    pass


class NumeroInvalidoError(Exception):
    pass


class CaracterEspecialInvalidoError(Exception):
    pass


class CalistoInvalidoError(Exception):
    pass


# Clase abstracta ReglaValidacion
class ReglaValidacion(ABC):
    def _init_(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) <= self._longitud_esperada:
            raise LongitudInvalidaError(f"La clave debe tener más de {self._longitud_esperada} caracteres.")
        return True

    def _contiene_mayuscula(self, clave: str) -> bool:
        if not any(c.isupper() for c in clave):
            raise MayusculaInvalidaError("La clave debe contener al menos una letra mayúscula.")
        return True

    def _contiene_minuscula(self, clave: str) -> bool:
        if not any(c.islower() for c in clave):
            raise MinusculaInvalidaError("La clave debe contener al menos una letra minúscula.")
        return True

    def _contiene_numero(self, clave: str) -> bool:
        if not any(c.isdigit() for c in clave):
            raise NumeroInvalidoError("La clave debe contener al menos un número.")
        return True

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


# ReglaValidacionGanimedes
class ReglaValidacionGanimedes(ReglaValidacion):
    def _init_(self):
        super()._init_(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        if not any(c in "@_#$%" for c in clave):
            raise CaracterEspecialInvalidoError(
                "La clave debe contener al menos uno de los caracteres especiales @, _, #, $, %.")
        return True

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True


# ReglaValidacionCalisto
class ReglaValidacionCalisto(ReglaValidacion):
    def _init_(self):
        super()._init_(6)

    def contiene_calisto(self, clave: str) -> bool:
        if 'calisto' not in clave.lower():
            raise CalistoInvalidoError("La clave debe contener la palabra 'calisto'.")

        mayusculas = sum(1 for c in clave if c.isupper())
        if mayusculas < 2 or mayusculas == len(clave):
            raise CalistoInvalidoError("La palabra calisto debe tener al menos dos letras en mayúscula, pero no todas.")

        return True

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True


# Clase Validador
class Validador:
    def _init_(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)