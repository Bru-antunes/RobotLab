#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include <stdbool.h>

#include "robot_config.h"

// Interface com Mid Level
extern volatile bool target_detected;

// ============================
// Inicialização
// ============================

static void run_init(void)
{
    #if INIT_STRATEGY == 1
        // Estratégia 1

    #elif INIT_STRATEGY == 2
        // Estratégia 2

    #elif INIT_STRATEGY == 3
        // Estratégia 3
        vTaskDelay(pdMS_TO_TICKS(1000));

    #elif INIT_STRATEGY == 4
        // Estratégia 4

    #elif INIT_STRATEGY == 5
        // Estratégia 5

    #else
        // fallback (nenhuma válida)
    #endif
}

// ============================
// Navegação
// ============================

static void run_navigation(void)
{
    #if NAV_STRATEGY == 1
        // Estratégia NAV 1

    #elif NAV_STRATEGY == 2
        // Estratégia NAV 2

    #elif NAV_STRATEGY == 3
        // Estratégia NAV 3

    #else
        // fallback
    #endif
}

// ============================
// Missão
// ============================

static void run_mission(void)
{
    #if MISSION_STRATEGY == 1
        // Estratégia MISSÃO 1

    #elif MISSION_STRATEGY == 2
        // Estratégia MISSÃO 2

    #else
        // fallback
    #endif
}

// ============================
// Task High Level
// ============================

void task_high_level(void *pvParameters)
{
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
