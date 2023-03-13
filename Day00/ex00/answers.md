EX00: CHEATSHEET CONDA

1. Mostrar una lista de los paquetes instalados y sus versiones:
~~~~
    conda list
~~~~
2. Mostrar los metadatos del paquete numpy
~~~~
    conda search numpy
~~~~
3. Eliminar el paquete numpy
~~~~
    conda remove numpy
~~~~
4. (Re)instala el paquete numpy
~~~~
    conda install numpy
~~~~
5. Congela tus paquetes python y sus versiones en un archivo requeriments.txt que tienes que entregar:
~~~~
    conda list --export > requeriments.txt
    # This file may be used to create an environment using:
    # $ conda create --name <env> --file <this file>
~~~~
