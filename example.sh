#!/bin/bash

score=hw1_kaggle_score.csv
cheat=hw1_cheat.txt

python3 collect_score.py \
    --public hw1_public.csv \
    --private hw1_private.txt \
    --students ../ML2021_students.csv \
    --publ-bl 2.03004 1.28359 0.88017 \
    --priv-bl 2.04826 1.36937 0.89266 \
    --output ${score}

python3 get_kaggle.py \
    --competition_id ml2021spring-hw1

python3 find_cheating.py \
    --dir kaggle_output/single_student \
    --id2n kaggle_output/id2name.json \
    --output ${cheat}

python3 convert_to_ntucool.py \
    --orig-file hw1_kaggle_score.csv \
    --id-col 1 \
    --score-col 4 \
    --cool-grade 2022-02-28T1413_成績-機器學習_(EE5184).csv \
    --cool-output ntucool_hw1.csv \
    --title "HW01 Kaggle Score"
