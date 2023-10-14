#include <looney_game.h>

int main(int argc, char *argv[]) {
    int ret = -1;
    game_board *game = NULL;
    
    game = (game_board*)malloc(sizeof(game_board));
    if (NULL == game) {
        fprintf(stderr, "Error: Out of memory\n");
        exit(-1);
    }

    game->characters = (character*)malloc(sizeof(character) * 4);
    if (NULL == game->characters) {
        fprintf(stderr, "Error: Out of memory\n");
        exit(-1);
    }

    for (int i = 0; i < character_count; i++) {
        ret = pthread_create(&(game->characters)[i], NULL, game_loop, (void*)(intptr_t)i);

        if (0 != ret) {
            fprintf(stderr, "Error: issue creating thread\n");
            exit(-1);
        }
    }

    while(game_loop_flag) {

    }

    //join threads

    return 0;
}

void move_random_loc(grid_loc *loc) {
    loc->x = rand() % 5;
    loc->y = rand() % 5;
    return;
}

void *game_loop(void *threadid) {

    while (game_loop_flag) {

    }

}