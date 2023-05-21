#include <SPI.h>
#include <MFRC522.h>
#define SS_PIN 10
#define RST_PIN 9
MFRC522 rfid(SS_PIN, RST_PIN);

void setup() { 
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  Serial.println("OK");
}
 
void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readString();
    input.toUpperCase();
    if (input == "!PING") {
      Serial.println("PONG");
    }
  }
  if(!rfid.PICC_IsNewCardPresent()) {
    return;
  }
  if(!rfid.PICC_ReadCardSerial()) {
    return;
  }
  String content="";
  byte letter;
  for (byte i = 0; i < rfid.uid.size; i++) {
    content.concat(String(rfid.uid.uidByte[i] < 0x10?" 0":" "));
    content.concat(String(rfid.uid.uidByte[i], HEX));
  }
  content = content.substring(1);
  content.toUpperCase();
  Serial.println(content);
  delay(3000);
}
