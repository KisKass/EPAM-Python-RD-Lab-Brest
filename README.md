This web-application written by Python and has CRUD management: user  will be able to create new workers, read information about every worker, update this information or delete worker if he is fired. All updates wiil be written in attached database.
the structure of the project is following:
department-app (a project/app directory)
  |__ migrations (includes migration files to manage database schema changes )
  |__ models (includes modules with Python classes describing DB models)
  |__ service (includes modules with functions/classes to work with DB)
  |__ rest (this package must include modules with RESTful service implementation)
  |__ templates (this folder must include web app HTML templates)
  |__ static (this folder must include static files (js, css, images, etc,))
  |__ tests (this package must include modules with unit tests)
  |__ views (this package must include modules with Web controllers/views)
To read extended information describing usability of project open the SRS.md file.
