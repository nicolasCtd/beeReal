log_mode = 'w'
out = ''
in_ = ''
tmp = ''
logs = ''
path = ''
media = ''
future = ''

classif = "RUTTNER"
y_max_scatter_plot = 6

# loaded: ditionary. Key=image number (from 1 to 100). Value=0 (image not loaded) or 1 (image loaded)
# edited: ditionary. Key=image number (from 1 to 100). Value=0 (image not edited) or 1 (image edited)
# enabled: ditionary. Key=image number (from 1 to 100). Value=0 (image disabled) or 1 (image enabled)
loaded = dict()
edited = dict()
enabled = dict()
for i in range(1, 101):
    loaded[i] = 0
    edited[i] = 0
    enabled[i] = 1