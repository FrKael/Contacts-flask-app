# FlaskApp

Running the mysqldb with a docker line, I decide do not create a volume because I want to build the image to migrate to another enviorement in the and i do not want posible troubles with the deploy.

```yaml
docker run -it --name mysqlflask -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret mysql

docker pull frkael/mysqlflask:v1.0
```

pendiente completar la condición para no enviar archivos en blanco desde index.html
