// Appel de la libraire Newping qui possède des commandes pour le capteur ultrason
#include <NewPing.h>  

#define distMax 400 // distance maximale mesurable (en cm)
int trig = 6;       // broche trig du capteur US HC-SR04
int echo = 7;       // broche echo du capteur US HC-SR04

NewPing sonar(trig, echo, distMax);  // initialisation de NewPing (broches etvdistance max)

void setup()      // setup est déroulé une seule fois après la remise à zéro
{
Serial.begin(115200); // initialisation de la liaison série à 115200 bauds
}
void loop() // loop est déroulé indéfiniment
{
int temps = sonar.ping();     // lecture de la durée des ultrasons 
Serial.print(“Le temps mis par les ultrasons est de : ”); 
Serial.print( temps );      // affichage durée du trajet des ultrasons en microsecondes
Serial.println(“ microsecondes”);

float t = temps*0.000001 ;****INSERER UN COMMENTAIRE
***
Serial.print(“Le temps mis par les rasons est de :  ”);
Serial.print(t,6);  //affichage durée du trajet des ultrasons   en  secondes
Serial.println(“ secondes”);
float d = ……………………………… ; // calcul de la distance nous séparant de l’objet
Serial.print(“La distance est de :  ”); Serial.print( d ); // calcul de la distance en mètres Serial.println(“ m”);
delay(5000); //attente pendant 5 secondes avant la prochaine mesure
}
