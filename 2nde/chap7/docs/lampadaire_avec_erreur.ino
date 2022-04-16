int Valeur_A0 ;
float Tension_A0 ;
boolean Etat_lampe ;

void setup() {
  pinMode (11, OUTPUT) 

}

void loop() {
 Valeur_A0 = analogRead(A0) ;
 tension_A0 = (float)Valeur_A0*5/1023 ;

 if ((Tension_A0> 4.0 && (Etat_lampe == true)) {
  digitalWrite (11, LOW) ;
  Etat_lampe = false ;
 }

 if ((Tension_A0< 3.3) && (Etat_lampe == false)) {
  digitalWrite (11, HIGH) ;
  Etat_lamp = true ;
 }

 delay(250) ;
}
