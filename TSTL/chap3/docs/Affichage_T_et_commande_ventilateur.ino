// déclaration des constantes
int           portTemp = 0;             // la tension aux bornes de la CTN est envoyée sur le port température : port analogique 0
float         a = -0.1459 ;                   // coefficient  a
float         b = 120.17;                    // coefficient b
int           portVentilateur = 3;      // la commande du ventilateur se fait par le port numérique 3

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

//commande de la vitesse du ventilateur
// division par 500 pour que la variation de 0 à 20% soit ramenée à une variation virtuelle de 0 à 100% 
  analogWrite(portVentilateur,255*commandeVitesse/500);
  


  Serial.print("Température = ");
  Serial.print(Temp);
  Serial.println(" °C");
  delay(1000);
}
