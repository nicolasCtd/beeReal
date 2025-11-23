log_mode = 'w'
out = ''
in_ = ''
tmp = ''
logs = ''
path = ''
media = ''
future = ''

classif = None
seuil_min_abeilles = None
y_max_scatter_plot = None

loaded = dict()
edited = dict()
enabled = dict()

for i in range(1, 101):
    loaded[i] = 0
    edited[i] = 0
    enabled[i] = 1