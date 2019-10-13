-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-10-2019 a las 00:37:10
-- Versión del servidor: 10.4.6-MariaDB
-- Versión de PHP: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `recetas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recetas_recetas`
--

CREATE TABLE `recetas_recetas` (
  `id` int(11) NOT NULL,
  `receta` mediumtext COLLATE utf8_bin NOT NULL,
  `pasos` mediumtext COLLATE utf8_bin NOT NULL,
  `ingredientes` mediumtext COLLATE utf8_bin NOT NULL,
  `descripcion` mediumtext COLLATE utf8_bin NOT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `imagen` varchar(100) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `recetas_recetas`
--

INSERT INTO `recetas_recetas` (`id`, `receta`, `pasos`, `ingredientes`, `descripcion`, `tipo_id`, `imagen`) VALUES
(1, 'Ensalada campera', 'Lo primero es cocer las patatas, las lavaremos bien y las coceremos en agua con sal sin pelarlas. Dependiendo del tamaño pueden tardar entre 20 o 40 minutos, para comprobar que están listas pinchad con la punta del cuchillo, este debe entrar sin resistencia. Otra opción es utilizar patatas «para cocer en microondas» que se cocinan al vapor en su propia bolsa en 8 minutos.\r\n\r\nUna vez cocidas, las pelamos, cortamos en rodajas y ponemos en la base de una fuente. Encima ponemos los tomates lavados y troceados, los dos pimientos cortados en rodajas finas, al igual que la cebolleta, los huevos cocidos y el atún que troceamos. Y por último un buen chorreón de aceite de oliva virgen extra y un poco de sal.\r\n\r\nEsta ensalada campera está riquísima y es una opción fantástica para toda la familia este verano.', 'Medio kilo de patatas\r\n1 pimiento verde\r\n1 pimiento rojo\r\n2 o 3 tomates\r\n1 cebolleta\r\n2 huevos cocidos\r\n1 lata (160 gr) de atún (al natural si queréis reducir las calorías)\r\nAceite de oliva virgen extra\r\nSal', 'Ensalada campera, sin duda una de las ensaladas estrella del verano. Y es que llegó el calor y en esta época ya sólo apetecen cosas frescas y rápidas, como esta ensalada o la ensalada de lentejas que os propusimos tiempo atrás.\r\n\r\nAdemás la ensalada campera es un plato muy completo al igual que una ensalada de pasta,  ya que lleva los hidratos de las patatas, las proteínas del huevo y el atún y las vitaminas de las verduras y hortalizas, por lo que puede servirse como plato único.', 2, 'recetas/saluda_ShS8MMG.jpg'),
(2, 'Gratín de patatas', 'Preparación del Gratín de patatas fácil\r\nEncendemos el horno a 220ºC con calor arriba y abajo sin ventilador para que se vaya precalentando.\r\n Pelamos las patatas y las cortamos en rodajas finísimas con un cuchillo bien afilado o de una mandolina, yo lo he hecho con esta última en la posición de 2 mm.\r\nLas ponemos en un bol, añadimos el resto de ingredientes y mezclamos bien para que se embadurnen lo máximo posible.\r\nEngrasamos una fuente para horno -o dos fuentes individuales- y colocamos las patatas apilándolas de manera que tengamos una altura de unos 3 centímetros.\r\nHorneamos durante unos 30 minutos a 220ºC hasta que la superficie esté dorada a nuestro gusto y al pinchar con un tenedor las patatas estén tiernas -si vemos que se doran demasiado por arriba, pero aún están duras, las tapamos con papel de aluminio hasta que se terminen de hacer.', 'Patatas Kennebec, 3 medianas\r\nMantequilla sin sal en punto pomada, 2 cucharadas\r\nQueso Parmesano rallado, 3 cucharadas\r\nSal, ½ cucharadita\r\nAjo en polvo, 1 cucharadita\r\nPimienta recién molida, 3 o 4 vueltas\r\nOrégano seco o tomillo, 1 cucharada\r\nAceite o mantequilla para engrasar la fuente', 'VEGETARIANAS\r\nGratín de patatas fácil, receta paso a paso\r\nReceta fácil con explicación detallada y vídeo de los pasos a seguir para preparar un gratín de patatas perfecto como guarnición de otros platos.\r\n23 febrero, 2016 12:00\r\n ESPECIAS MANTEQUILLA PATATAS QUESO VIDEORRECETA\r\nMer Bonilla\r\nPreparación: 10 min Cocción: 30 min Total: 40 min Comensales: 2 Calorías: 132 Tipo de comida: Guarnición\r\n\r\nIngredientes\r\nPatatas Kennebec, 3 medianas\r\nMantequilla sin sal en punto pomada, 2 cucharadas\r\nQueso Parmesano rallado, 3 cucharadas\r\nSal, ½ cucharadita\r\nAjo en polvo, 1 cucharadita\r\nPimienta recién molida, 3 o 4 vueltas\r\nOrégano seco o tomillo, 1 cucharada\r\nAceite o mantequilla para engrasar la fuente\r\nPocos alimentos conozco que sean tan versátiles como las patatas, hay mil formas de prepararlas y siempre están ricas, vale que vivo en Galicia y aquí todo resulta siempre mejor con unas patatitas, pero oye, son baratas y pueden llegar a ser muy lucidas. Así que hoy va de patatas el asunto.', 1, 'recetas/vegetariana.jpg'),
(3, 'Polenta Rellena', 'Para el relleno, mezclar la carne con el condimento para carne Gourmet. Calentar el aceite en una sartén, agregar la cebolla y cocinar hasta que esté blanda y transparente. Incorporar los aliños y cocinar por un minuto. Agregar la carne y los cubos de tomates, cocinar hasta que la carne esté cocida y los tomates blandos. Probar para ajustar sazón. Reservar.\r\nPoner film plástico por dentro de 6 moldes (1 ½ taza de capacidad, aprox.).\r\nPreparar la polenta. Poner el agua hirviendo en una olla y agregar el caldo de verduras Gourmet, revolver hasta integrar. Añadir la leche y cocinar a fuego medio bajo hasta que el líquido esté caliente. Incorporar la polenta en forma de lluvia y revolver hasta que la mezcla esté espesa y se vea el fondo de la olla. Sacar del fuego, agregar la mantequilla y el queso, revolver hasta integrar. Poner la polenta en el fondo y bordes de los moldes preparados, dejando un espacio para poner el relleno. Poner la mezcla de carne al medio y luego tapar con un poco de polenta. Dejar enfriar y luego desmoldar (ayudándose con el film plástico) sobre una bandeja de horno aceitada.\r\nPara servir, Espolvorear con un poco de queso parmesano y calentar en horno a 180°C por 10 a 15 minutos o hasta que la polenta esté caliente.', '2 tazas de agua hirviendo\r\n1 sobre de Caldo de Verduras Gourmet\r\n1 taza de leche\r\n1 cucharada de Orégano Entero Gourmet\r\n1 cucharadita de Sal de Mar Gourmet\r\n1 ½ tazas de polenta\r\n1 cucharada de mantequilla\r\n½ taza de queso parmesano rallado, mas para espolvorear', 'La polenta es una comida de harina de maíz hervida, originaria de Italia y muy difundida también en Austria, el sur de Francia (Córcega, Niza y Saboya) y Suiza, la isla de Madeira, donde se le llama milho, y la península de los Balcanes (Bosnia, Croacia, Eslovenia, Serbia y Romania).', 3, 'recetas/gourmet_O3vc8TD.jpg'),
(4, 'Pechugas de pollo en salsa', 'En una fuente apta para horno ponemos tres patatas cortadas en trozos con piel bien limpias y cebolleta a tiras. Horneamos durante 15 minutos, colocamos una bolsa de tomates cherry y las pechugas de pollo en el centro (la mitad de cada pechuga entera) sobre cada mitad, ponemos medio queso mozarella a trocitos, cerramos con la otra mitad de pechuga de pollo.\r\n\r\nPor último añadimos un puñado de aceitunas negras sin hueso a trocitos pequeños o enteras como más os gusten, dos cucharaditas de aceite de oliva virgen extra, sal y pimienta negra. Llevamos al horno a 180º calor arriba y abajo durante 15 minutos aproximadamente.', '2 pechugas de pollo partidas por la mitad.\r\n3 patatas\r\nQueso mozzarella\r\nAceitunas negras sin hueso\r\nTomates cherry\r\n1 cebolleta fresca\r\nAceite de oliva virgen extra\r\nSal\r\nPimienta', 'Las pechugas de pollo en salsa es un plato económico, resultón y muy rico, además tiene poca elaboración y es muy ligero. Seguro que una vez lo probéis, se convertirá en una de vuestras recetas favoritas y por muchos motivos. Tanto si las utilizáis para hacer unas fajitas de pollo como para hacer pollo al limón o cualquier otra, siempre es un éxito, especialmente entre los más pequeños de la casa, a quienes las recetas de pollo suelen volverles locos.\r\n\r\nEs una receta completa y variada, con pocas grasas y las que tiene son saludables. Al hacer las pechugas de pollo al horno evitamos tener que freírlas, una preparación mucho más saludable, el queso lo incorporamos una vez las pechugas estén cocinadas, para evitar que se funda, de esta manera aportará un toque de frescor y una textura deliciosa.', 4, 'recetas/facil_nxWGcme.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `recetas_recetas`
--
ALTER TABLE `recetas_recetas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recetas_recetas_tipo_id_fc04c021_fk_tipo_descripcion_id` (`tipo_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `recetas_recetas`
--
ALTER TABLE `recetas_recetas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `recetas_recetas`
--
ALTER TABLE `recetas_recetas`
  ADD CONSTRAINT `recetas_recetas_tipo_id_fc04c021_fk_tipo_descripcion_id` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_descripcion` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
