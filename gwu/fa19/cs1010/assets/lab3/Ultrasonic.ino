#define ECHOPIN 2
#define TRIGPIN 3

int distance = 0;
int time = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ECHOPIN, INPUT);
  pinMode(TRIGPIN, OUTPUT);
}

void loop() {
  //time = millis();
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(5);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPIN, LOW);
  pinMode(ECHOPIN,INPUT);
  distance = pulseIn(ECHOPIN, HIGH);
  distance = distance/(2 * 29.1);
  //Serial.print(time);
  //Serial.print(" ");
  Serial.println(distance);
  delay(50);
}
