/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class PauseState.
*/

#include <Settings.hpp>
#include <src/states/PauseState.hpp>
#include <src/states/StateMachine.hpp>
#include <src/text_utilities.hpp>

PauseState::PauseState(StateMachine *sm) noexcept : BaseState{sm} {}

void PauseState::enter(std::shared_ptr<World> _world,
                       std::shared_ptr<Bird> _bird) noexcept
{
    world = _world;
    bird = _bird;
}

void PauseState::render(sf::RenderTarget &target) const noexcept
{
    world->render(target);
    render_text(target, Settings::VIRTUAL_WIDTH / 2,
                Settings::VIRTUAL_HEIGHT / 2, "PAUSED",
                Settings::HUGE_TEXT_SIZE, "font", sf::Color::White, true);
}

void PauseState::handle_inputs(const sf::Event &event) noexcept
{
    if (event.type == sf::Event::KeyPressed &&
        event.key.code == sf::Keyboard::P)
    {
        state_machine->change_state("playing", world, bird);
    }
}
