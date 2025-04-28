#!/usr/bin/env bash
set -e

BATCHES=(32 64)
LEARNINGRATES=(0.01 0.001 0.0001 0.00001)
DEFAULTBATCH=16
DEFAULTLR=0.01

for B in "${BATCHES[@]}"; do
	echo "Running with batch=$B, default lr=$DEFAULTLR"
	python code/main.py \
		-batch "$B" \
		-lr "$DEFAULTLR" \
		> "results_batch${B}_lr${DEFAULTLR}.log" 2>&1
done


for LR in "${LEARNINGRATES[@]}"; do
	echo "Running with default batch=$DEFAULTBATCH, lr=$LR"
	python code/main.py \
		-batch "$DEFAULTBATCH" \
		-lr "$LR" \
		> "results_batch${DEFAULTBATCH}_lr${LR}.log" 2>&1
done
