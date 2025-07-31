# Laboratorio 5: BPM y Servicios Web Basados en Eventos

Este repositorio contiene los archivos necesarios para ejecutar el Laboratorio 5 del curso de BPM, cuyo objetivo es integrar procesos de negocio usando RabbitMQ como bróker de mensajes junto a Bonita Studio y servicios Java externos.

## 🧩 Objetivo

Integrar dos procesos de negocio en Bonita Studio mediante colas de mensajes en RabbitMQ, simulando la comunicación asincrónica entre servicios usando conectores y clientes Java.

## 🛠️ Requisitos

- Java JDK 17 o superior  
- Bonita Studio (última versión)
- RabbitMQ Server (localhost)
- Python 3.x (opcional para pruebas de cliente)
- Git

## 📁 Estructura del repositorio

| Archivo / Carpeta                       | Descripción |
|----------------------------------------|-------------|
| `Collaboration with MQ.bos`            | Proceso de negocio importable en Bonita Studio |
| `proposalProcessClient.jar`            | Cliente Java que consume cola `requests` y responde a `answers` |
| `proposalProcessClient-Java-src.zip`   | Código fuente del cliente Java |
| `connector-rabbitmq-0.0.1-SNAPSHOT.jar`| Conector para usar RabbitMQ en Bonita Studio |
| `amqp-client-5.26.0.jar`               | Librería AMQP oficial de RabbitMQ |
| `slf4j-api-1.7.36.jar`                 | API de logging necesaria para AMQP |
| `slf4j-simple-1.7.36.jar`              | Implementación simple del logger SLF4J |
| `client.py`                            | Cliente Python alternativo para responder mensajes de la cola `requests` |

## 🚀 Instrucciones de uso

### 1. Instalar y ejecutar RabbitMQ

- Instala RabbitMQ y accede a su interfaz en: http://localhost:15672  
- Usuario: guest  
- Contraseña: guest

### 2. Importar proceso en Bonita Studio

- Abre Bonita Studio  
- Importa el archivo `Collaboration with MQ.bos`  
- Asegúrate de instalar el conector `connector-rabbitmq-0.0.1-SNAPSHOT.jar`  
  - Copiarlo a `workspace\connectors` o agregarlo desde el panel de conectores.

### 3. Ejecutar el cliente (Java o Python)

Ejemplo usando Java (requiere las dependencias en el classpath):
```bash
java -cp "proposalProcessClient.jar;amqp-client-5.26.0.jar;slf4j-api-1.7.36.jar;slf4j-simple-1.7.36.jar" proposalProcessClient.Client requests answers
```
### 4. Verificar en RabbitMQ
Mensajes enviados por Bonita aparecerán en la cola requests

Las respuestas del cliente aparecerán en la cola answers

Puedes monitorear desde la UI web de RabbitMQ
