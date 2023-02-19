"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp to attach a pair of cannons to the paddle.
"""
from typing import TypeVar
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp
import pygame
import settings


class Cannons(PowerUp):
    """
    Power-up to attach a pair of cannons to the paddle.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 7)

        self.taken = False
        self.shots = 2

        self.cannons_y = 0
        self.cannon_a_x = 0
        self.cannon_b_x = 0

    def update(self, dt: float, play_state: TypeVar("PlayState")) -> None:
        # If the powerup has not been taken, update as usual
        if not self.taken:
            super().update(dt, play_state)
        else:
            paddle = play_state.paddle

            self.cannons_y = paddle.y

            self.cannon_a_x = paddle.x
            self.cannon_b_x = paddle.x + paddle.width - 16

    def handle_input(self, input_id: str, play_state: TypeVar("PlayState")) -> None:
        if input_id == "fire":
            if self.in_play and self.shots > 0:
                self.shots = self.shots - 1
                self.fire()

    def fire(slef):
        pass

    def render(self, surface: pygame.Surface) -> None:
        if not self.taken:
            super().render(surface)
        else:
            surface.blit(
                settings.TEXTURES["spritesheet"],
                (self.cannon_a_x, self.cannons_y),
                settings.FRAMES["powerups"][0],
            )

            surface.blit(
                settings.TEXTURES["spritesheet"],
                (self.cannon_b_x, self.cannons_y),
                settings.FRAMES["powerups"][1],
            )

    def take(self, play_state: TypeVar("PlayState")) -> None:
        self.taken = True
