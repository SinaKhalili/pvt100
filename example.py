import time

import pvt100

if __name__ == "__main__":
    print(f"{pvt100.color_bg_blue} Hello, world! {pvt100.style_reset}")

    print(
        f"{pvt100.style_bold} Behold! {pvt100.style_reset} {pvt100.color_bg_red} The bold text! {pvt100.style_reset}"
    )

    print(f"{pvt100.color_bright_cyan} Let's get fancier... {pvt100.style_reset}")

    for i in range(0, 255):
        print(f"{pvt100.color_256(i, 255 - i)} {i:3} {pvt100.style_reset}", end="")
        if i % 16 == 15:
            print()
    print("\n")

    print(
        f"{pvt100.color_bg_bright_white} {pvt100.color_bright_black} And now for something completely different... {pvt100.style_reset}"
    )

    print(f"{pvt100.cursor_set_invisible}")
    for i in range(0, 35):
        print(f"{pvt100.cursor_move_up(1)}", end="", flush=True)
        print(f"{pvt100.cursor_move_forward(1)}", end="", flush=True)
        print(
            f"{pvt100.color_bg_red}   {pvt100.style_reset}",
            end="",
            flush=True,
        )
        time.sleep(0.2)
    print(f"{pvt100.cursor_set_visible}")
