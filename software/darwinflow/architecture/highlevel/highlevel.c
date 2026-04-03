#include "high_level.h"

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include <stdbool.h>

#include "robot_config.h"

// ============================
// Interface com Mid Level
// ============================
extern volatile bool target_detected;

// ============================
// Inicialização
// ============================

static void run_init(void)
{
    switch (INIT_STRATEGY)
    {
        case 1:
            // Estratégia 1
            break;

        case 2:
            // Estratégia 2
            break;

        case 3:
            // Estratégia 3
            vTaskDelay(pdMS_TO_TICKS(1000));
            break;

        case 4:
            // Estratégia 4
            break;

        case 5:
            // Estratégia 5
            break;

        default:
            // fallback
            break;
    }
}

// ============================
// Navegação
// ============================

static void run_navigation(void)
{
    switch (NAV_STRATEGY)
    {
        case 1:
            // NAV 1: girar procurando alvo
            break;

        case 2:
            // NAV 2: zigue-zague
            break;

        case 3:
            // NAV 3
            break;

        default:
            // fallback
            break;
    }
}

// ============================
// Missão
// ============================

static void run_mission(void)
{
    switch (MISSION_STRATEGY)
    {
        case 1:
            // MISSÃO 1: ataque direto
            break;

        case 2:
            // MISSÃO 2: ataque controlado
            break;

        default:
            // fallback
            break;
    }
}

// ============================
// Task High Level
// ============================

void task_high_level(void *pvParameters)
{
    // Inicialização (executa uma vez)
    run_init();

    while (1)
    {
        if (target_detected)
        {
            run_mission();
        }
        else
        {
            run_navigation();
        }

        vTaskDelay(pdMS_TO_TICKS(10));
    }
}
