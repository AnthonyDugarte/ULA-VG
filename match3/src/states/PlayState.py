"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class PlayState.
"""
from typing import Dict, Any, List

import pygame

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text
from gale.timer import Timer

from src.states.state_utils import get_virtual_position
import settings


class PlayState(BaseState):
    def enter(self, **enter_params: Any) -> None:
        self.level = enter_params["level"]
        self.board = enter_params["board"]
        self.score = enter_params["score"]

        # Position in the grid which we are highlighting
        self.board_highlight_i1 = -1
        self.board_highlight_j1 = -1
        self.board_highlight_i2 = -1
        self.board_highlight_j2 = -1

        self.dragged_tile = False  # i1,j1
        self.highlighted_tile = False  # i2,j2

        self.active = True

        self.timer = settings.LEVEL_TIME

        self.goal_score = self.level * 1.25 * 1000

        # A surface that supports alpha to highlight a selected tile
        self.tile_alpha_surface = pygame.Surface(
            (settings.TILE_SIZE, settings.TILE_SIZE), pygame.SRCALPHA
        )
        pygame.draw.rect(
            self.tile_alpha_surface,
            (255, 255, 255, 96),
            pygame.Rect(0, 0, settings.TILE_SIZE, settings.TILE_SIZE),
            border_radius=7,
        )

        # A surface that supports alpha to draw behind the text.
        self.text_alpha_surface = pygame.Surface((212, 136), pygame.SRCALPHA)
        pygame.draw.rect(
            self.text_alpha_surface, (56, 56, 56, 234), pygame.Rect(0, 0, 212, 136)
        )

        def decrement_timer():
            self.timer -= 1

            # Play warning sound on timer if we get low
            if self.timer <= 5:
                settings.SOUNDS["clock"].play()

        Timer.every(1, decrement_timer)

        InputHandler.register_listener(self)

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, _: float) -> None:
        if self.timer <= 0:
            Timer.clear()
            settings.SOUNDS["game-over"].play()
            self.state_machine.change("game-over", score=self.score)

        if self.score >= self.goal_score:
            Timer.clear()
            settings.SOUNDS["next-level"].play()
            self.state_machine.change("begin", level=self.level + 1, score=self.score)

    def render(self, surface: pygame.Surface) -> None:
        self.board.render(surface)

        if self.highlighted_tile:
            x = self.highlighted_j2 * settings.TILE_SIZE + self.board.x
            y = self.highlighted_i2 * settings.TILE_SIZE + self.board.y
            surface.blit(self.tile_alpha_surface, (x, y))

        surface.blit(self.text_alpha_surface, (16, 16))
        render_text(
            surface,
            f"Level: {self.level}",
            settings.FONTS["medium"],
            30,
            24,
            (99, 155, 255),
            shadowed=True,
        )
        render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["medium"],
            30,
            52,
            (99, 155, 255),
            shadowed=True,
        )
        render_text(
            surface,
            f"Goal: {self.goal_score}",
            settings.FONTS["medium"],
            30,
            80,
            (99, 155, 255),
            shadowed=True,
        )
        render_text(
            surface,
            f"Timer: {self.timer}",
            settings.FONTS["medium"],
            30,
            108,
            (99, 155, 255),
            shadowed=True,
        )

    def swap_tiles(self, i1, j1, i2, j2):
        tile1 = self.board.tiles[i1][j1]
        tile2 = self.board.tiles[i2][j2]

        (
            self.board.tiles[tile1.i][tile1.j],
            self.board.tiles[tile2.i][tile2.j],
        ) = (
            self.board.tiles[tile2.i][tile2.j],
            self.board.tiles[tile1.i][tile1.j],
        )

        tile1.i, tile1.j, tile2.i, tile2.j = (
            tile2.i,
            tile2.j,
            tile1.i,
            tile1.j,
        )

        return tile1, tile2

    def mark_dragged_tile(self, i, j, dragged=True):
        self.dragged_tile = dragged
        self.highlighted_i1 = i
        self.highlighted_j1 = j

        tile = self.board.tiles[self.highlighted_i1][self.highlighted_j1]
        tile.dragged = dragged

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if not self.active:
            return

        if input_id == "click":
            pos_x, pos_y = get_virtual_position(input_data.position)

            i = (pos_y - self.board.y) // settings.TILE_SIZE
            j = (pos_x - self.board.x) // settings.TILE_SIZE

            if 0 <= i < settings.BOARD_HEIGHT and 0 <= j <= settings.BOARD_WIDTH:
                if input_data.pressed:
                    if self.dragged_tile:
                        # clean previus highlighted tile, is this really reached?
                        pass

                    self.mark_dragged_tile(i, j)
                elif self.dragged_tile:
                    self.highlighted_tile = True
                    self.highlighted_i2 = i
                    self.highlighted_j2 = j

                    di = abs(self.highlighted_i2 - self.highlighted_i1)
                    dj = abs(self.highlighted_j2 - self.highlighted_j1)

                    self.active = False
                    tile1 = self.board.tiles[self.highlighted_i1][self.highlighted_j1]
                    tile2 = self.board.tiles[self.highlighted_i2][self.highlighted_j2]

                    if di <= 1 and dj <= 1 and di != dj:

                        def arrive():
                            tile1, tile2 = self.swap_tiles(
                                self.highlighted_i1,
                                self.highlighted_j1,
                                self.highlighted_i2,
                                self.highlighted_j2,
                            )

                            if not self.__calculate_matches([tile1, tile2]):
                                self.swap_tiles(
                                    self.highlighted_i1,
                                    self.highlighted_j1,
                                    self.highlighted_i2,
                                    self.highlighted_j2,
                                )

                                Timer.tween(
                                    0.1,
                                    [
                                        (tile1, tile1.get_default_pos_timer_obj()),
                                        (tile2, tile2.get_default_pos_timer_obj()),
                                    ],
                                    on_finish=lambda: None,
                                )

                        Timer.tween(
                            0.25,
                            [
                                (tile1, tile2.get_default_pos_timer_obj()),
                                (tile2, tile1.get_default_pos_timer_obj()),
                            ],
                            on_finish=arrive,
                        )

                    else:
                        # clean previus highlighted tile

                        def finish():
                            self.active = True

                        Timer.tween(
                            0.2,
                            [
                                (
                                    tile1,
                                    {
                                        "x": tile1.j * settings.TILE_SIZE,
                                        "y": tile1.i * settings.TILE_SIZE,
                                    },
                                ),
                            ],
                            on_finish=finish,
                        )

                    self.mark_dragged_tile(
                        self.highlighted_i1, self.highlighted_j1, False
                    )
                    self.highlighted_tile = False

        if input_id in ["m_up", "m_down", "m_left", "m_right"]:
            pos_x, pos_y = get_virtual_position(input_data.position)

            i = (pos_y - self.board.y) // settings.TILE_SIZE
            j = (pos_x - self.board.x) // settings.TILE_SIZE

            if self.dragged_tile:
                if not input_data.buttons[0]:
                    self.mark_dragged_tile(
                        self.highlighted_i1, self.highlighted_j1, False
                    )
                else:
                    tile1 = self.board.tiles[self.highlighted_i1][self.highlighted_j1]

                    tile1.x = pos_x - self.board.x - settings.TILE_SIZE // 2
                    tile1.y = pos_y - self.board.y - settings.TILE_SIZE // 2

                    if (
                        0 <= i < settings.BOARD_HEIGHT
                        and 0 <= j <= settings.BOARD_WIDTH
                    ):
                        if i != self.highlighted_i1 or j != self.highlighted_j1:
                            self.highlighted_tile = True
                            self.highlighted_i2 = i
                            self.highlighted_j2 = j
                    else:
                        self.higihtlighted_tile = False

    def __calculate_matches(self, tiles: List) -> bool:
        matches = self.board.calculate_matches_for(tiles)

        if matches is None:
            self.active = True
            return False

        settings.SOUNDS["match"].stop()
        settings.SOUNDS["match"].play()

        for match in matches:
            self.score += len(match) * 50

        self.board.remove_matches()

        falling_tiles = self.board.get_falling_tiles()

        def finish():
            self.__calculate_matches([item[0] for item in falling_tiles])

        Timer.tween(
            0.25,
            falling_tiles,
            on_finish=finish,
        )

        return True
