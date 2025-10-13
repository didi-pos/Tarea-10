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
      Este caso es similar a la primera simulación, ya que asi se hace la dockerización la diferencia es cuantos aechivos uno agregue dependiendo cuantos sean necesarios y se configuraria en Dockerfile.
      Lo diferente aqui es que se requiere un archivo ademas del de la simulación que se quiere dockerizar, ya que para que funcione correctamente la simulacion se necesita de este otro archivo que mismo se menciona en el codigo de la simulación, pero se menciona en una carpeta, asi que se necesita mover la carpeta con el archivo (.urdf) a la carpeta que se quiere dockerizar la simulación.
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/b6c677d7-5ba9-42a3-8609-6f9647ed6e3d"/></p>
    </div>
    <p>
      Aqui se muestra el archivo de la simulación (.py), donde tiene puesto el <code>physicsClient = p.connect(p.DIRECT)</code> y también se evidencia como se menciona el archivo (.urdf) que complementa este archivo de simulación.
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/45fda3e4-d34d-412b-bbba-27d316dc6a8b"/></p>
    </div>
    <p>
      Y aqui se muestra el Dockerfile de esta imagen de simulación donde se muestra que se requirio otro "COPY" para poder agregar 
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
      
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/17a24418-4422-4dfe-8ca3-bcaa7cb54c40"/></p>
    </div>
    <p>
      
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/0803efff-35fd-448e-a157-a52b679da09b"/></p>
    </div>
    <p>
      
    </p>
  </li>
</ol>

<h2>Corriendo Simulaciones</h2>
<div align="center">
  <p><img width=850 src="https://github.com/user-attachments/assets/311b5286-44c1-44d9-9985-ed2f206ad4f0"/></p>
</div>
<p>
      
</p>

<hr>

<div align="center">
  <p><em>Segundo Punto</em></p>
</div>

<hr>

<div align="center">
  <h2>Dockerizar las Simulaciones con Graficos</h2>
</div>

<ol>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/8e6e8c3e-21ca-4d67-acd1-e9eb3f220dd7"/></p>
    </div>
    <p>
      
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/cd4e5d83-cf1c-4a61-affc-b0438741dbdf"/></p>
    </div>
    <p>
      
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/73254ccb-048b-4238-8d10-37d87b02a81e"/></p>
    </div>
    <p>
      
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/4f9884c7-7911-409e-8131-01a3f207b977"/></p>
    </div>
    <p>
      
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/4f9884c7-7911-409e-8131-01a3f207b977"/></p>
    </div>
    <p>
      
    </p>
  </li>
</ol>
