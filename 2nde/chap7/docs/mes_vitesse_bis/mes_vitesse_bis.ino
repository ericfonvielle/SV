//declaration des constantes (avec valeur)
#define USEcho 7     //echo sur le pin digital 3 
#define USTrig 6     //trig sur le pin digital 2
int n = 10000;
int att = 10; 
int i=0;                  //declaration des variables (nom et type) 
unsigned long duree;
float vitesse;

void setup()               //réalisé une fois à la mise sous tension de la carte
{
Serial.begin(115200);     //initialisation de la connexion série et choix du débit
pinMode(USTrig, OUTPUT);  //on envoie des pulses sur le trig 
pinMode(USEcho, INPUT);   //on lit les retour sur echo
}

void loop()               //realisé en boucle ensuite
{
if (i<n){
digitalWrite(USTrig,HIGH);  //un pulse creneau de 10 microsecondes 
delayMicroseconds(10);      //suite
digitalWrite(USTrig,LOW);   //suite

duree = pulseIn(USEcho,HIGH,30000);   //on attend le retour delai maxi 30000 microsecondes
Serial.println(duree);                //on ecrit la valeur dans le moniteur série 

////////////////////////////////////////////////////////////////
vitesse =              // Ecrire ici la formule de la vitesse
Serial.println(vitesse);
//////////////////////////////////////////////////////////////////
i++;

}
delay(att);
}
