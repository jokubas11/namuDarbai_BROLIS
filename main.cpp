#include "mbed.h"
#include "LM75B.h"
#include "C12832.h"
#include "IAP.h"

#define     MEM_SIZE        256
#define     TARGET_SECTOR    24

void getFlashMemory( char *p, int n );
void getTemperature();
void LED(bool greenLED, bool redLED);
void writeData();
void deleteFlashMemory();
void clearScreen();
void readButton();
void readFlashMemory();
void getTime(time_t seconds);
void setTime();

Serial pc(USBTX, USBRX);
C12832 lcd(p5, p7, p6, p8, p11);
LM75B sensor(p28,p27);
PwmOut redLight (p23);
PwmOut greenLight (p24);
DigitalIn inputButton(p14);
IAP iap;

float temperatureMeasure = 0.0;
/////////////////
char answerToRequest[18]; // 0 - symbol for next step, 1-16 - info, 17 = \n
char receivedRequest[18]; // 0 - symbol for next step, 1-16 - info, 17 = \n
char buffer[32]; // buffer to keep things
char deviceData[33]; // 0-15 name, 16-31 serial number, 32 = \n
/////////////////
long int timeRTC;
char *trash; // one of used functions require to use a pointer, even though I don't need it
/////////////////
bool nameIsSet = false;
bool serialIsSet = false;

int main()
{
        
    redLight = 1.0;  
    greenLight = 1.0;

    // Check if name or serial no is in flash memory
    // If so, move it to deviceData
    
    getFlashMemory(sector_start_adress[ TARGET_SECTOR ], 32);
    if ((strlen(deviceData) > 16) && (deviceData[0] != ' ')) {
        nameIsSet = true;
        serialIsSet = true;
        }
    else if ((strlen(deviceData) < 16) && (deviceData[0] != ' ')) {
        nameIsSet = true;
        serialIsSet = false;
        }
    else if ((strlen(deviceData) > 16) && (deviceData[0] == '\n')) {
        nameIsSet = false;
        serialIsSet = true;
        }
    else {
        // leave unset
        }        

    // mbed always waits for request    
    while(1) {
            
        pc.scanf("%s", receivedRequest);
        
        // time calculating 
        time_t seconds = time(NULL);

        clearScreen();

        if (receivedRequest[0] == 'a') {
            getTemperature();            
        }
        if (receivedRequest[0] == 'b') {
            readButton();
        }
        if (receivedRequest[0] == 'c') { 
            readFlashMemory();
        }
        
        if (receivedRequest[0] == 'd') {
            getTime(seconds);
        }
        
        if (receivedRequest[0] == 'e') {             
            setTime();            
        }
        
        if (receivedRequest[0] == 'f' || receivedRequest[0] == 'g') {
            writeData();            
        }
        
        if (receivedRequest[0] == 'h') {
            deleteFlashMemory();
            nameIsSet = false;
            serialIsSet = false;
            pc.printf("h\n");
            LED(true, false);
        }
        else {
            // if request unrecognized, return "x\n"
        }

        // delete everything that has been stored before, except deviceData
        memset(receivedRequest,0,sizeof(receivedRequest));
        memset(answerToRequest,0,sizeof(answerToRequest));
        memset(buffer,0,sizeof(buffer));
    }
    
}

#include    <ctype.h>

// function reads from flash memory
// more: https://os.mbed.com/users/okano/code/IAP_internal_flash_write//file/382f38b15c22/main.cpp/

void getFlashMemory( char *base, int n )
{
    unsigned int    *p;
    char            s[17]   = { '\x0' };
    int k = 0;

    // gets hexadecimal values and writes them into deviceData
    p   = (unsigned int *)((unsigned int)base & ~(unsigned int)0x3);
 
    for ( int i = 0; i < (n >> 2); i++, p++ ) {
        if (!(i % 4)) { 
            for (int j = 0; j < 16; j++) {
                s[j]  = isgraph((int)(*((char *)p + j))) ? (*((char *)p + j)) : ' ';
                deviceData[k] = s[j];
                k++;
            }
        }
    }   
}

// function to read temperature
void getTemperature()
{   
    char stringTemp[9];
    if (sensor.open()) {    
        
        // get temp value
        temperatureMeasure = sensor.temp();

        // convert to string, because we are returning string 
        sprintf(stringTemp, "%.3f\n", temperatureMeasure);
        
        // write the answerToRequest
        answerToRequest[0] = 'a';        
        int i = 1;
        while(stringTemp[i] != '\n') {
            answerToRequest[i] = stringTemp[i-1];
            i++;
        }
        answerToRequest[i] = '\n';

        // answer is returned
        pc.printf("%s", answerToRequest);

        // print temperature and flash LED
        lcd.printf("Temperature: %s", stringTemp);
        LED(true, false);

    } 
    
    else {
        
        // if request is bad, return error
        answerToRequest[0] = 'a';
        answerToRequest[1] = '\n';
        pc.printf("%s\n", answerToRequest);
        lcd.printf("Error! Cannot measure temperature!");
        LED(false, true);
    }
}

// function to light LED
// takes two arguments, depending on which light you need
// for green, send greenLED = true
// for red, send redLED = true

void LED(bool greenLED, bool redLED)
{
    PwmOut *addressForLed;
    
    if (greenLED == true && redLED == false) {
        addressForLed = &greenLight;
        }
    else if (greenLED == false && redLED == true) {
        addressForLed = &redLight;
        }
    else {
        LED(false, true);
        }

    for (int i = 0; i < 5; i++) {
        *addressForLed = 0.0;
        wait(0.05);
        *addressForLed = 1.0;
        wait(0.05);
        }
}

// function writes RAM memory into flash
// Mbed allows to write only sectors of size 256, 512, 1024, 2048
// We write data we need to save into mem, then fill rest with empty addresses

void writeData() {
        char    mem[ MEM_SIZE ]; // this array will be written into memory
        int     r; // used for some of memory writin functions  
        
        // this part if we are asked to write name
        if (receivedRequest[0] == 'f') {            
            for (int i = 0; i < 32; i++) {                
                if (i < 16) {                    
                    if (i < (strlen(receivedRequest)-1)) {                        
                        mem[i] = receivedRequest[i+1];                           
                        }
                    else {                        
                        mem[i] = ' ';                        
                        }
                    }                
                else {                    
                    if (serialIsSet == true) {                        
                        mem[i] = deviceData[i];                        
                        }
                    else {
                        mem[i] = ' ';
                        }
                    nameIsSet = true;
                    }
                }
            }
        // this part if we are asked to write serial no
        else if (receivedRequest[0] == 'g') {            
            for (int i = 0; i < 32; i++) {                
                if (i < 16) {
                    if (nameIsSet == true) {
                        mem[i] = deviceData[i];
                        }
                    else {
                        mem[i] = ' ';

                        }
                    serialIsSet = true;                        
                    }
                else {
                    if (i < (strlen(receivedRequest) + 15)) {
                        mem[i] = receivedRequest[i-15];
                    }
                else {
                    mem[i] = ' ';
                        }
                    }
                }
            }
        
        // write empty addresses into remaining ones
        for ( int i = 32; i < MEM_SIZE; i++ ) {
            mem[i] = i & 0xFF;
        }
        
        deleteFlashMemory();

        // special IAP functions written to write from RAM to flash 
        iap.prepare( TARGET_SECTOR, TARGET_SECTOR );
        r = iap.write( mem, sector_start_adress[ TARGET_SECTOR ], MEM_SIZE );
        // get newly written data
        getFlashMemory(sector_start_adress[ TARGET_SECTOR ], 32);
        
        // return answer, light LED
        pc.printf("f\n");
        lcd.printf("Data written successfully");
        LED(true, false);
}

// function to delete flash memory
void deleteFlashMemory()
{
    int r;
        r   = iap.blank_check( TARGET_SECTOR, TARGET_SECTOR );
        if ( r == SECTOR_NOT_BLANK ) {  
            iap.prepare( TARGET_SECTOR, TARGET_SECTOR );
            r = iap.erase( TARGET_SECTOR, TARGET_SECTOR );
        }
}

// function to clear screen on the device
void clearScreen()
{
    lcd.cls();
    lcd.locate(0,3);    
}

// function reads user input button
void readButton()
{
    if (inputButton) {
        lcd.printf("Button is pressed");
        pc.printf("b1\n");   
        }
    else {
        lcd.printf("Button is not pressed");
        pc.printf("b2\n");    
        }
    LED(true, false);      
}

// function checks if there is something in the flash memory, if so, returns it 
void readFlashMemory()
{
    if ((nameIsSet == false) && (serialIsSet == false)) {
        lcd.printf("Device does not have name nor serial number");
        pc.printf("c\n");
        LED(false, true);
        }
    else {
        getFlashMemory(sector_start_adress[ TARGET_SECTOR ], 32);
        lcd.printf("Name  and  serial  number:  %s", deviceData);
        pc.printf("%s\n", deviceData);
        LED(true, false);
        }     

}

// function to get time
void getTime(time_t seconds)
{
    strftime(buffer, 32, "%Y-%m-%d %H:%M:%S\n", localtime(&seconds));
    if (seconds == -1) {
        lcd.printf("Device time has not been set yet");
        pc.printf("d-1\n");
        LED(false, true);
        }
    else {
        lcd.printf("%s", buffer);
        pc.printf("d%d\n", seconds);
        LED(true, false);           
        } 
}

// function to set time
void setTime()
{
    for (int i = 1; i < sizeof(receivedRequest) + 1; i++) {
        buffer[i-1] = receivedRequest[i];
        }
    
    // convert request string to long int
    timeRTC = strtol(buffer, &trash, 10);
    
    // set RTC time
    set_time(timeRTC);
            
    lcd.printf("New time set successfully");
    pc.printf("e\n");
    LED(true, false);
}