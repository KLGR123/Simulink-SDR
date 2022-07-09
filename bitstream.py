#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: bitstream
# Author: Jasper Leo
# Copyright: BUPT 2019211127 2019210517
# Description: Homework 1
# GNU Radio version: 3.8.0.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from gnuradio import qtgui

class bitstream(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "bitstream")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("bitstream")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "bitstream")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000
        self.repeat = repeat = 25
        self.phase2 = phase2 = 15
        self.phase1 = phase1 = 15
        self.freqmod = freqmod = 1
        self.bps = bps = 20

        ##################################################
        # Blocks
        ##################################################
        self._phase2_range = Range(0, 90, 1, 15, 200)
        self._phase2_win = RangeWidget(self._phase2_range, self.set_phase2, 'phase2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._phase2_win)
        self._phase1_range = Range(0, 90, 1, 15, 200)
        self._phase1_win = RangeWidget(self._phase1_range, self.set_phase1, 'phase1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._phase1_win)
        self._freqmod_range = Range(1, 5, 1, 1, 200)
        self._freqmod_win = RangeWidget(self._freqmod_range, self.set_freqmod, 'freqmod', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freqmod_win)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0_1_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_char*1, repeat*2)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, bps, 1, 0, phase2)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, bps*freqmod, 1, 0, phase1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 20000))), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_throttle_0_1_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.blocks_throttle_0_1_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_throttle_0_1_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "bitstream")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.samp_rate)

    def get_repeat(self):
        return self.repeat

    def set_repeat(self, repeat):
        self.repeat = repeat
        self.blocks_repeat_0.set_interpolation(self.repeat*2)

    def get_phase2(self):
        return self.phase2

    def set_phase2(self, phase2):
        self.phase2 = phase2
        self.analog_sig_source_x_0_0.set_phase(self.phase2)

    def get_phase1(self):
        return self.phase1

    def set_phase1(self, phase1):
        self.phase1 = phase1
        self.analog_sig_source_x_0.set_phase(self.phase1)

    def get_freqmod(self):
        return self.freqmod

    def set_freqmod(self, freqmod):
        self.freqmod = freqmod
        self.analog_sig_source_x_0.set_frequency(self.bps*self.freqmod)

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.analog_sig_source_x_0.set_frequency(self.bps*self.freqmod)
        self.analog_sig_source_x_0_0.set_frequency(self.bps)



def main(top_block_cls=bitstream, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
