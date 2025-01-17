from matplotlib.widgets import Slider


class DiscreteSlider(Slider):
    def __init__(self, *args, **kwargs):
        self.inc = kwargs.pop('increment', 1)
        self.valfmt = '%s'
        Slider.__init__(self, *args, **kwargs)
        self.changecallback = lambda v: ()

    def set_val(self, val):
        if self.val != val:
            discrete_val = int(int(val / self.inc) * self.inc)
            xy = self.poly.xy
            xy[2] = discrete_val, 1
            xy[3] = discrete_val, 0
            self.poly.xy = xy
            self.valtext.set_text(self.valfmt % discrete_val)
            if self.drawon:
                self.ax.figure.canvas.draw()
            self.val = val
            if not self.eventson:
                return

            self.changecallback(discrete_val)

            # for cid, func in self.observers.items():
            #     func(discrete_val)

    def on_changed(self, func):
        self.changecallback = func

    def update_val_external(self, val):
        self.set_val(val)
