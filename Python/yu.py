import scipy.spearmanr

# Dữ liệu
tien_luong = [9, 9, 7, 12, 8, 4, 9, 10, 10, 8]

# Tính hệ số tương quan Spearman
spearman_corr, _ = spearmanr(tuoi_nghe, tien_luong)
print(f'Hệ số tương quan hạng Spearman: {spearman_corr}')
