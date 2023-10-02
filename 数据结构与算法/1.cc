#include <Wire.h>
#include "SSD1306Wire.h"
// #include <string>
// #include <RTClib.h>
// OLED引脚定义
#define SDA 19
#define SCL 18
SSD1306Wire display(0x3c, SDA, SCL);
// using namespace std;
char timeString[9];
unsigned int h = 19;
unsigned int m = 5;
unsigned int s = 34;
void setup()
{
    // 初始化显示器
    display.init();
    display.flipScreenVertically();
    display.setFont(ArialMT_Plain_24);
    // display.setTextAlignment(TEXT_ALIGN_CENTER);
}

void loop()
{

    // timeString = to_string(h) + ":" + to_string(m) + ":" + to_string(s);
    sprintf(timeString, "%02d:%02d:%02d", h, m, s);
    // 显示时间
    display.drawString(8, 8, timeString);
    // 刷新显示内容
    display.display();
    // 延迟一秒
    delay(1000);
    s++;
    if (s > 59)
    {
        s -= 60;
        m++;
        if (m > 59)
        {
            m -= 60;
            h++;
            if (h > 23)
            {
                h -= 24;
            }
        }
    }
    display.clear();
}