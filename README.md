<div align="center">
<h1>Tarea 10</h1>
  <p>
    Ingeniería Electrónica · Universidad Santo Tomás
    <br>
    <b>Didier Posse</b>
    <br>
    <em>Primer punto</em>
  </p>
</div>

<hr>

<div align="center">
  <h2>Dockerizar las Simulaciones sin Gráficos</h2>
</div>

<h2>Primera Simulación</h2>
<ol>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/8e6e8c3e-21ca-4d67-acd1-e9eb3f220dd7"/></p>
    </div>
    <p>
      Lo primero para <b>dockerizar</b> es crear una <b>carpeta o directorio</b> donde estarán todos los archivos necesarios para este proceso y que después se pueda ejecutar correctamente el archivo a dockerizar.
      <br><br>
      Luego de crear el directorio, se ingresa a él y se crea un <b>archivo de texto (.txt)</b> en el cual se colocan los nombres de las librerías que se van a usar y que deben descargarse, como por ejemplo <code>pybullet</code>.
      Las librerías se escriben con el formato: <code>&lt;nombre_librería&gt;==&lt;versión_librería&gt;</code>. Esto permite que, durante el proceso de construcción, se descarguen automáticamente las dependencias indicadas.
      <br><br>
      Después, se mueve el archivo de la simulación <b>(.py)</b> a la carpeta que se creó.
      <br>
      Ahora se configura todo para crear la imagen de Docker en un archivo sin extensión llamado <b>Dockerfile</b>. El código que se escriba dentro de este archivo representa los pasos del proceso de construcción.
      <br><br>
      Finalmente, se utiliza el comando <code>docker build -t &lt;nombre_imagen&gt; .</code>, y si todo está bien configurado, debería construirse correctamente la imagen.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/cd4e5d83-cf1c-4a61-affc-b0438741dbdf"/></p>
    </div>
    <p>
      Aquí se muestra el <b>código del archivo de la simulación (.py)</b>. 
      Es importante agregar la línea <code>physicsClient = p.connect(p.DIRECT)</code> para que la simulación pueda ejecutarse correctamente al estar dockerizada, ya que esta configuración permite que se procese sin entorno gráfico.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/73254ccb-048b-4238-8d10-37d87b02a81e"/></p>
    </div>
    <p>
      Este es el archivo <b>Dockerfile</b>, y su funcionamiento se puede explicar de la siguiente manera:
      <ul>
        <li><code>FROM python:3.11-slim</code> → Define la <b>imagen base</b> de Python (ligera y optimizada).</li>
        <li><code>LABEL maintainer:"..."</code> → Agrega una etiqueta con la información del creador del contenedor.</li>
        <li><code>RUN apt-get update ...</code> → Instala las <b>dependencias necesarias</b> para soportar PyBullet y la salida gráfica (OpenGL y librerías del sistema). Al final limpia la caché para reducir el tamaño de la imagen.</li>
        <li><code>WORKDIR /carrito</code> → Define la <b>carpeta de trabajo</b> dentro del contenedor donde se colocarán los archivos.</li>
        <li><code>COPY requirements.txt .</code> → Copia el archivo con las dependencias de Python dentro del contenedor.</li>
        <li><code>RUN pip install --no-cache-dir -r requirements.txt</code> → Instala las librerías Python sin guardar la caché de pip.</li>
        <li><code>COPY carrito.py .</code> → Copia el script principal de la simulación al contenedor.</li>
        <li><code>CMD ["python", "carrito.py"]</code> → Comando por defecto que ejecuta la simulación cuando se inicia el contenedor.</li>
      </ul>
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/4f9884c7-7911-409e-8131-01a3f207b977"/></p>
    </div>
    <p>
      Aquí se muestra cómo debe aparecer el proceso de <b>construcción de la imagen</b>. 
      Debe mostrarse una línea indicando <i>"building ...s (../..) Finished"</i>, lo que confirma que la construcción fue exitosa.
      <br><br>
      En la primera prueba no se pudo iniciar correctamente porque faltaba instalar los compiladores <code>gcc</code> y <code>g++</code>, los cuales son necesarios para compilar algunas librerías, como <code>pybullet</code>. 
      Una vez agregados, la imagen se construyó sin errores.
    </p>
  </li>
</ol>


<h2>Segunda Simulación</h2>
<ol>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/a571e02d-2570-431b-8f76-7994e4638d23"/></p>
    </div>
    <p>
      Este caso es <b>similar a la primera simulación</b>, ya que el proceso de dockerización se realiza prácticamente igual. 
      La diferencia está en la cantidad de <b>archivos que se deben incluir</b> dependiendo de lo que la simulación necesite, y esto se configura dentro del archivo <b>Dockerfile</b>.
      <br><br>
      En este caso, además del archivo principal de la simulación (<b>.py</b>), se requiere otro archivo adicional para que el programa funcione correctamente. 
      Este archivo adicional (<b>.urdf</b>) es mencionado dentro del código de la simulación y se encuentra en una carpeta específica. 
      Por eso, es necesario mover esa carpeta con su contenido hacia el mismo directorio donde se va a dockerizar la simulación.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/b6c677d7-5ba9-42a3-8609-6f9647ed6e3d"/></p>
    </div>
    <p>
      Aquí se muestra el <b>archivo de la simulación (.py)</b>, donde se utiliza la línea 
      <code>physicsClient = p.connect(p.DIRECT)</code> para permitir que la simulación se ejecute correctamente dentro del contenedor Docker. 
      <br><br>
      También se puede ver cómo dentro del código se hace referencia al archivo <b>(.urdf)</b>, que complementa la simulación y contiene la información del modelo que se carga en PyBullet.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/45fda3e4-d34d-412b-bbba-27d316dc6a8b"/></p>
    </div>
    <p>
      Finalmente, aquí se muestra el <b>Dockerfile</b> correspondiente a esta segunda simulación. 
      En él se puede observar que se agregó una línea adicional con <code>COPY</code> para incluir la <b>carpeta que contiene el archivo (.urdf)</b> dentro de la imagen de Docker.
      <br><br>
      Con esto, la configuración del Dockerfile queda completa y lista para construir la imagen sin errores, asegurando que tanto el archivo principal como los recursos adicionales estén disponibles dentro del contenedor.
    </p>
  </li>
</ol>

<h2>Tercera Simulación</h2>
<ol>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/1ef9ff6f-9b47-4c99-b770-a3b042665d88"/></p>
    </div>
    <p>
      En esta tercera simulación se realiza el <b>mismo proceso que en la primera</b>, ya que no se requieren archivos adicionales para que el script funcione correctamente. 
      <br><br>
      Al construir la imagen se puede observar el mensaje <i>"building ...s (../..) Finished"</i>, lo que indica que la <b>compilación se realizó exitosamente</b> y la imagen fue generada sin errores.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/17a24418-4422-4dfe-8ca3-bcaa7cb54c40"/></p>
    </div>
    <p>
      Este es el <b>archivo de la simulación del brazo robótico</b>, en el cual se utiliza la instrucción 
      <code>physicsClient = p.connect(p.DIRECT)</code> para garantizar que la simulación se ejecute correctamente dentro del contenedor Docker, sin necesidad de interfaz gráfica.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/0803efff-35fd-448e-a157-a52b679da09b"/></p>
    </div>
    <p>
      Finalmente, se muestra el <b>Dockerfile</b> utilizado para esta simulación, el cual mantiene la <b>misma estructura que el de la primera</b>. 
      <br><br>
      Una vez se comprende cómo funcionan los comandos principales, resulta sencillo entender su aplicación en la configuración de esta imagen, que sigue el mismo flujo de construcción.
    </p>
  </li>
</ol>

<h2>Corriendo Simulaciones</h2>
<div align="center">
  <p><img width=850 src="https://github.com/user-attachments/assets/311b5286-44c1-44d9-9985-ed2f206ad4f0"/></p>
</div>
<p>
  Después de haber construido todas las imágenes, el siguiente paso es <b>ejecutarlas para comprobar su funcionamiento</b> y verificar que la dockerización de las simulaciones en Python (<b>.py</b>) fue exitosa. 
  <br><br>
  Para correr una imagen se utiliza el comando <code>docker run &lt;nombre_imagen&gt;</code>, con el cual se inicia el contenedor y comienza el proceso de ejecución de la simulación.
</p>

<hr>

<div align="center">
  <p><em>Segundo Punto</em></p>
</div>

<hr>

<div align="center">
  <h2>Dockerizar las Simulaciones con Gráficos</h2>
</div>

<ol>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/5c6fc341-3c76-4cc1-b2ea-ab0530f9edbe"/></p>
    </div>
    <p>
      Para ejecutar las <b>imágenes de las simulaciones con entorno gráfico</b> —que es la forma más interesante y visual de observar los resultados— se deben hacer algunos ajustes previos. 
      <br><br>
      Primero, se modifica el archivo principal de la simulación (<b>.py</b>), realizando algunos cambios necesarios para habilitar la parte visual. 
      Luego, se ejecuta el comando <code>xhost +local:docker</code>, el cual <b>permite las conexiones X11</b> indispensables para mostrar el entorno gráfico del contenedor. 
      <br><br>
      Finalmente, se construye la imagen con <code>docker build -t &lt;nombre_de_la_imagen&gt; .</code>, dejándola lista para ejecutarse en cualquier entorno compatible.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/0db9c9fd-009d-455d-84a6-f5eb4710a730"/></p>
    </div>
    <p>
      En el código del archivo de simulación se reemplaza la línea 
      <code>physicsClient = p.connect(p.DIRECT)</code> por 
      <code>physicsClient = p.connect(p.GUI)</code>. 
      <br><br>
      Este cambio es clave, ya que permite <b>activar la interfaz gráfica</b> para visualizar la simulación, en lugar de que se ejecute directamente en modo de consola.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/59a729c7-127d-4350-b7c5-8ac07dff9dea"/></p>
    </div>
    <p>
      En el <b>Dockerfile</b>, se agrega una línea antes del comando que ejecuta la simulación: 
      <code>ENV DISPLAY=:0</code>. 
      <br><br>
      Esta instrucción <b>habilita la variable de entorno</b> que permite abrir la ventana donde se mostrará el entorno gráfico de la simulación, conectándose al servidor X del sistema anfitrión.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/0b1c0ecc-afce-4819-94a2-c9251e44c947"/></p>
    </div>
    <p>
      Para ejecutar correctamente el contenedor con entorno gráfico, además de haber configurado el script y el Dockerfile, se utiliza el siguiente comando:
      <br><br>
      <code>docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix &lt;nombre_imagen&gt;</code>.
      <br><br>
      Con este comando se establece la <b>conexión X11</b> con el servidor gráfico del sistema, permitiendo que la simulación se muestre en una ventana visual.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/4c3313a6-0378-4ccd-823d-631886e29924"/></p>
    </div>
    <p>
      Finalmente, se observa la <b>simulación corriendo de forma gráfica</b>, donde ya se puede interactuar con ella directamente. 
      <br><br>
      Es importante recordar que este procedimiento se aplica a cualquier simulación que se desee ejecutar con entorno gráfico, ya que no depende de otros factores externos. 
      Además, vale la pena tener en cuenta que el <b>modo gráfico</b> es ideal para simulaciones, juegos o aplicaciones visuales, mientras que existen otros contenedores que se ejecutan únicamente en la terminal mostrando solo datos en texto.
    </p>
  </li>
</ol>
