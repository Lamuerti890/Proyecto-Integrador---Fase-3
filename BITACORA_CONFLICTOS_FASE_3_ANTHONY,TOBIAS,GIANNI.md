# Bitácora de gestión de conflictos

## Registro 1

- Fecha: 2026-11-12
- Integrantes involucrados: Anthony Puga, Tobias Castillo, Gianni Bedon
- Tema del proyecto: Separación de módulos (`game_logic.py`, `juego.py`, `server.py`) y sincronización de turnos/estado en red LAN

### 1. Hechos
- Durante la carga de los diagramas de la fase anterior a código en Python, se trabajó inicialmente con la clase `MemoryGame` dentro de `juego.py` mientras `game_logic.py` quedó con métodos pendientes y `server.py` importaba desde `juego`. Además, al probar el intercambio de mensajes JSON entre servidor y cliente, hubo confusión sobre qué archivo debía centralizar la validación de jugadas y el formato de las claves del estado (`scores` y posiciones indexadas desde `0` frente a la numeración mostrada desde `1` en consola).

- Al realizar pruebas de conexión cliente-servidor entre equipos en red local, se presentaron intentos fallidos de conexión cuando el servidor no estaba escuchando aún en puertos diferentes o cuando el cliente ingresaba datos no numéricos o posiciones fuera de rango, además de quedar pendientes el llenado de la bitácora, los datos de autoría y la revisión final de los entregables antes de grabar el video explicativo.

### 2. Sentimientos
- Al ser nuestro primer semestre en la U, la falta de experiencia previa integrando sockets TCP con lógica de juego generó incertidumbre, retrasos puntuales y algo de tensión al ver que los cambios de un integrante afectaban las pruebas de los demás.

- Sentimos presión por la cercanía de la entrega de la fase y algo de frustración cuando una prueba de red no conectaba a la primera, aunque también motivación por ver funcionando el juego multijugador.

### 3. Necesidades
- Necesitamos mayor claridad en la responsabilidad de cada archivo, un criterio común antes de modificar funciones compartidas y pruebas conjuntas en red local para avanzar con orden sin pisar el trabajo de nadie.

-Necesitamos una lista de verificación clara de los requisitos de la rúbrica, validar casos de error (entradas inválidas, desconexión del cliente y conexión LAN) y repartir de forma explícita la documentación y la grabación del video.

### 4. Petición
- Proponemos la definición de `game_logic.py` como única fuente de la clase `MemoryGame`, que `juego.py` y `server.py` importen desde allí para luego reaizar una prueba conjunta de 20 minutos en LAN antes de cerrar cambios, quedando como responsable de la unificación de importaciones y pruebas el equipo completo el 2026-11-15.

-Proponemos revisar juntos la rúbrica antes de grabar, donde probemos los casos de error en `server.py` y `client.py`, completemos `README.md`, `LICENSE` y `BITACORA_CONFLICTOS.md`, y acordemos un guion breve para el video explicativo, con revisión final el 2026-11-21.

### Acuerdo y seguimiento
- **Acuerdo:** Centralizar `MemoryGame` en `game_logic.py`, actualizar las importaciones en `juego.py` y `server.py`, y validar el flujo completo de turnos en modo local y LAN. Tambien verificar manejo de errores en consola y sockets, completar documentación y autoría en el repositorio, y ensayar la demostración para el video explicativo.

- Responsable(s): Anthony Puga, Tobias Castillo y Gianni Bedon
- Fecha de revisión: 2026-11-15
- Resultado: Resuelto; los módulos quedaron separados y probados con intercambio de mensajes JSON y en cierre; documentación y código listos para la verificación final y grabación del video..
