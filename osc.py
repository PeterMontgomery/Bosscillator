import math
import itertools
import matplotlib.pyplot as plt
def get_sin_oscillator(freq, sample_rate):
    increment = (2 * math.pi * freq) / sample_rate
    return (math.sin(v) for v in itertools.count(start = 0, step = increment))

osc = get_sin_oscillator(freq = 1, sample_rate = 512)
#list comprehension
samples = [next(osc) for i in range(512)]

def get_n(iterator, n):
    return [next(iterator) for i in range(n)]

def plot(xy, r=1,c=1,i=1,title="", xlabel="",ylabel="",yticks=None, xticks=None,**plot_kwargs):
    plt.subplot(r,c,i)
    plt.title(title)
    if len(xy) == 2:
        plt.plot(*xy, **plot_kwargs)
    else:
        plt.plot(xy, **plot_kwargs)
        
    if xticks is not None: plt.xticks(xticks)
    if yticks is not None: plt.yticks(yticks)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

fig = plt.figure(figsize=(8*2,4*2))

hz = 1
osc = get_sin_oscillator(freq=hz, sample_rate=512)
wave = get_n(osc,512)
plot(wave, label=f"{hz} Hz Sine Wave", xlabel = "samples", ylabel="amplitude", color="#323031")

plt.legend(loc='lower right')
plt.show()
fig.savefig("sine.jpg")
