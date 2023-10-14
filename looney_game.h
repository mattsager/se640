
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <time.h>

#include <unistd.h>
#include <errno.h>

#define TRUE 1
#define FALSE 0

const int character_count = 4;
int game_loop_flag = TRUE;

struct grid_loc {
    int x;
    int y;
};

typedef struct grid_loc grid_loc;

struct character {
    char *sprite;
    int x;
    int y;
    int has_carrot;
    pthread_t *thread;
};
typedef struct character character;

struct game_board {
    int row_count;
    int col_count;
    grid_loc mountain;
    grid_loc carrot1;
    grid_loc carrot2;
    character **characters;
};
typedef struct game_board game_board;