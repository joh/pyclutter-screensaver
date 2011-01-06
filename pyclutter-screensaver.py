#!/usr/bin/env python
"""
Example clutter screensaver
"""
import os
import clutter
import clutter.x11

class Screensaver(object):
    def __init__(self):
        # Set up Clutter stage and actors
        self.stage = clutter.Stage()
        self.stage.set_title('PyClutter Screensaver')
        self.stage.set_color('#000000')
        self.stage.set_size(640, 480)
        self.stage.set_user_resizable(True)
        self.stage.connect('destroy', self.quit)
        self.stage.connect('notify::allocation', self.size_changed)
        self.stage.connect('key-press-event', self.key_pressed)
        
        # Set up foreign window, if specified
        if 'XSCREENSAVER_WINDOW' in os.environ:
            xwin = int(os.environ['XSCREENSAVER_WINDOW'], 0)
            clutter.x11.set_stage_foreign(self.stage, xwin)
        
        # Text
        self.text = clutter.Text()
        self.text.set_text("PyClutter")
        self.text.set_color(clutter.color_from_string("green"))
        self.text.set_font_name("Helvetica 40")
        
        w, h = self.text.get_size()
        
        print "Text size:", w, h
        
        self.text.set_anchor_point(w/2, h/2)
        self.text.set_position(640./2, 480./2)
        
        self.stage.add(self.text)
        
        # Animation
        self.timeline = clutter.Timeline(duration=5000)
        self.timeline.set_loop(True)

        self.alpha = clutter.Alpha(self.timeline, clutter.EASE_OUT_QUAD)
        self.rot = clutter.BehaviourRotate(alpha=self.alpha,
                                           axis=clutter.Y_AXIS,
                                           angle_start=0.0, angle_end=359.0)
        self.rot.apply(self.text)
        
        self.timeline.start()
        
        self.stage.show_all()
    
    def size_changed(self, *args):
        """ Stage size changed """
        width, height = self.stage.get_size()
        
        print "Stage size: %dx%d" % (width, height)
    
    def key_pressed(self, stage, event):
        """ Key pressed event """
        if event.keyval == clutter.keysyms.Escape:
            self.quit()
    
    def main(self):
        clutter.main()
    
    def quit(self, *args):
        print "Exiting..."
        
        clutter.main_quit()




if __name__ == '__main__':
    screensaver = Screensaver()
    screensaver.main()

    