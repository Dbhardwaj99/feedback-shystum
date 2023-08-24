#dockerfile to run sql
FROM mysql:5.7.34
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=password

# ADD a init.sql to the docker-entrypoint-initdb.d/ directory
ADD init.sql /docker-entrypoint-initdb.d/

# Expose port 3306
EXPOSE 3306

# Run the command to start mysql
CMD ["mysqld"]