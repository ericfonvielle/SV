// déclaration des constantes
int           portTemp = 0;             // la tension aux bornes de la CTN est envoyée sur le port température : port analogique 0
float         a =1 ;                   // coefficient  a 
float         b = 1;                    // coefficient b
int           portVentilateur = 3;      // la commande du ventilateur se fait par le port numérique 3
int           consigne = 45;            // valeur de la Consigne 
int           K = 5;                   // valeur du coefficient de proportionnalité

// Définition des variables
int           N = 0;                    //  variable nombre N sur port température
float         Temp;                     // variable température mesurée par le capteur
int           commandeVitesse = 0;      // pourcentage de la commande de vitesse de 0 à 100%


void setup()
{
  // initialisation serial port
  Serial.begin(9600);

    pinMode(portVentilateur, OUTPUT);
}

void loop()
{
  N = analogRead(portTemp); //Lecture N
  Temp = a * N + b;         //calcul température T

// génération de la commande en regulation P
// à compléter
  commandeVitesse = K*(                 );

// conditions limites
  if (commandeVitesse > 100) {commandeVitesse = 100 ;}
  if (commandeVitesse < 0) { commandeVitesse = 0 ;}



//commande de la vitesse du ventilateur
  analogWrite(portVentilateur,255*commandeVitesse/100);
  
  Serial.print(consigne);
  Serial.print(",");
  Serial.print(Temp);
  Serial.print(",");
  Serial.println(commandeVitesse);
  delay(1000);
}
