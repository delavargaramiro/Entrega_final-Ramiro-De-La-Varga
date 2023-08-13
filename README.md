# Entrega_final-Ramiro-De-La-Varga

Bienvenido a la Aplicación de Gestión de Clientes y Pedidos
Nuestra aplicación web está diseñada para facilitar la gestión de clientes, productos y pedidos de una manera eficiente y organizada. Con esta herramienta, podrás tener un control total sobre tus operaciones comerciales y administrativas. A continuación, te explicamos algunas de las funciones más importantes de nuestra aplicación:

Configuración del entorno:

Tener Python instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python (https://www.python.org/downloads/). Instala Django en tu entorno virtual. Puedes hacerlo mediante el comando pip install django. Descarga y prepara el proyecto:

Descarga los archivos del proyecto a tu máquina local y descomprímelos si es necesario. Abre una terminal o línea de comandos y navega al directorio raíz del proyecto. Configura la base de datos:

Abre el archivo settings.py dentro del directorio app. Asegúrate de configurar la base de datos según tus preferencias (por defecto, está configurado para utilizar SQLite, que es una base de datos ligera incluida con Django). Aplica las migraciones:

En la terminal, ejecuta el siguiente comando para aplicar las migraciones y crear las tablas necesarias en la base de datos: python manage.py migrate. Crea un superusuario (opcional):

Si deseas acceder al panel de administración de Django, puedes crear un superusuario utilizando el siguiente comando: python manage.py createsuperuser. Sigue las instrucciones para ingresar un nombre de usuario, dirección de correo electrónico y contraseña. Ejecuta el servidor de desarrollo:

Inicia el servidor de desarrollo de Django con el siguiente comando: python manage.py runserver. El servidor estará disponible en http://localhost:8000/. Accede a la aplicación:

Abre tu navegador web y navega a http://localhost:8000/. Verás la página de inicio de la aplicación, con enlaces para registrar clientes, productos, realizar pedidos y buscar.

Página de Inicio
Al acceder a la aplicación, serás recibido por una página de inicio intuitiva que te brindará una visión general de las diferentes áreas de tu negocio. Desde aquí, podrás acceder rápidamente a las funciones clave, como la gestión de clientes, productos, pedidos y la búsqueda de información relevante.

Gestión de Clientes
Nuestra aplicación te permite mantener un registro detallado de tus clientes. Puedes agregar nuevos clientes, incluyendo su nombre, edad, dirección, correo electrónico, tarjeta de crédito y saldo. Además, puedes editar la información de los clientes existentes o eliminar registros si es necesario. Esto te ayudará a mantener un historial completo de tus relaciones con los clientes.

Gestión de Productos
Administra tus productos de manera eficiente utilizando nuestra aplicación. Puedes agregar productos con su nombre, precio, cantidad y descripción. Esto te permitirá tener un inventario actualizado y realizar un seguimiento de la disponibilidad de tus productos. También puedes editar y eliminar productos según sea necesario.

Gestión de Pedidos
Realiza y gestiona pedidos de forma sencilla. Al crear un nuevo pedido, podrás seleccionar el cliente, el producto y la cantidad deseada. El sistema calculará automáticamente el valor total del pedido y la fecha en que se realizó. Esto te ayudará a rastrear tus ventas y controlar los pedidos pendientes.

Búsqueda Avanzada
Nuestra función de búsqueda te permite encontrar rápidamente la información que necesitas. Puedes buscar clientes, productos o pedidos por nombre, correo electrónico, descripción y más. Los resultados de búsqueda te mostrarán una lista de coincidencias que podrás revisar en detalle.

Autenticación de Usuarios
La seguridad es fundamental, por lo que hemos implementado un sistema de autenticación de usuarios. Los usuarios pueden registrarse en la plataforma utilizando un formulario simple. Una vez registrados, podrán iniciar sesión con sus credenciales. Además, los usuarios tienen la opción de cerrar sesión cuando lo deseen.
