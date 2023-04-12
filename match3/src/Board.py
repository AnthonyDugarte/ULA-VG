"""
ISPPJ1 2023
Study Case: Match-3

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Board.
"""
from typing import List, Optional, Tuple, Any, Dict, Set

import pygame

import random

import settings
from src.Tile import Tile
from gale import input_handler


class Board:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.matches: List[List[Tile]] = []
        self.tiles: List[List[Tile]] = []
        self.__initialize_tiles()

    def render(self, surface: pygame.Surface) -> None:
        dragged_tile = None

        for row in self.tiles:
            for tile in row:
                if tile.dragged:
                    dragged_tile = tile
                else:
                    tile.render(surface, self.x, self.y)

        if dragged_tile:
            dragged_tile.render(surface, self.x, self.y)

    def __is_match_generated(self, i: int, j: int, color: int) -> bool:
        if (
            i >= 2
            and self.tiles[i - 1][j].color == color
            and self.tiles[i - 2][j].color
        ):
            return True

        return (
            j >= 2
            and self.tiles[i][j - 1].color == color
            and self.tiles[i][j - 2].color
        )

    def __initialize_tiles(self) -> None:
        self.tiles = [
            [None for _ in range(settings.BOARD_WIDTH)]
            for _ in range(settings.BOARD_HEIGHT)
        ]
        for i in range(settings.BOARD_HEIGHT):
            for j in range(settings.BOARD_WIDTH):
                color = random.randint(0, settings.NUM_COLORS - 1)
                while self.__is_match_generated(i, j, color):
                    color = random.randint(0, settings.NUM_COLORS - 1)

                self.tiles[i][j] = Tile(
                    i, j, color, random.randint(0, settings.NUM_VARIETIES - 1)
                )

        if not self.are_there_any_possible_matches():
            self.__initialize_tiles()

    def __calculate_match_rec(self, tile: Tile) -> Set[Tile]:
        if tile in self.in_stack:
            return []

        self.in_stack.add(tile)

        color_to_match = tile.color

        ## Check horizontal match
        h_match: List[Tile] = []

        # Check left
        if tile.j > 0:
            left = max(0, tile.j - 2)
            for j in range(tile.j - 1, left - 1, -1):
                if self.tiles[tile.i][j].color != color_to_match:
                    break
                h_match.append(self.tiles[tile.i][j])

        # Check right
        if tile.j < settings.BOARD_WIDTH - 1:
            right = min(settings.BOARD_WIDTH - 1, tile.j + 2)
            for j in range(tile.j + 1, right + 1):
                if self.tiles[tile.i][j].color != color_to_match:
                    break
                h_match.append(self.tiles[tile.i][j])

        ## Check vertical match
        v_match: List[Tile] = []

        # Check top
        if tile.i > 0:
            top = max(0, tile.i - 2)
            for i in range(tile.i - 1, top - 1, -1):
                if self.tiles[i][tile.j].color != color_to_match:
                    break
                v_match.append(self.tiles[i][tile.j])

        # Check bottom
        if tile.i < settings.BOARD_HEIGHT - 1:
            bottom = min(settings.BOARD_HEIGHT - 1, tile.i + 2)
            for i in range(tile.i + 1, bottom + 1):
                if self.tiles[i][tile.j].color != color_to_match:
                    break
                v_match.append(self.tiles[i][tile.j])

        match: List[Tile] = []

        if len(h_match) >= 2:
            for t in h_match:
                if t not in self.in_match:
                    self.in_match.add(t)
                    match.append(t)

        if len(v_match) >= 2:
            for t in v_match:
                if t not in self.in_match:
                    self.in_match.add(t)
                    match.append(t)

        if len(match) > 0:
            if tile not in self.in_match:
                self.in_match.add(tile)
                match.append(tile)

        for t in match:
            match += self.__calculate_match_rec(t)

        self.in_stack.remove(tile)
        return match

    def calculate_matches_for(
        self, new_tiles: List[Tile]
    ) -> Optional[List[List[Tile]]]:
        self.in_match: Set[Tile] = set()
        self.in_stack: Set[Tile] = set()

        for tile in new_tiles:
            if tile in self.in_match:
                continue
            match = self.__calculate_match_rec(tile)
            if len(match) > 0:
                self.matches.append(match)

        delattr(self, "in_match")
        delattr(self, "in_stack")

        return self.matches if len(self.matches) > 0 else None

    def swap_tiles(self, i1, j1, i2, j2):
        tile1 = self.tiles[i1][j1]
        tile2 = self.tiles[i2][j2]

        (
            self.tiles[tile1.i][tile1.j],
            self.tiles[tile2.i][tile2.j],
        ) = (
            self.tiles[tile2.i][tile2.j],
            self.tiles[tile1.i][tile1.j],
        )

        tile1.i, tile1.j, tile2.i, tile2.j = (
            tile2.i,
            tile2.j,
            tile1.i,
            tile1.j,
        )

        return tile1, tile2

    def are_there_any_possible_matches(self) -> bool:
        old_matches = self.matches
        self.matches = []

        for row in self.tiles:
            for tile in row:
                for di, dj in [
                    # TODO: Create a more friendly alias
                    input_handler.MOUSE_MOTION_UP,
                    input_handler.MOUSE_MOTION_RIGHT,
                    input_handler.MOUSE_MOTION_DOWN,
                    input_handler.MOUSE_MOTION_LEFT,
                ]:
                    og_i = tile.i
                    og_j = tile.j
                    i = tile.i + di
                    j = tile.j + dj
                    if 0 <= i < settings.BOARD_HEIGHT and 0 <= j < settings.BOARD_WIDTH:
                        self.swap_tiles(og_i, og_j, i, j)

                        # TODO: Not sure if performance would really be improved
                        # but we could store the tuples of already calculated matches
                        # to avoid recomputing them, though it's not an extremely
                        # expensive operation
                        found_a_match = self.calculate_matches_for(
                            [self.tiles[og_i][og_j], self.tiles[i][j]]
                        )
                        self.swap_tiles(og_i, og_j, i, j)

                        if found_a_match:
                            self.matches = old_matches
                            return True

        self.matches = []
        return False

    def remove_matches(self) -> None:
        for match in self.matches:
            for tile in match:
                self.tiles[tile.i][tile.j] = None

        self.matches = []

    def clean_tiles(self) -> None:
        for i in range(settings.BOARD_HEIGHT):
            for j in range(settings.BOARD_WIDTH):
                self.tiles[i][j] = None

    def get_falling_tiles(self) -> Tuple[Any, Dict[str, Any]]:
        # List of tweens to create
        tweens: Tuple[Tile, Dict[str, Any]] = []

        # for each column, go up tile by tile until we hit a space
        for j in range(settings.BOARD_WIDTH):
            space = False
            space_i = -1
            i = settings.BOARD_HEIGHT - 1

            while i >= 0:
                tile = self.tiles[i][j]

                # if our previous tile was a space
                if space:
                    # if the current tile is not a space
                    if tile is not None:
                        self.tiles[space_i][j] = tile
                        tile.i = space_i

                        # set its prior position to None
                        self.tiles[i][j] = None

                        tweens.append((tile, {"y": tile.i * settings.TILE_SIZE}))
                        space = False
                        i = space_i
                        space_i = -1
                elif tile is None:
                    space = True

                    if space_i == -1:
                        space_i = i

                i -= 1

        # create a replacement tiles at the top of the screen
        for j in range(settings.BOARD_WIDTH):
            for i in range(settings.BOARD_HEIGHT):
                tile = self.tiles[i][j]

                if tile is None:
                    tile = Tile(
                        i,
                        j,
                        random.randint(0, settings.NUM_COLORS - 1),
                        random.randint(0, settings.NUM_VARIETIES - 1),
                    )
                    tile.y -= settings.TILE_SIZE
                    self.tiles[i][j] = tile
                    tweens.append((tile, {"y": tile.i * settings.TILE_SIZE}))

        return tweens
