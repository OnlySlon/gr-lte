#!/usr/bin/env python
# 
# Copyright 2012 Johannes Demel
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
#

from gnuradio import gr, gr_unittest
import lte_swig
import scipy.io
import os

class qa_pss_tagging_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()
        
        #print os.getpid()
        #raw_input("Press the ANY key!")
        
        offset = 43223  #sample15 = 21839 #sample20 = 43223
        fftl = 512
        cell_id = 124
        N_rb_dl = 6
        
        
        mod=scipy.io.loadmat('/home/demel/exchange/matlab_test_first_freq.mat') 
        mat_u1=tuple(mod['test'].flatten())
        mat_d=range(len(mat_u1))
        for idx, val in enumerate(mat_u1):
            mat_d[idx]=val
        intu=tuple(mat_d[0:100000])
        
        
        self.src  = gr.vector_source_c(intu,False,1)
        #self.tag  = lte_swig.tag_symbol_cc(offset,fftl)
        
        self.tagp = lte_swig.pss_tagging_cc(fftl)
        self.snk  = gr.vector_sink_c(1)
        
        self.tb.connect(self.src, self.tagp, self.snk)#self.tag, 

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data


if __name__ == '__main__':
    gr_unittest.main ()
