#include <Adafruit_VL53L0X.h>
#include <Wire.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// OLED on Wire1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire1, -1);

// TOF sensor on Wire
Adafruit_VL53L0X tof;

void setup() {
  Serial.begin(9600);
  delay(2000);

  // -------- I2C bus 0 for VL53L0X --------
  Wire.setSDA(2);   // sensor SDA
  Wire.setSCL(3);   // sensor SCL
  Wire.begin();

  if (!tof.begin(0x29, false, &Wire)) {
    Serial.println("Failed to boot VL53L0X");
    while (1) delay(10);
  }

  // -------- I2C bus 1 for OLED --------
  Wire1.setSDA(20); // OLED SDA
  Wire1.setSCL(21); // OLED SCL
  Wire1.begin();

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED failed");
    while (1) delay(10);
  }

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Ready");
  display.display();

  Serial.println("System started");
}

void loop() {
  VL53L0X_RangingMeasurementData_t measure;
  tof.rangingTest(&measure, false);

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 20);

  if (measure.RangeStatus != 4) {
    Serial.print("Distance: ");
    Serial.print(measure.RangeMilliMeter);
    Serial.println(" mm");

    display.print(measure.RangeMilliMeter);
    display.print(" mm");
  } else {
    Serial.println("Out of range");
    display.print("No reading");
  }

  display.display();
  delay(100);
}