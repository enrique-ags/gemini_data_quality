-- Tabla: Empleados
CREATE TABLE Empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    id_salario INT
);

-- Insertar 10 registros en la tabla Empleados
INSERT INTO Empleados (id, nombre, edad, id_salario) VALUES
(1, 'Juan Pérez', 30, 101),
(2, 'María López', 25, 102),
(3, NULL, 35, 103),
(4, 'Pedro García', 40, NULL),
(5, 'Ana Martínez', 28, 105),
(6, 'Luis Rodríguez', 33, 106),
(7, NULL, 22, 107),
(8, 'Sofía Hernández', 45, NULL),
(9, 'Carlos Díaz', 38, 109),
(10, 'Laura Fernández', 31, 110);

---

-- Tabla: Salarios
CREATE TABLE Salarios (
    id_salario INT PRIMARY KEY,
    salario DECIMAL(10, 2)
);

-- Insertar registros en la tabla Salarios (uno de ellos mal)
INSERT INTO Salarios (id_salario, salario) VALUES
(101, 50000.00),
(102, 60000.00),
(103, 45000.00),
(104, 70000.00),
(105, 55000.00),
(106, 62000.00),
(107, 48000.00),
(108, 75000.00),
(109, 999999.99), -- Valor de salario mal
(110, 53000.00);