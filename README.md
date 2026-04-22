# Sistema_de_tienda-POO_Paradigmas
## **Descripción del proyecto**

**Objetivo:** Diseñar e implementar una aplicación de web que gestione las ventas diarias de una tienda de abarrotes, aplicando rigurosamente los principios de Programación Orientada a Objetos e implementando Patrones de Diseño bajo la arquitectura Modelo-Vista-Controlador (MVC) .
---

### 1. Requerimientos Funcionales del Sistema

El sistema debe permitir:

1.  **Gestión de Productos:**
    - Registrar productos: Código de barras, nombre, categoría (Abarrotes, Lácteos, Bebidas, Limpieza), precio de compra, precio de venta, stock actual.
    - Listar productos con filtro por categoría o nombre.
    - Actualizar stock (recibir mercancía).

2.  **Proceso de Venta (Punto de Venta):**
    - Iniciar una nueva venta.
    - Agregar productos al carrito usando el código de barras.
    - Aplicar descuentos (Ver sección de Patrones).
    - Calcular subtotal, IVA (16%) y total.
    - Finalizar venta (descontar stock automáticamente).
    - Generar ticket de compra en texto plano.

3.  **Gestión de Clientes:**
    - Registrar clientes frecuentes (Nombre, Teléfono, Puntos acumulados).
    - Asignar cliente a la venta.

---
## Tecnologias usadas

```md
- Python
- Flask
- HTML / CSS / Js
- Git y Github
```

---
##Estructura del proyecto
```md
com.tienda.abarrotes
|
|-app.py
|
|-model
|  |
|  |-cliente.py
|  |-inventario.py
|  |-producto.py
|  |-venta.py
|  |-producto_granel.py
|  |-producto_unitario.py
|  |-detalles_venta.py
|
|-view
|  |
|  |-static
|  |  |
|  |  |-css
|  |  |
|  |  |-js
|  |
|  |-templates
|    |
|    |-index.html
|    |-inventario.html
|    |-ventas.html
|
|-controller
|  |
|  |-inventario_controller.py
|  |-ventas_controller.py
|
|-patterns
|  |
|  |-factory
|  |  |
|  |  |-producto_factory.py
|  |
|  |-observer
|  |  |
|  |  |-alerta_bajo_stock.py
|  |  |-istock_observer.py
|  |
|  |-strategy
|    |
|    |-descuento_fijo.py
|    |-descuento_porcentaje.py
|    |-iestrategia_descuento.py
|
|-utils
  |-sin_stock_exeption.py

```
---
##Como ejecutar

para ejecutar el proyect, se ejectuar el archivo "app.py"

---
##Acceso

Abrir en el navegador:
htt://127.0.0.1:5000
---
#Alumnos:
Garcia Reyes Gamaliel
Montes Olivares Sergio Alonso
