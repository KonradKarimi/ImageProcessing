from absl import app, flags, logging

import scipy.io
import numpy as np
from matplotlib import pyplot as plt

FLAGS = flags.FLAGS
flags.DEFINE_string("path_to_mat_file", None, "Path to .mat file location")
flags.mark_flag_as_required("path_to_mat_file")


def extractData(path_to_mat_file):
    mat = scipy.io.loadmat(path_to_mat_file)
    logging.info("Mat file contains: \n%s", scipy.io.whosmat(path_to_mat_file))
    Sig = mat["Sig"]
    fs = mat["fs"]
    Sig = np.hstack(Sig)
    fs = np.hstack(fs)
    return fs[0], Sig


def printPlots(fs, Sig):
    fig = plt.figure()

    plt.subplot(4, 1, 1)
    plt.plot(np.arange(0, len(Sig)/fs, 0.01), Sig)
    plt.title('sygnal czasowy')
    plt.grid(True)
    plt.plot()

    plt.subplot(4, 1, 2)
    FFT = np.fft.ifft(Sig)
    plt.stem(np.real(FFT), use_line_collection=True)
    plt.title('część rzeczywista')
    plt.plot()

    plt.subplot(4, 1, 3)
    plt.title('część urojona')
    FFT = np.fft.ifft(Sig)
    plt.stem(np.imag(FFT), use_line_collection=True)
    plt.plot()

    plt.subplot(4, 1, 4)
    plt.title('modul')
    FFT = np.fft.ifft(Sig)
    plt.stem(np.abs(FFT), use_line_collection=True)
    plt.plot()

    plt.show()


def main(argv):
    del argv  # Unused.

    fs, Sig = extractData(FLAGS.path_to_mat_file)
    printPlots(fs, Sig)


if __name__ == '__main__':
    app.run(main)
