/*
    ISPPJ1 2023
    Study Case: Pong

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the functions to init a pong game,
    update it, and render it.
*/

#include <stdio.h>
#include <math.h>

#include <allegro5/allegro_primitives.h>

#include "settings.h"
#include "fonts.h"
#include "pong.h"

void init_pong(struct Pong *pong, struct Sounds *sounds, bool player1_use_ia, bool player2_use_ia)
{
    init_paddle(&pong->player1, PADDLE_X_OFFSET, PADDLE_Y_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT, player1_use_ia);
    init_paddle(&pong->player2, TABLE_WIDTH - PADDLE_WIDTH - PADDLE_X_OFFSET, TABLE_HEIGHT - PADDLE_HEIGHT - PADDLE_Y_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT, player2_use_ia);
    init_ball(&pong->ball, TABLE_WIDTH / 2 - BALL_SIZE / 2, TABLE_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE);
    pong->state = START;
    pong->player1_score = 0;
    pong->player2_score = 0;
    pong->serving_player = 0;
    pong->winning_player = 0;
    pong->sounds = sounds;
    srand(time(NULL));
}

void handle_input_pong(struct Pong* pong, ALLEGRO_KEYBOARD_STATE* state)
{
    if (pong->state == START)
    {
        if (al_key_down(state, ALLEGRO_KEY_ENTER))
        {
            pong->state = SERVE;
            pong->serving_player = rand() % 2 + 1;
        }
    }
    else if (pong->state == SERVE)
    {
        if (al_key_down(state, ALLEGRO_KEY_ENTER))
        {
            pong->state = PLAY;

            pong->ball.vx = rand() % 60 + 140;

            if (pong->serving_player == 2)
            {
                pong->ball.vx *= -1;
            }

            pong->ball.vy = rand() % 100 - 50;
        }
    }
    else if (pong->state == PLAY)
    {
        if (!pong->player1.is_ai_driven)
        {
            if (al_key_down(state, ALLEGRO_KEY_S))
            {
                pong->player1.vy = PADDLE_SPEED;
            }
            else if (al_key_down(state, ALLEGRO_KEY_W))
            {
                pong->player1.vy = -PADDLE_SPEED;
            }
            else
            {
                pong->player1.vy = 0;
            }
        }

        if (!pong->player2.is_ai_driven)
        {
            if (al_key_down(state, ALLEGRO_KEY_DOWN))
            {
                pong->player2.vy = PADDLE_SPEED;
            }
            else if (al_key_down(state, ALLEGRO_KEY_UP))
            {
                pong->player2.vy = -PADDLE_SPEED;
            }
            else
            {
                pong->player2.vy = 0;
            }
        }
    }
    else
    {
        if (al_key_down(state, ALLEGRO_KEY_ENTER))
        {
            pong->state = SERVE;
            init_ball(&pong->ball, TABLE_WIDTH / 2 - BALL_SIZE / 2, TABLE_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE);

            pong->player1_score = 0;
            pong->player2_score = 0;

            if (pong->winning_player == 1)
            {
                pong->serving_player = 2;
            }
            else
            {
                pong->serving_player = 1;
            }
        }
    }
}

void update_pong(struct Pong* pong, double dt)
{
    if (pong->state == PLAY)
    {
        update_paddle(&pong->player1, dt);
        update_paddle(&pong->player2, dt);
        update_ball(&pong->ball, dt);

        struct Hitbox ball_hitbox;
        build_ball_hitbox(pong->ball, &ball_hitbox);

        struct Hitbox player1_hitbox;
        build_paddle_hitbox(pong->player1, &player1_hitbox);

        struct Hitbox player2_hitbox;
        build_paddle_hitbox(pong->player2, &player2_hitbox);

        if (ball_hitbox.x1 > TABLE_WIDTH)
        {
            al_play_sample(pong->sounds->score, /* gain */ 1.0, /* center */ 1.0, /* speed */ 1.0, ALLEGRO_PLAYMODE_ONCE, NULL);
            ++pong->player1_score;
            pong->serving_player = 2;

            if (pong->player1_score == MAX_POINTS)
            {
                pong->winning_player = 1;
                pong->state = DONE;
            }
            else
            {
                pong->state = SERVE;
                init_ball(&pong->ball, TABLE_WIDTH / 2 - BALL_SIZE / 2, TABLE_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE);
            }
        }
        else if (ball_hitbox.x2 < 0)
        {
            al_play_sample(pong->sounds->score, /* gain */ 1.0, /* center */ -1.0, /* speed */ 1.0, ALLEGRO_PLAYMODE_ONCE, NULL);
            ++pong->player2_score;
            pong->serving_player = 1;

            if (pong->player2_score == MAX_POINTS)
            {
                pong->winning_player = 2;
                pong->state = DONE;
            }
            else
            {
                pong->state = SERVE;
                init_ball(&pong->ball, TABLE_WIDTH / 2 - BALL_SIZE / 2, TABLE_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE);
            }
        }

        if (ball_hitbox.y1 <= 0)
        {
            al_play_sample(pong->sounds->wall_hit, /* gain */ 1.0, /* center */ 0.0, /* speed */ 1.0, ALLEGRO_PLAYMODE_ONCE, NULL);
            pong->ball.y = 0;
            pong->ball.vy *= -1;
        }
        else if (ball_hitbox.y2 >= TABLE_HEIGHT)
        {
            al_play_sample(pong->sounds->wall_hit, /* gain */ 1.0, /* center */ 0.0, /* speed */ 1.0, ALLEGRO_PLAYMODE_ONCE, NULL);
            pong->ball.y = TABLE_HEIGHT - pong->ball.height;
            pong->ball.vy *= -1;
        }
        
        if (collides(ball_hitbox, player1_hitbox))
        {
            al_play_sample(pong->sounds->paddle_hit, /* gain */ 1.0, /* center */ -1.0, /* speed */ 1.0, ALLEGRO_PLAYMODE_ONCE, NULL);
            pong->ball.x = player1_hitbox.x2;
            pong->ball.vx *= -1.03;

            if (pong->ball.vy < 0)
            {
                pong->ball.vy = -(rand() % 140 + 10);
            }
            else
            {
                pong->ball.vy = rand() % 140 + 10;
            }
        }
        else if (collides(ball_hitbox, player2_hitbox))
        {
            al_play_sample(pong->sounds->paddle_hit, /* gain */ 1.0, /* center */ 1.0, /* speed */ 1.0, ALLEGRO_PLAYMODE_ONCE, NULL);
            pong->ball.x = player2_hitbox.x1 - pong->ball.width;
            pong->ball.vx *= -1.03;

            if (pong->ball.vy < 0)
            {
                pong->ball.vy = -(rand() % 140 + 10);
            }
            else
            {
                pong->ball.vy = rand() % 140 + 10;
            }
        }

        if (pong->player1.is_ai_driven)
        {
            update_pong_paddle_ia(&pong->player1, &ball_hitbox, &pong->ball, dt);
        }

        if (pong->player2.is_ai_driven)
        {
            update_pong_paddle_ia(&pong->player2, &ball_hitbox, &pong->ball, dt);
        }
    }
}

void render_pong(struct Pong* pong, struct Fonts* fonts)
{
    al_draw_filled_rectangle(
        TABLE_WIDTH / 2 - MID_LINE_WIDTH / 2, 0,
        TABLE_WIDTH / 2 + MID_LINE_WIDTH / 2, TABLE_HEIGHT,
        al_map_rgb(255, 255, 255));
    render_paddle(pong->player1);
    render_paddle(pong->player2);
    render_ball(pong->ball);

    char score[3];
    sprintf(score, "%d", pong->player1_score);
    al_draw_text(fonts->score_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2 - 50, TABLE_HEIGHT / 6, ALLEGRO_ALIGN_CENTER, score);
    sprintf(score, "%d", pong->player2_score);
    al_draw_text(fonts->score_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2 + 50, TABLE_HEIGHT / 6, ALLEGRO_ALIGN_CENTER, score);

    if (pong->state == START)
    {
        al_draw_text(fonts->large_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2, TABLE_HEIGHT / 2, ALLEGRO_ALIGN_CENTER, "Press enter to start");
    }
    else if (pong->state == SERVE)
    {
        al_draw_text(fonts->large_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2, TABLE_HEIGHT / 2, ALLEGRO_ALIGN_CENTER, "Press enter to serve");
    }
    else if (pong->state == DONE)
    {
        char winner_message[14];
        sprintf(winner_message, "Player %d won!", pong->winning_player);
        al_draw_text(fonts->large_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2, TABLE_HEIGHT / 3, ALLEGRO_ALIGN_CENTER, winner_message);
        al_draw_text(fonts->large_font, al_map_rgb(255, 255, 255), TABLE_WIDTH / 2, TABLE_HEIGHT / 2, ALLEGRO_ALIGN_CENTER, "Press enter to restart");
    }
}

int BALL_DIR_LEFT = -1;
int BALL_DIR_RIGHT = 1;

void update_pong_paddle_ia(struct Paddle *paddle, struct Hitbox *ball_hitbox, struct Ball *ball, float dt)
{
    // If ball is getting away, simply follow it
    if (fabsf(ball->x + ball->vx * dt - paddle->x) > fabsf(ball->x - paddle->x))
    {
        if (ball_hitbox->y2 < paddle->y + paddle->height / 2)
        {
            paddle->vy = -PADDLE_SPEED;
        }
        else if (ball_hitbox->y1 > paddle->y + paddle->height / 2)
        {
            paddle->vy = PADDLE_SPEED;
        }
        else
        {
            paddle->vy = 0;
        }
    }
    else // When it's getting closer, estimate it's position
    {

        int ball_dir = ball->vx / fabsf(ball->vx); // 1 -> right / -1 -> left

        float hit_x = paddle->x;
        // the ball will hit on the paddle right side
        if (ball_dir == BALL_DIR_LEFT)
        {
            hit_x += paddle->width;
        }
        // The ball will hit on the paddle left side
        if (ball_dir == BALL_DIR_RIGHT)
        {
            hit_x -= ball->width;
        }

        float ax = fabsf(hit_x - ball->x);

        float estimated_y = ball->y + fabsf(ax / ball->vx) * ball->vy;

        if (estimated_y + ball->height < paddle->y + paddle->height / 2)
        {
            paddle->vy = -PADDLE_SPEED;
        }
        else if (estimated_y > paddle->y + paddle->height / 2)
        {
            paddle->vy = PADDLE_SPEED;
        }
        else
        {
            paddle->vy = 0;
        }
    }
}
