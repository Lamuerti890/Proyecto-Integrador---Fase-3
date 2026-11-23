# Proyecto-Integrador---Fase-3
# Juego de Memoria

## Descripción
El programa permite jugar a encontrar parejas de cartas en un tablero de 4 x 4. Incluye dos modalidades:

- Modo local: dos jugadores utilizan el mismo equipo.
- Modo multijugador LAN: dos equipos se comunican mediante TCP. El equipo servidor representa al Jugador 1 y el equipo cliente representa al Jugador 2.

## Tecnologías
- Python 3
- Sockets TCP
- JSON para el intercambio de mensajes
- Bibliotecas estándar de Python (`random`, `time`, `socket`, `json`; no requiere paquetes externos)

## Estructura del repositorio
- juego-memoria/
- game_logic.py
- juego.py
- server.py
- client.py
- README.md
- LICENSE
- BITACORA_CONFLICTOS.md

## Requisitos
- Python 3.9 o superior.
- Para el modo LAN, ambos equipos deben estar conectados a la misma red y la red debe permitir la comunicación por el puerto TCP 5000.
- Permitir el puerto 5000 en el firewall del equipo servidor, si el sistema lo bloquea.

## Ejecución

### Modo local
En la terminal, dentro de la carpeta del proyecto:
```bash
python juego.py
```

### Modo multijugador

**1. En el equipo que será el servidor (Jugador 1):**

```bash
python server.py
```

**2. En el equipo que será el cliente (Jugador 2):**

```bash
python client.py
```

Cuando el cliente lo solicite, debe escribir la dirección IP local del equipo servidor. Ambos equipos deben estar en la misma LAN.

## Comunicación cliente-servidor
- El servidor crea el tablero y mantiene el estado oficial de la partida.
- El servidor valida las jugadas y actualiza las puntuaciones.
- El cliente envía sus dos posiciones seleccionadas al servidor.
- Los mensajes se transmiten mediante TCP y están codificados en JSON.
- Si el cliente se desconecta, el servidor informa la interrupción en la terminal.

## Protocolo de comunicación

Cada mensaje se envía como un objeto JSON terminado en salto de línea.

Ejemplo de jugada del cliente:

```json
{"type": "play", "cards": [0, 5]}
```

Ejemplo de actualización del servidor:

```json
{"type": "state", "state": {"current_player": 2, "game_over": false}}
```

## Decisiones del proyecto
- Dimensión del tablero: 4 x 4.
- Protocolo de transporte: TCP.
- Puerto de comunicación: 5000.
- Formato de mensajes: JSON.
- La lógica del juego (`game_logic.py`) está separada del modo local (`juego.py`) y de la comunicación de red (`server.py` y `client.py`).

## Autoría
- Integrantes: Anthony Puga, Tobias Castillo, Gianni Bedon
- Asignatura: Lógica de Programación / Proyecto Integrador
- Institución: UIDE
- Docente: Paulina, Marcela, Gustavo, Philip, Juan

## Licencia y atribución

Este proyecto se distribuye bajo la licencia MIT. Consultar el archivo `LICENSE`.

### Créditos, referencias y apoyo de IA
- Código y librerías: Desarrollado en Python utilizando únicamente bibliotecas de la librería estándar (`random`, `time`, `socket`, `json`). No se incorporaron paquetes externos ni fragmentos de código de terceros con licencias adicionales.
- Recursos visuales: La interfaz es de consola/terminal basada en texto y caracteres ASCII/simples (como `##` para cartas ocultas y separadores textuales); no se emplearon imágenes, íconos ni recursos multimedia externos.
- Apoyo de Inteligencia Artificial: Se utilizó asistencia de IA como apoyo académico para revisar la modularización entre `game_logic.py`, `juego.py` y `server.py`, verificar la consistencia del protocolo JSON/TCP, redactar borradores de documentación y estructurar entradas de la bitácora bajo la Fórmula Asertiva. Todo el código y contenido final fue revisado, probado y validado por los integrantes del equipo.
