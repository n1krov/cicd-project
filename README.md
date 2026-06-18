![Arquitectura del Pipeline de IC/CD](https://github.com/n1krov/cicd-project/blob/feature/master/docs/img/imagen.png)

## Estructura de Calidad (Piramide de Pruebas)

El proyecto implementa dos niveles criticos de verificacion automatizada dentro de un contenedor Docker para asegurar la integridad de la aplicacion:

1. **Pruebas Unitarias (Pytest):** Valida de forma aislada la logica matematica y las restricciones de longitud de los modulos funcionales en memoria (Enfoque de Caja Blanca en `src/validador.py`).
2. **Pruebas de Aceptacion (Behave / Gherkin):** Valida la conformidad del artefacto final respecto a las especificaciones y criterios de aceptacion del negocio (Enfoque de Caja Negra sobre `src/index.html`).

---

## Guia de Uso y Ejecucion del Repositorio

### Requisitos Previos (Entorno Local)
* Sistema Operativo: GNU/Linux (Entorno de desarrollo validado en Arch Linux).
* Motor de Contenedores: Docker instalado y con el demonio activo (`systemctl status docker`).
* Herramientas de Construccion: GNU Make (`make`).
* Control de Versiones: Git.

### 1. Clonar el Repositorio e Inicializar Ramas
Para replicar el entorno de Gitflow utilizado en el desarrollo, ejecute:
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
git checkout -b dev
git checkout -b feature/hola-mundo

```

### 2. Ejecucion y Construccion en el Entorno Local (Build Local)

El proyecto cuenta con un `Makefile` que encapsula la complejidad de Docker. Para compilar la imagen local ejecutable y correr la suite unificada de pruebas de forma secuencial, ejecute:

```bash
make test
```

*Nota:* Este comando implementa el principio de **Fallo Rapido (Fail-Fast)**. Si las pruebas unitarias de `pytest` fallan, la ejecucion se aborta inmediatamente antes de invocar a `behave`, optimizando los tiempos de feedback del desarrollador.

### 3. Flujo de Integracion hacia la Nube

Una vez que la build local arroje un resultado exitoso (verde), los cambios deben ser promovidos siguiendo el flujo de trabajo establecido:

```bash
# Guardar cambios en la rama de caracteristica
git add .
git commit -m "feat: implementar suite unificada de pruebas"
git push origin feature/hola-mundo

# Integrar en la rama de desarrollo para activar el Servidor de IC
git checkout dev
git merge feature/hola-mundo
git push origin dev

```

---

## Datos Adicionales e Informacion de Control

### Variables de Entorno y Secretos Requeridos

Para que el pipeline de GitHub Actions se ejecute de manera exitosa en la nube, se deben cargar los siguientes secretos en la configuracion del repositorio (**Settings > Secrets and variables > Actions**):

* `TRELLO_API_KEY`: Clave de la API de desarrollo de Trello.
* `TRELLO_TOKEN`: Token de acceso de usuario para la API de Trello.
* `TRELLO_BOARD_ID`: Identificador unico del tablero de gestion.
* `TRELLO_DOING_LIST_ID`: ID de la columna de tareas en ejecucion (Doing).
* `TRELLO_DONE_LIST_ID`: ID de la columna de tareas finalizadas (Done).
* `MAIL_USERNAME`: Cuenta de correo electronico (Gmail) utilizada para la autenticacion SMTP de alertas.
* `MAIL_PASSWORD`: Contraseña de aplicacion de un solo uso generada en la cuenta de Google.

### Fuente Unica de Verdad (Single Source of Truth)

El ciclo de vida del software esta estrictamente gobernado por los documentos analiticos ubicados dentro del directorio `docs/`:

* `docs/requirements.md`: Especificacion de requerimientos y criterios de aceptacion.
* `docs/plan.md`: Definicion de la arquitectura tecnica y seleccion del stack.
* `docs/tasks.md`: Matriz de control y seguimiento de tareas de implementacion.
* `docs/STATUS.md`: Bitacora del estado actual del proyecto y proximos objetivos.
