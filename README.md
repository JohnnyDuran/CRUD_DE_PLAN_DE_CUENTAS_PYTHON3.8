# CRUD_DE_PLAN_DE_CUENTAS_PYTHON3.8
Esta es mi tarea de CRUD de Plan de Cuentas
Para que puedas trabajar con este programa debes crear una base de datos sea en MySQL o MariaDB(HeidiSQL)
Recuerda: En el archivo de conexion.py debes configurar el usuario y contraseña que usas en el HeidiSQL donde
copiaras y crearas esta base de datos.
Nombre de la base (Ya especificado en el codigo): db_tarea_crud
Integrantes de la creacion del codigo: Johnny Duran y Gabriela Loyola
Realizado en Base a la Tarea Crud de Plan de Cuentas, Programacion Web, 6to Semestre, Docente: Daniel Vera
SCRIPT DE BASE DE DATOS ANEXADO AQUI EN EL README.md
**********************************************************************************************************************
/*---Script de la Base de Datos---*/

/********************************/
/*Correr este codigo en HeidiSQL*/
/********************************/

CREATE DATABASE db_tarea_crud;
USE db_tarea_crud;
CREATE TABLE Grupo
(
  id INT NOT NULL AUTO_INCREMENT,
  descripcion VARCHAR(50),
  PRIMARY KEY (id)
);
CREATE TABLE PlanCuenta 
(
  id INT NOT NULL AUTO_INCREMENT,
  codigo VARCHAR (20),
  grupo INT NOT NULL ,
  descripcion VARCHAR(100),
  naturaleza VARCHAR(1),
  estado BOOLEAN,
  PRIMARY KEY (id),
  FOREIGN KEY (grupo) REFERENCES Grupo(id)
);

INSERT INTO Grupo (descripcion) VALUES('Activo');
INSERT INTO Grupo (descripcion) VALUES('Pasivo');
INSERT INTO Grupo (descripcion) VALUES('Patrimonio');
INSERT INTO Grupo (descripcion) VALUES('Ingreso');
INSERT INTO Grupo (descripcion) VALUES('Gastos');

INSERT INTO PlanCuenta(codigo,grupo,descripcion,naturaleza,estado) 
VALUES ('01',1,'Caja','D',TRUE);
INSERT INTO PlanCuenta(codigo,grupo,descripcion,naturaleza,estado) 
VALUES ('02',1,'Banco','D',TRUE);
INSERT INTO PlanCuenta(codigo,grupo,descripcion,naturaleza,estado) 
VALUES ('03',2,'Cuenta x P.','A',TRUE);
INSERT INTO PlanCuenta(codigo,grupo,descripcion,naturaleza,estado) 
VALUES ('04',3,'Cap. Cont.','A',TRUE);
INSERT INTO PlanCuenta(codigo,grupo,descripcion,naturaleza,estado) 
VALUES ('05',4,'Ventas','A',TRUE);
INSERT INTO PlanCuenta(codigo,grupo,descripcion,naturaleza,estado) 
VALUES ('06',5,'Compras','D',TRUE);
INSERT INTO PlanCuenta(codigo,grupo,descripcion,naturaleza,estado) 
VALUES ('07',5,'Arriendo','D',FALSE);
*********************************************************************************************************************
