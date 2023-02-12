/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class GameNormalMode.
*/

#pragma once

#include "src/game_modes/GameModeBase.hpp"
#include <memory>

#include <SFML/Graphics.hpp>
#include <Settings.hpp>

class GameNormalMode : public GameModeBase
{
  public:
    GameNormalMode() : GameModeBase{} {};

    void handle_bird_inputs(const sf::Event &event,
                            std::shared_ptr<Bird> bird) noexcept override;
};
