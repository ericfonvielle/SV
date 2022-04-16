// déclaration des constantes
int           portTemp = 0;             // la tension aux bornes de la CTN est envoyée sur le port température : port analogique 0
float         a =-0.1303 ;                   // coefficient  a 
float         b = 112.87;                    // coefficient b
int           portVentilateur = 3;      // la commande du ventilateur se fait par le port numérique 3
int           consigne = 55;            // valeur de la consigne 
int           K = 5;                   // valeur du coefficient de proportionnalité
float         Ki = 0.02;                   // valeur du coefficient d'intégration

// Définition des variables
int           N = 0;                    //  variable nombre N sur port température
float         Temp;                     // variable température mesurée par le capteur
int           commandeVitesse = 0;      // pourcentage de la commande de vitesse de 0 à 100%
float         sommeEcart = 0 ;          // variable pour la commande PI



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

// attente commande de la consigne donnée sur port série
  int entier_recu = 0;
  while ( Serial.available() ) 
  {
    int octet_lu = Serial.read();
    entier_recu = ascii_vers_int(entier_recu, octet_lu);
   }
   if ( entier_recu != 0 ) 
  {
    consigne = entier_recu ;
  }

// génération de la commande en regulation PI
  sommeEcart = sommeEcart + (Temp-consigne);
  commandeVitesse = K*(Temp - consigne)+ Ki*sommeEcart;

// conditions limites
  if (commandeVitesse > 100) {commandeVitesse = 100 ;}
  if (commandeVitesse < 0) { commandeVitesse = 0 ;}



//commande de la vitesse du ventilateur
  analogWrite(portVentilateur,255*commandeVitesse/500); // division par (5 *100) le facteur 5 limite l'excursion de ventilation de 0 à 20% (voir caract statique Artic 64 GT  
  Serial.print(consigne);
  Serial.print(",");
  Serial.print(Temp);
  Serial.print(",");
  Serial.println(commandeVitesse);
  delay(1000);
}

// fonction de conversion d'un octet en nombre
int ascii_vers_int(int n, int octet_lu)
{
  return n*10 + (octet_lu - 48);
}
