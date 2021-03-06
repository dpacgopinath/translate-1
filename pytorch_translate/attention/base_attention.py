#!/usr/bin/env python3

import torch.nn as nn


class BaseAttention(nn.Module):
    def __init__(self, decoder_hidden_state_dim, encoder_output_dim):
        super().__init__()
        self.decoder_hidden_state_dim = decoder_hidden_state_dim
        self.encoder_output_dim = encoder_output_dim

    def forward(self, decoder_state, source_hids, src_lengths):
        """
        Input
            decoder_state: bsz x decoder_hidden_state_dim
            source_hids: srclen x bsz x encoder_output_dim
            src_lengths: bsz x 1, actual sequence lengths
        Output
            output: bsz x encoder_output_dim
            attn_scores: max_src_len x bsz
        """
        raise NotImplementedError
