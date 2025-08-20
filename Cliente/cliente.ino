/*
 *  This sketch sends a message to a TCP server
 *
 */

#include <WiFi.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>

WiFiMulti WiFiMulti;

#define MetroDigital 34
int valor;

//const char *ssid = "PEINE-3";
//const char *password = "etecPeine3";

const char *ssid = "ETEC-UBA";
const char *password = "ETEC-alumnos@UBA";
const char *serverName = "http://10.9.120.87:7000/api/sensor";

void setup() {

  pinMode(MetroDigital, INPUT);
  Serial.begin(115200);
  delay(10);

  // We start by connecting to a WiFi network
  WiFiMulti.addAP(ssid, password);

  Serial.println();
  Serial.println();
  Serial.print("Waiting for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    Serial.flush();
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  delay(500);
}

void loop() {
  delay(1000);

  if(WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    HTTPClient http;
    valor = analogRead(MetroDigital);
    http.begin(client, serverName);
    http.addHeader("Content-Type", "application/json");
    Serial.print("Enviando valor: ");
    Serial.println(valor);
    String jsonStr = "{\"nombre\":\"MetroDigital\",\"valor\":" + String(valor) + "}"; 
    //char *jsonStr = "{\"nombre\":\"luxometro\",\"valor\":145}";
    int httpResponseCode = http.POST(jsonStr);
    Serial.print("Respuesta: ");
    Serial.println(httpResponseCode);
    http.end();
  } else {
    Serial.println("Desconectado");
  }
}