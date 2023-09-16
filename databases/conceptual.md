### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language

- What is the difference between SQL and PostgreSQL?
    SQL - Sructured query language
        - A language to write querys to databases
    PostgreSQL - A relational database management system that uses and extends the SQL language combined with other features  

- In `psql`, how do you connect to a database?
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///{database_name}'

- What is the difference between `HAVING` and `WHERE`?
      Where - Filters results from the table
      Having - Filters results from a group

- What is the difference between an `INNER` and `OUTER` join?
      Inner Join - returns matching data from 2+ tables based off specified criteria
      Outer Join - An inner join but with addional data being returned by the table being specified, either right, left or full

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
      Right Outer - returns all the records from the Right table
      Left Outer - returns all the records from the Left table

- What is an ORM? What do they do?
      Object Relational Mapper -  technique for converting data between a relational database and object-oriented programming language
     
      SQLAlchemy is an ORM written in Python to give developers the power and flexibility of SQL
          

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
    HTTP request - client side - runs though the browser, 
    Server side - request are processing on web servers


- What is CSRF? What is the purpose of the CSRF token?
    CSRF - Cross-Site Request Forgery -  an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated.
    CSRF Token - CSRF Tokens are secure random tokens that are hidden in a users session and sent along with a request to verify legitimacy of the end-user request.
               
  

- What is the purpose of `form.hidden_tag()`?
  To hide to csrf token from the UI