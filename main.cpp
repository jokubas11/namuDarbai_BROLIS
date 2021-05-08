#include "mbed.h"
#include "LM75B.h"
#include "C12832.h"
#include "IAP.h"

#define     MEM_SIZE        256
#define     TARGET_SECTOR    24

void gautiFlashAtminti( char *p, int n );
void gautiTemperatura();
void lempute(bool zaliaLemp, bool raudonaLemp);
void irasomiDuomenys();
void trintiAtminti();
void isvalytiEkrana();
void skaitytiMygtuka();
void skaitytiDuomenis();
void skaitytiLaika(time_t seconds);
void nustatytiLaika();

Serial pc(USBTX, USBRX);
C12832 lcd(p5, p7, p6, p8, p11);
LM75B sensor(p28,p27);
PwmOut raudona (p23);
PwmOut zalia (p24);
DigitalIn mygtukas(p14);
IAP iap;

float temperaturosMatavimas = 0.0;
/////////////////
char atsakymasIUzklausa[18]; // 0 = simbolis, 1-16 - informacija, 17 = \n
char gautaUzklausa[18]; // 0 = simbolis, 1-16 informacija, 17 = \n
char buffer[32]; // bufferis laikyti dalykams;
char prietaisoDuomenys[33]; // 0-15 vardas, 16-31 serijinis numeris, 32 = \n
/////////////////
long int laikas;
char *siuksles; // viena naudojama funkcija reikalauja pointerio, nors man jo nereikia
/////////////////
bool vardasNustatytas = false;
bool serNrNustatytas = false;

int main()
{
        
    raudona = 1.0;  
    zalia = 1.0;

    // Paziureti ar flash atmintyje yra prietaiso vardas ir serijinis numeris
    // Jei taip, ikelti juos i prietaisoDuomenys
    
    gautiFlashAtminti(sector_start_adress[ TARGET_SECTOR ], 32);
    if ((strlen(prietaisoDuomenys) > 16) && (prietaisoDuomenys[0] != ' ')) {
        vardasNustatytas = true;
        serNrNustatytas = true;
        }
    else if ((strlen(prietaisoDuomenys) < 16) && (prietaisoDuomenys[0] != ' ')) {
        vardasNustatytas = true;
        serNrNustatytas = false;
        }
    else if ((strlen(prietaisoDuomenys) > 16) && (prietaisoDuomenys[0] == '\n')) {
        vardasNustatytas = false;
        serNrNustatytas = true;
        }
    else {
        // palikti nenustatyta
        }        

    // mbedas visada laukia komandos    
    while(1) {
            
        pc.scanf("%s", gautaUzklausa);
        
        // laiko skaiciavimas 
        time_t seconds = time(NULL);

        // gavus komanda isvalyti viska, kas buvo pries tai
        isvalytiEkrana();

        // pagal tai kokia uzklausos pirma raide, eiti i atitinkama funkcija
        if (gautaUzklausa[0] == 'a') {
            gautiTemperatura();            
        }
        if (gautaUzklausa[0] == 'b') {
            skaitytiMygtuka();
        }
        if (gautaUzklausa[0] == 'c') { 
            skaitytiDuomenis();
        }
        
        if (gautaUzklausa[0] == 'd') {
            skaitytiLaika(seconds);
        }
        
        if (gautaUzklausa[0] == 'e') {             
            nustatytiLaika();            
        }
        
        if (gautaUzklausa[0] == 'f' || gautaUzklausa[0] == 'g') {
            irasomiDuomenys();            
        }
        
        if (gautaUzklausa[0] == 'h') {
            trintiAtminti();
            vardasNustatytas = false;
            serNrNustatytas = false;
            pc.printf("h\n");
            lempute(true, false);
        }
        else {
            // jeigu neatpazystama uzklausa, grazinti "x\n"
            pc.printf("x\n");
        }

        // nusiuntus atsakyma istrinti viska, del visa ko
        memset(gautaUzklausa,0,sizeof(gautaUzklausa));
        memset(atsakymasIUzklausa,0,sizeof(atsakymasIUzklausa));
        memset(buffer,0,sizeof(buffer));
    }
    
}

#include    <ctype.h>

// funkcija skaito duomenis is flash atminties
// daugiau: https://os.mbed.com/users/okano/code/IAP_internal_flash_write//file/382f38b15c22/main.cpp/

void gautiFlashAtminti( char *base, int n )
{
    unsigned int    *p;
    char            s[17]   = { '\x0' };
    int k = 0;

    // paima hexadecimal reiksmes is atminties ir raso jas i prietaisoDuomenys
    // vyksta daug vertimo is vieno duomenu tipo i kita
    p   = (unsigned int *)((unsigned int)base & ~(unsigned int)0x3);
 
    for ( int i = 0; i < (n >> 2); i++, p++ ) {
        if (!(i % 4)) { 
            for (int j = 0; j < 16; j++) {
                s[j]  = isgraph((int)(*((char *)p + j))) ? (*((char *)p + j)) : ' ';
                prietaisoDuomenys[k] = s[j];
                k++;
            }
        }
    }   
}

// funkcija skaito temperatura is sensoriaus
void gautiTemperatura()
{   
    char stringTemp[9];
    if (sensor.open()) {    
        
        // gauna temperaturos reiskme
        temperaturosMatavimas = sensor.temp();

        // pavercia temperatura i stringa, nes grazinti reikia stringa      
        sprintf(stringTemp, "%.3f\n", temperaturosMatavimas);
        
        // rasomas atsakymasIUzklausa
        atsakymasIUzklausa[0] = 'a';        
        int i = 1;
        while(stringTemp[i] != '\n') {
            atsakymasIUzklausa[i] = stringTemp[i-1];
            i++;
        }
        atsakymasIUzklausa[i] = '\n';

        // grazinamas atsakymas python programai
        pc.printf("%s", atsakymasIUzklausa);

        // spausdinti ant ekrano prietaise ir pasviesti ijungti lempute
        lcd.printf("Temperatura: %s", stringTemp);
        lempute(true, false);

    } 
    
    else {
        
        // jeigu bloga uzklausa, pasviesti raudona lempute, grazinti klaida
        atsakymasIUzklausa[0] = 'a';
        atsakymasIUzklausa[1] = '\n';
        pc.printf("%s", atsakymasIUzklausa);
        lcd.printf("Klaida matuojant temperatura!");
        lempute(false, true);
    }
}

// fukcija lemputei pasviesti
// funkcija ima du argumentus, priklausomai nuo to, kokios lemputes reikia
// pirmas argumentas zalia lempute, antras argumentas raudona
// jeigu reikia zalios lemputes, siusti zaliaLemp = true
// pavyzdziui: lempute(true, false) zaliai lemputei
//             lempute(false, true) raudonai lemputei
void lempute(bool zaliaLemp, bool raudonaLemp)
{
    PwmOut *lemputesAdresas;
    
    // jeigu norime zalios lemputes, nustatyti pointeri i zalia lempute
    // jeigu norime raudonos, nustatyti pointeri i raudona lempute
    if (zaliaLemp == true && raudonaLemp == false) {
        lemputesAdresas = &zalia;
        }
    else if (zaliaLemp == false && raudonaLemp == true) {
        lemputesAdresas = &raudona;
        }
    else {
        lempute(false, true);
        }
    
    // pamirkseti lempute
    for (int i = 0; i < 5; i++) {
        *lemputesAdresas = 0.0;
        wait(0.05);
        *lemputesAdresas = 1.0;
        wait(0.05);
        }
}

// funkcija raso turimus prietaisoDuomenys i flash atminti
// mbed leidzia rasyti atminti tik sektoriais 256, 512, 1024, 2048
// tad net jei ir norime rasyti tik 32 simbolius, reikia uzpildyti visus 256 siuo atveju

void irasomiDuomenys() {
        char    mem[ MEM_SIZE ]; // sis array bus rasomas i flash atminti
        int     r; // r yra reikalingas norint naudoti kaikurias mbed rasymo i atminti funckijas   
        
        // jeigu praso rasyti varda, rasyti varda i mem
        // visa kita uzpildyti tarpais, po mem[32] uzpildyti tusciais adresais
        // patikrina ar duomenys jau buvo pries tai irasyti
        // kadangi rasymas perrasys senus duomenis, reikia issisaugoti tai kas buvo irasyta pries tai

        if (gautaUzklausa[0] == 'f') {            
            for (int i = 0; i < 32; i++) {                
                if (i < 16) {                    
                    if (i < (strlen(gautaUzklausa)-1)) {                        
                        mem[i] = gautaUzklausa[i+1];                           
                        }
                    else {                        
                        mem[i] = ' ';                        
                        }
                    }                
                else {                    
                    if (serNrNustatytas == true) {                        
                        mem[i] = prietaisoDuomenys[i];                        
                        }
                    else {
                        mem[i] = ' ';
                        }
                    vardasNustatytas = true;
                    }
                }
            }
        // jeigu praso rasyti serijini nr, naudoti sita dali
        else if (gautaUzklausa[0] == 'g') {            
            for (int i = 0; i < 32; i++) {                
                if (i < 16) {
                    if (vardasNustatytas == true) {
                        mem[i] = prietaisoDuomenys[i];
                        }
                    else {
                        mem[i] = ' ';

                        }
                    serNrNustatytas = true;                        
                    }
                else {
                    if (i < (strlen(gautaUzklausa) + 15)) {
                        mem[i] = gautaUzklausa[i-15];
                    }
                else {
                    mem[i] = ' ';
                        }
                    }
                }
            }
        
        // rasyti tuscius adresus i likusia mem dali
        for ( int i = 32; i < MEM_SIZE; i++ ) {
            mem[ i ]    = i & 0xFF;
        }
        
        // trinti atminti, kad irasyti naujus duomenis
        trintiAtminti();

        // specialios IAP funkcijos skirtos rasymui is RAM i flash atminti        
        iap.prepare( TARGET_SECTOR, TARGET_SECTOR );
        r = iap.write( mem, sector_start_adress[ TARGET_SECTOR ], MEM_SIZE );
        // gauti naujai irasytus duomenis
        gautiFlashAtminti(sector_start_adress[ TARGET_SECTOR ], 32);
        
        // grazinti atsakyma ir pasviesti lempute
        pc.printf("f\n");
        lcd.printf("Duomenys nustatyti sekmingai");
        lempute(true, false);
}

// funkcija trina flash atminti
void trintiAtminti()
{
    int r;
        r   = iap.blank_check( TARGET_SECTOR, TARGET_SECTOR );
        if ( r == SECTOR_NOT_BLANK ) {  
            iap.prepare( TARGET_SECTOR, TARGET_SECTOR );
            r = iap.erase( TARGET_SECTOR, TARGET_SECTOR );
        }
}

// funkcija isvalo ekrana
void isvalytiEkrana()
{
    lcd.cls();
    lcd.locate(0,3);    
}

// funkcija skaito user-input mygtuka
void skaitytiMygtuka()
{
    // jeigu mygtukas nuspaustas grazina toki atsakyma
    if (mygtukas) {
        lcd.printf("Mygtukas paspaustas");
        pc.printf("b1\n");   
        }
    // jeigu nenuspasutas - toki
    else {
        lcd.printf("Mygtukas nepaspaustas");
        pc.printf("b2\n");    
        }
    lempute(true, false);      
}

// patikrinti ar flash atmintyje yra duomenu, jeigu taip - skaityti juos
void skaitytiDuomenis()
{
    if ((vardasNustatytas == false) && (serNrNustatytas == false)) {
        lcd.printf("Prietaisas neturi vardo ir serijinio numerio");
        pc.printf("c\n");
        lempute(false, true);
        }
    else {
        gautiFlashAtminti(sector_start_adress[ TARGET_SECTOR ], 32);
        lcd.printf("Vardas  ir serijinis  numeris: %s", prietaisoDuomenys);
        pc.printf("%s\n", prietaisoDuomenys);
        lempute(true, false);
        }     

}

// funckija skirta nuskaityti laika is mbed
void skaitytiLaika(time_t seconds)
{
    strftime(buffer, 32, "%Y-%m-%d %H:%M:%S\n", localtime(&seconds));
    if (seconds == -1) {
        lcd.printf("Prietaiso laikas nenustatytas");
        pc.printf("d-1\n");
        lempute(false, true);
        }
    else {
        lcd.printf("%s", buffer);
        pc.printf("d%d\n", seconds);
        lempute(true, false);           
        } 
}

// funkcija skirta nustatyti laika
void nustatytiLaika()
{
    for (int i = 1; i < sizeof(gautaUzklausa) + 1; i++) {
        buffer[i-1] = gautaUzklausa[i];
        }
    
    // paversti gauta uzklausos stringa i long int
    laikas = strtol(buffer, &siuksles, 10);
    
    // nustatyti rtc laika
    set_time(laikas);
            
    lcd.printf("Naujas laikas nustatytas sekmingai");
    pc.printf("e\n");
    lempute(true, false);
}