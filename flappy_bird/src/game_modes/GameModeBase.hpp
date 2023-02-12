/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class GameModeBase.
*/

#pragma once

#include "src/Bird.hpp"
#include "src/World.hpp"
#include <memory>

#include <SFML/Graphics.hpp>

class GameModeBase
{
  public:
    GameModeBase() {}

    virtual ~GameModeBase() {}

    virtual void handle_bird_inputs(const sf::Event &event,
                                    std::shared_ptr<Bird> bird) noexcept
    {
    }
};
