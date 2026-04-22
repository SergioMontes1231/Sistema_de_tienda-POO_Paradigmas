# 🛒 Sistema de Tienda (POO + Flask)

## 📌 Descripción del proyecto

Aplicación web para la gestión de ventas de una tienda de abarrotes, desarrollada bajo principios de **Programación Orientada a Objetos (POO)**, utilizando **Flask** y aplicando **Patrones de Diseño** dentro de una arquitectura **Modelo-Vista-Controlador (MVC)**.

---

## ⚙️ Requerimientos Funcionales

### 🧾 1. Gestión de Productos

* Registro de productos:

  * Código de barras
  * Nombre
  * Categoría (Abarrotes, Lácteos, Bebidas, Limpieza)
  * Precio de compra
  * Precio de venta
  * Stock actual
* Listado con filtros por categoría o nombre
* Actualización de stock

---

### 💳 2. Proceso de Venta

* Iniciar nueva venta
* Agregar productos por código de barras
* Aplicar descuentos
* Calcular:

  * Subtotal
  * IVA (16%)
  * Total
* Finalizar venta (actualiza inventario)
* Generar ticket en texto plano

---

### 👤 3. Gestión de Clientes

* Registro de clientes frecuentes:

  * Nombre
  * Teléfono
  * Puntos acumulados
* Asociar cliente a la venta

---

## 🛠️ Tecnologías utilizadas

* Python
* Flask
* HTML / CSS / JavaScript
* SQLite
* Git & GitHub

---

## 📁 Estructura del proyecto

```
com.tienda.abarrotes/
│
├── app.py
│
├── model/
│   ├── cliente.py
│   ├── inventario.py
│   ├── producto.py
│   ├── venta.py
│   ├── producto_granel.py
│   ├── producto_unitario.py
│   ├── detalle_venta.py
│   └── database.py
│
├── view/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   └── templates/
│       ├── index.html
│       ├── inventario.html
│       └── ventas.html
│
├── controller/
│   ├── inventario_controller.py
│   └── ventas_controller.py
│
├── patterns/
│   ├── factory/
│   │   └── producto_factory.py
│   │
│   ├── observer/
│   │   ├── alerta_bajo_stock.py
│   │   └── istock_observer.py
│   │
│   └── strategy/
│       ├── descuento_fijo.py
│       ├── descuento_porcentaje.py
│       └── iestrategia_descuento.py
│
├── utils/
│   └── sin_stock_exception.py
│
└── database/
    └── tienda.db
```

---

## ▶️ Cómo ejecutar el proyecto

```bash
cd com.tienda.abarrotes
source venv/bin/activate
python app.py
```

---

## 🌐 Acceso

Abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## 📚 Buenas prácticas (PEP8)

### 🧠 Nombres

* Variables: `snake_case`

```python
total_venta = 100
```

* Funciones: `snake_case`

```python
def calcular_total():
    pass
```

* Clases: `PascalCase`

```python
class Producto:
    pass
```

* Constantes: `MAYUSCULAS`

```python
IVA = 0.16
```

---

### 📏 Formato

* Máximo 79 caracteres por línea
* Espacios entre funciones y clases
* Indentación de 4 espacios (no tabs)

---

### 🧩 Organización

* Separar lógica (model), rutas (controller) y vistas (HTML)
* No mezclar HTML con lógica Python
* Usar funciones pequeñas y claras

---

## 🌱 Buenas prácticas con Git

### 🔹 Flujo básico

```bash
git add .
git commit -m "mensaje claro"
git push
```

---

### 🔹 Mensajes de commit

* ✔ claros y específicos

```bash
git commit -m "agrega funcionalidad de ventas"
```

* ❌ evitar:

```bash
git commit -m "cosas"
```

---

### 🔹 Uso de ramas

Crear nueva rama:

```bash
git checkout -b feature/nombre
```

Subir rama:

```bash
git push origin feature/nombre
```

---

### 🔹 Pull Request (PR)

1. Subir rama a GitHub
2. Ir al repositorio
3. Click en **Compare & pull request**
4. Explicar cambios realizados
5. Crear PR

---

## 👨‍💻 Autores

* García Reyes Gamaliel
* Montes Olivares Sergio Alonso
