/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the definition of the class Bird.
*/

#include <Settings.hpp>
#include <algorithm>
#include <src/Bird.hpp>

Bird::Bird(float _x, float _y, float w, float h) noexcept
    : x{_x}, y{_y}, width{w}, height{h}, vy{0.f}, vx{0.f}, sprite{Settings::textures["bird"]}
{
    sprite.setPosition(x, y);
}

sf::FloatRect Bird::get_collision_rect() const noexcept
{
    return sf::FloatRect{x, y, width, height};
}

void Bird::jump() noexcept
{
    if (!jumping)
    {
        jumping = true;
    }
}

void Bird::move_x(float _vx) noexcept
{
  vx = _vx;
}

void Bird::toggle_move_l(bool is_moving) noexcept
{
    moving_left = is_moving;
    handle_move_toggle();
}
void Bird::toggle_move_r(bool is_moving) noexcept
{
    moving_right = is_moving;
    handle_move_toggle();
}

void Bird::handle_move_toggle() noexcept
{
    if (moving_right)
    {
        move_x(Settings::JUMP_TAKEOFF_SPEED);
    }
    else if (moving_left)
    {

        move_x(-Settings::JUMP_TAKEOFF_SPEED);
    }
    else
    {
        move_x(0);
    }
}

void Bird::update(float dt) noexcept
{
    vy += Settings::GRAVITY * dt;

    if (jumping)
    {
        Settings::sounds["jump"].play();
        vy = -Settings::JUMP_TAKEOFF_SPEED;
        jumping = false;
    }

    x += vx * dt;
    y += vy * dt;

    sprite.setPosition(x, y);
}

void Bird::render(sf::RenderTarget& target) const noexcept
{
    target.draw(sprite);
}
