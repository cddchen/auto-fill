source /Users/cdd/miniforge3/etc/profile.d/conda.sh
conda activate dl
for (( i = 1; i <= 30; ++i ))
do
    echo "$i task begin."
    {
        python main.py
    } || {
        echo "$i task wrong!"
    }
    
done