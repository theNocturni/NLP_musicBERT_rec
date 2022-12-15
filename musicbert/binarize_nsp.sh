#!/bin/bash
#

[[ -z "$1" ]] && { echo "PREFIX is empty" ; exit 1; }
PREFIX=$1
[[ -d "${PREFIX}_converteddata_bin" ]] && { echo "output directory ${PREFIX}_converteddata_bin already exists" ; exit 1; }
fairseq-preprocess \
    --only-source \
    --trainpref ${PREFIX}_converteddata_raw/train.txt \
    --validpref ${PREFIX}_converteddata_raw/test.txt \
    --destdir ${PREFIX}_converteddata_bin/input0 \
    --srcdict ${PREFIX}_converteddata_raw/dict.txt \
    --workers 24
fairseq-preprocess \
    --only-source \
    --trainpref ${PREFIX}_converteddata_raw/train.label \
    --validpref ${PREFIX}_converteddata_raw/test.label \
    --destdir ${PREFIX}_converteddata_bin/label \
    --workers 24