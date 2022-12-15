#!/bin/bash
#

[[ -z "$1" ]] && { echo "PREFIX is empty" ; exit 1; }
PREFIX=$1
[[ -d "${PREFIX}_augplusdata_bin" ]] && { echo "output directory ${PREFIX}_augplusdata_bin already exists" ; exit 1; }
fairseq-preprocess \
    --only-source \
    --trainpref ${PREFIX}_augplusdata_raw/train.txt \
    --validpref ${PREFIX}_augplusdata_raw/test.txt \
    --destdir ${PREFIX}_augplusdata_bin/input0 \
    --srcdict ${PREFIX}_augplusdata_raw/dict.txt \
    --workers 24
fairseq-preprocess \
    --only-source \
    --trainpref ${PREFIX}_augplusdata_raw/train.label \
    --validpref ${PREFIX}_augplusdata_raw/test.label \
    --destdir ${PREFIX}_augplusdata_bin/label \
    --workers 24