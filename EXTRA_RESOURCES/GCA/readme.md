<h1 align="center"> FelipedelosH </h1>
<br>
<h4>GCA</h4>

![Banner](Docs/banner.png)
<br>
:construction: Status of project :construction:
<br>
This is a automate code generator for Java Spring boot. You need create a templates (API, Entity, DAO, UseCases) to generate a automatic code java for springboot.

## :hammer:Funtions:

- `Function 1`: Load a Class Diagram with extension .drawio<br>
- `Function 2`: Make a AUTOMATIC .sql query to insert all tables to class diagram<br>
- `Function 3`: Make a AUTOMATIC Entity.java FILE WITH(Constructs, Getters&Setters and toJson) for every entity in class Diagram<br>
- `Function 4`: Make a AUTOMATIC APIRest.java FILE to get all same entities from use case fro every class in diagram<br>
- `Function 5`: Make a AUTOMATIC DAO pattern in java to acces DB for every entity in class diagram<br>
- `Function 5`: Make a AUTOMATIC Mapper to conver DAO entity to Domain Entity<br>


## :play_or_pause_button:How to execute a project

Charge you "classDiagram.drawio" in folder "input" (put the name of file in _PATH_DRAWIO_CLASES_FILE = "input/classDiagram.drawio" in main.py file) execute with Double click in main.py all result files find in "output" folder.

## :hammer_and_wrench:Tech.

- PYTHON
- XML
- DRAW.IO
- output SQL file.
- ourput JAVA file.

## :warning:Warning.

- the software CAN'T put the name of sql tables (Not plural words hable).
- if you try to use this script in another Spring boot project you need change the tenplates.

## Autor

| [<img src="https://avatars.githubusercontent.com/u/38327255?v=4" width=115><br><sub>Andrés Felipe Hernánez</sub>](https://github.com/felipedelosh)|
| :---: |