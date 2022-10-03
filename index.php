<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>PHP</title>
</head>
<body>
    <div id="container">
        <div id="header">Fejléc</div>
        <div id="nav">
        <ul>
            <li><a href="index.php?page=home">Home</a></li>
            <li><a href="index.php?page=products">Products</a></li>
            <li><a href="index.php?page=services">Services</a></li>
            <li><a href="index.php?page=about">About Us</a></li>
            <li><a href="index.php?page=contact">Contact</a></li>
        </ul>
    </div>
    
    <div id="content">
        <?php include_once("inc/" . $page . ".php"); ?>
    </div>
        <div id="footer">Lábléc</div>
    </div>
</body>
</html>
