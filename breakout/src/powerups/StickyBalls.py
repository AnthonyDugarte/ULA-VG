"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp to add two more ball to the game.
"""
from typing import TypeVar
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp
import pygame
import settings


class StickyBalls(PowerUp):
    """
    Power-up to stick the balls to the paddle.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 3)

        self.taken = False
        self.elapsed = 0

    def update(self, dt: float, play_state: TypeVar("PlayState")) -> None:
        # If the powerup has not been taken, update as usual
        if not self.taken:
            super().update(dt, play_state)
        else:
            # Store elapsed time
            self.elapsed += dt
            # Consider the paddle in play for as long as specified on settings
            self.in_play = self.elapsed <= settings.POWERUP_STICKY_BALL_LIFESPAM_SECONDS

            for ball in play_state.balls:
                if ball.sticked_to_paddle:
                    ball.x += play_state.paddle.update_dx

                if not self.in_play:
                    self.free_ball(ball)
                    continue

                if ball.paddled_in_update:
                    ball.sticked_to_paddle = True
                    ball.vx = 0
                    ball.vy = 0

    def free_ball(self, ball: Ball) -> None:
        if ball.sticked_to_paddle:
            ball.sticked_to_paddle = False
            ball.assign_rand_velocity()

    def handle_input(self, input_id: str, play_state: TypeVar("PlayState")) -> None:
        if input_id == "fire":
            for ball in play_state.balls:
                self.free_ball(ball)

    def render(self, surface: pygame.Surface) -> None:
        if not self.taken:
            super().render(surface)
        else:
            pass

    def take(self, play_state: TypeVar("PlayState")) -> None:
        self.taken = True
