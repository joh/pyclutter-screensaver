import clutter

stage = clutter.Stage()
stage.set_size(200, 200)
stage.set_color(clutter.Color(0, 0, 0))
stage.connect('destroy', clutter.main_quit)
stage.show()

clutter.main()
