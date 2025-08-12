/*
Etant donné que je n'avais pas compris qu'il fallait utilisé le ascii et que j'ai vu la réponse un poil trop tard,
j'ai corrigé la réponse quelques minutes après 16h. 

De base comme je n'avais pas compris la question j'avais fais un simple console.log("Hello Nalios !") mais cela me parraissait suspect que ce soit aussi simple.

Voici donc la version avec la valeur en ascii des caractère mais je voulais être honnête sur le fait que la correction de cet exercice à été fait un poil après 16h et vous laisser juger ce qu'il en convient :)
*/

function hello() {
	asciiMessage = [72, 101, 108, 108, 111, 44, 32, 78, 97, 108, 105, 111, 115, 32, 33];
	console.log(String.fromCharCode(...asciiMessage));
}

hello()
