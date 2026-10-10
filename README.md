# TerraLoop POC 01

## Human in the Loop para observación local

TerraLoop POC 01 es una prueba de concepto desarrollada con micro:bit y MakeCode Python.

La idea central es explorar un sistema simple donde una lectura automática de sensor pueda combinarse con una observación humana local.

No busca predecir terremotos ni reemplazar sistemas científicos de monitoreo.

Busca representar, de manera educativa y experimental, una arquitectura híbrida basada en:

- sensores
- observación humana
- persistencia temporal
- interpretación conjunta

---

## Idea

Un sensor puede medir movimiento.

Pero un sensor no conoce por sí solo el contexto del territorio.

Una persona local puede observar algo que el sensor no registra directamente, por ejemplo:

- cambios en el terreno
- modificaciones en estructuras
- cambios en cursos de agua
- sonidos inusuales
- otras observaciones relevantes del entorno

TerraLoop incorpora esa observación humana dentro del sistema.

---

## Human in the Loop

El micro:bit utiliza dos entradas humanas.

### Botón A

Indica:

`Sin observación local relevante`

El sistema muestra:

`OK`

### Botón B

Indica:

`Existe una observación local relevante`

El sistema muestra inicialmente:

`H`

La observación queda activa durante una ventana temporal determinada.

---

## Estados visuales

El micro:bit representa distintos estados:

- Diamante pequeño: estado normal
- Diamante grande: movimiento detectado por el sensor
- Cuadrado vacío: observación humana activa
- Tilde: coincidencia entre movimiento detectado y observación humana

---

## Persistencia temporal

La observación humana no desaparece inmediatamente.

Cuando una persona presiona el botón B, la observación queda activa durante un tiempo definido.

En el POC se utiliza un tiempo corto para realizar pruebas.

En una implementación futura podría utilizarse una ventana temporal mayor.

Esto permite representar que una observación humana puede seguir siendo relevante incluso después del momento exacto en que fue registrada.

---

## Arquitectura conceptual

Sensor automático

+

Observación humana local

+

Tiempo

=

Interpretación conjunta

---

## Hardware

- BBC micro:bit
- Computadora
- Cable USB

No requiere sensores externos para esta primera prueba de concepto.

---

## Software

- Microsoft MakeCode
- Python para MakeCode

---

## Objetivo del POC

Demostrar que un sistema de observación puede combinar:

1. una señal automática
2. una entrada humana
3. una ventana temporal
4. un estado interpretado

El objetivo no es sustituir sistemas profesionales de monitoreo.

El objetivo es explorar cómo incorporar conocimiento humano local dentro de sistemas tecnológicos de bajo costo.

---

## Posibles próximas versiones

Futuras iteraciones podrían incorporar:

- tipos de observación local
- categorías como terreno, agua o estructuras
- registro histórico
- transmisión entre nodos
- sensores externos
- visualización en Python
- series temporales
- mapas
- participación comunitaria
- validación científica

---

## Concepto

TerraLoop parte de una idea simple:

> Los sensores miden.  
> Las personas interpretan.  
> El contexto aparece cuando ambos se conectan.

---

## Autoría

Concepto e implementación:

Sonia Alejandra Toledo, 2026.(Alias Adabyte)

---

## License

This project is licensed under the MIT License.

---

## Estado

Proof of Concept 01

En desarrollo experimental.

