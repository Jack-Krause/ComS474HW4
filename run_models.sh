set -e

BATCHES=(32 64)
LEARNINGRATES=(0.01 0.001 0.0001 0.00001)

for B in "${BATCHES[@]}"; do
	for LR in "${LEARNINGRATES[@]}"; do
		echo "Running with batch=$B, lr=$LR"
		python code/main.py \
			-batch "$B" \
			-lr "$LR" \
		      > "results_batch${B}_lr${LR}.log" 2>&1
	done
done


