#include <dht11.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#define DHT11PIN 3
dht11 DHT11;
LiquidCrystal_I2C lcd(0x27,16,2);
int coffee = 0;
int starttime;
int timeout;
void setup() {
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
  pinMode(A12, OUTPUT); 
  pinMode(A1, OUTPUT);
  lcd.init();                      // Инициализация дисплея  
  lcd.backlight();                 // Подключение подсветки
  lcd.setCursor(0,0); 
  lcd.print("Hello");
  
}

void loop() {
  
  int chk = DHT11.read(DHT11PIN);
  int hum = DHT11.humidity;
  int temp = DHT11.temperature;
  lcd.setCursor(0,0);
  lcd.print("HUMIDITY(%)"); 
  lcd.setCursor(12,0);
  lcd.print(DHT11.humidity);
  lcd.setCursor(0,1);
  lcd.print("TEMP (C)" ); 
  lcd.setCursor(12,1);
  lcd.print(DHT11.temperature);
  if(Serial.available())
  {
    switch(Serial.read())
    {
      case '0':
      digitalWrite(A0, LOW);
      break;
      case '1':
      digitalWrite(A0, HIGH);
      break;  
      case '3':  
        Serial.print(String(DHT11.humidity)); 
        Serial.print(String(DHT11.temperature));
        break;
      case '4':
        digitalWrite(A1, LOW);
        break;
      case '5':
        digitalWrite(A1, HIGH);
        break;
   }

   
  }
  

}
