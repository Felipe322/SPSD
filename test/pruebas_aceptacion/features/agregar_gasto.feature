Característica: Agregar un gasto
    Como administrador de la secretaría de prevención del delito
    requiero registrar un gasto nuevo
    para poder llevar el control de los egresos.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema como administrador
        Y entro a la sección de Agregar Gasto
        Y capturo los datos: Descripcion "Se compraron muchos lápices", Proveedor "La comer S.A C.V", Precio Unitario "2.50", Cantidad "300", Fecha "12/12/2020", Actividad "5 2 4"
        Cuando presiono el botón Agregar del gasto
        Entonces puedo ver el gasto "Se compraron muchos lápices" agregado en la lista de gastos.

