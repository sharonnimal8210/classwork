
import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing
import arcade


WIDTH = 640
HEIGHT = 480

x = float(input("what is the x value : "))
y = float (input("what is the y value :"))
radius = float(input("what is the radius : "))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.BLUE_GREEN)

# End drawing
arcade.finish_render()
arcade.run()

arcade.draw_circle_filled(50, 50, 30, arcade.color.BLUE_GREEN)

# End drawing
arcade.finish_render()
arcade.run()                                                                  