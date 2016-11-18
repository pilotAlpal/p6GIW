<!DOCTYPE html>
<html lang="es">
<head>
<title>Lista de libros</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Libros</h1>
    </header>
    <ul>
    % for libro in lista:
      <li> {{libro[0]}} </li>
    % end
    </ul>    
</body>
</html>