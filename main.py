from OpenGL.GL import *
from utils.window_manager import Window
from game import Game
import imgui

class App:
    def __init__(self):
        self.window = Window()
        self.game = Game(self.window.windowHeight, self.window.windowWidth, self.window.impl)
        self.show_main_menu = True

    def RenderLoop(self):
        while self.window.IsOpen():
            inputs, time = self.window.StartFrame(0.0, 0.0, 0.0, 1.0)
            
            if self.show_main_menu:
                self.DrawMainMenu()
            else:
                self.game.ProcessFrame(inputs, time)
            
            self.window.EndFrame()
        
        self.window.Close()

    def DrawMainMenu(self):
        window_w, window_h = 400, 200  # Set the window size
        x_pos = (self.window.windowWidth - window_w) / 2
        y_pos = (self.window.windowHeight - window_h) / 2

        imgui.new_frame()
        # Centered window
        imgui.set_next_window_position(x_pos, y_pos)
        imgui.set_next_window_size(window_w, window_h)
        imgui.begin("Main Menu", False, imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_RESIZE)

        # Center text horizontally
        imgui.set_cursor_pos_x((window_w - imgui.calc_text_size("Press 1: New Game")[0]) / 2)
        if imgui.button("New Game", width=200, height=50):
            self.show_main_menu = False
            self.game.screen = 1
            self.game.InitScene()

        imgui.end()

        imgui.render()
        self.window.impl.render(imgui.get_draw_data())

if __name__ == "__main__":
    app = App()
    app.RenderLoop()