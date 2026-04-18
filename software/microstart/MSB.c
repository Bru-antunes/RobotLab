#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdio.h>

void f_acao (void);
void f_decode (void);
void f_start (void);
void f_eventos (void);
unsigned int f_diferenca (unsigned int atual, unsigned int anterior);

// Variáveis globais
volatile uint16_t bit_duration = 0;
volatile uint8_t current_bit = 0;
volatile uint16_t ir_signal = 0;
volatile uint8_t decoded_command = 0;
volatile uint16_t pulse_duration = 0;
volatile uint8_t Flag_1 = 0;
volatile uint8_t Flag_2 = 0;
volatile uint8_t Flag_start = 0;
volatile uint16_t contador = 0;
volatile uint16_t last_counter = 0;
volatile uint16_t periodo = 0;
volatile uint8_t fl_ev0 = 0;
volatile uint8_t fl_ev1 = 0;

volatile uint8_t last_state = 1;
volatile uint8_t current_state = 1;

volatile uint16_t incrementador = 0;

// ================= TIMER =================
ISR(TIM0_COMPA_vect) {
    incrementador++;
    // if (incrementador >= 65535) {incrementador = 0;}
}

// ================= INTERRUPÇÃO IR =================
ISR(PCINT0_vect) {

    current_state = (PINB & (1 << PB4)) ? 1 : 0;


    if (current_state != last_state) {

        contador = incrementador;
        periodo = f_diferenca(contador, last_counter);
        last_counter = contador;


        if (current_state == 1) {
            fl_ev1 = 1;
        }

        last_state = current_state;
    }
}

// ================= SETUP =================
void setup(void) {
    DDRB |= (1 << PB0);
    DDRB |= (1 << PB1);
    DDRB |= (1 << PB2);
    PORTB &= ~(1 << PB2);

    TCCR0A = (1 << WGM01);
    TCCR0B = (1 << CS00);
    OCR0A = 153;
    TIMSK0 |= (1 << OCIE0A);

    DDRB &= ~(1 << PB4);

    GIMSK |= (1 << PCIE);
    PCMSK |= (1 << PCINT4);

    sei();
}

// ================= MAIN =================
int main(void) {
    setup();

    while (1) {
        f_eventos();
    }
    return 0;
}

// ================= AÇÃO =================
void f_acao (void){
    switch (decoded_command) {
        case 0x80:
            PORTB ^= (1 << PB1);
            Flag_1 = 1;
            PORTB &= ~(1 << PB2);
            break;

        case 0x81:
            if (Flag_1){
                PORTB |= (1 << PB2);
                Flag_2 = 1;
                PORTB |= (1 << PB0);
                PORTB &= ~(1 << PB1);
            }
            break;

        case 0x82:
            if (Flag_2){
                PORTB &= ~(1 << PB2);
                PORTB &= ~(1 << PB0);
                Flag_1 = 0;
                Flag_2 = 0;
            }
            break;

        default:
            break;
    }
}

// ================= START =================
void f_start (void){


    if ((periodo > 120) && (periodo < 150)) {  // ~2.4ms

        current_bit = 0;
        ir_signal = 0;
        Flag_start = 1;
    }
}

// ================= DECODE =================
void f_decode (void){


    if (!Flag_start) return;

    if ((periodo > 55) && (periodo < 90)) {
        ir_signal |= (1 << current_bit);  // bit 1
    } else if ((periodo < 50) && (periodo > 20)) {
        ir_signal &= ~(1 << current_bit); // bit 0
    }

    current_bit++;

    if (current_bit >= 12) {
        decoded_command = ir_signal;
        ir_signal = 0;
        current_bit = 0;
        Flag_start = 0;
        fl_ev0 = 1;
    }
}

// ================= CONTADOR =================
void f_contador (void){
    contador = incrementador;
    periodo = f_diferenca(contador, last_counter);
}

unsigned int f_diferenca (unsigned int atual, unsigned int anterior) {
    if (atual > anterior) return atual - anterior;
    else return anterior - atual;
}

// ================= EVENTOS =================
void f_eventos (void){

    if (fl_ev0){
        f_acao();
        fl_ev0 = 0;
    }

    if (fl_ev1){


        if (periodo > 120){
            f_start();
        } else {
            f_decode();
        }

        fl_ev1 = 0;
    }
}
